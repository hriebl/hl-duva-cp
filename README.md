# hl-duva-cp

Download and redirect TTL and CSV data from a DUVA2DCAT endpoint, so that it can be served as static web content. Developed by [@hriebl](https://github.com/hriebl) for the [Hanseatic City of Lübeck](https://luebeck.de). *Not an official product of the Hanseatic City of Lübeck*.

## Requirements

The script hl-duva-cp.py depends on Python and rdflib, which should already be installed on systems running CKAN and ckanext-dcat.

## Setup

1. Configure the variables `DUVA2DCAT`, `CKANDUVA` and `DOWNLOADDIR` in hl-duva-cp.py.
2. Run hl-duva-cp.py once and set up a cron job to repeat this step regularly (probably daily).
3. Configure Apache/Nginx/etc. to serve `DOWNLOADDIR` (default: /var/www/duva) as static web content from `CKANDUVA` (default: <https://opendata.smart-hl.city/duva>).
4. Configure CKAN to harvest `CKANDUVA/catalog.ttl` (default: <https://opendata.smart-hl.city/duva/catalog.ttl>) instead of the DUVA2DCAT endpoint.
