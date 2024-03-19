#!/usr/bin/env python3

DUVA2DCAT = "https://duva2dcat.luebeck.de/duva2dcat"
CKANDUVA = "https://opendata.smart-hl.city/duva"
DOWNLOADDIR = "/var/www/duva"

from copy import deepcopy
from pathlib import Path
from urllib.request import urlretrieve

from rdflib import Graph, URIRef
from rdflib.namespace import DCAT


def main():
    old_graph = Graph()
    old_graph.parse(f"{DUVA2DCAT}/catalog.ttl")
    new_graph = deepcopy(old_graph)

    for dataset in old_graph.objects(URIRef(f"{DUVA2DCAT}/"), DCAT.dataset):
        for distribution in old_graph.objects(dataset, DCAT.distribution):
            download_url = old_graph.value(distribution, DCAT.downloadURL)
            access_url = old_graph.value(distribution, DCAT.accessURL)

            if access_url.startswith(f"{DUVA2DCAT}/dataset/"):
                basename = access_url[len(f"{DUVA2DCAT}/dataset/"):]
                urlretrieve(download_url, Path(DOWNLOADDIR, f"{basename}.csv"))
                new_url = URIRef(f"{CKANDUVA}/{basename}.csv")

                new_graph.remove((dataset, DCAT.distribution, distribution))
                new_graph.add((dataset, DCAT.distribution, new_url))

                for p, o in old_graph.predicate_objects(distribution):
                    new_graph.remove((distribution, p, o))

                    if p == DCAT.downloadURL or p == DCAT.accessURL:
                        new_graph.add((new_url, p, new_url))
                    else:
                        new_graph.add((new_url, p, o))

    new_graph.serialize(Path(DOWNLOADDIR, "catalog.ttl"))


if __name__ == "__main__":
    main()
