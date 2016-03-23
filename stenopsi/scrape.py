#!/usr/bin/env python
# coding=utf-8
import logging

import requests
from lxml import html

log = logging.getLogger(__name__)

URL_ZIPPED_BASE = 'http://www.psp.cz/eknih/%dps/stenprot/zip/'
URL_ZIPPED = URL_ZIPPED_BASE + 'index.htm'

def get_zipped_links(start_year):
    url = URL_ZIPPED % start_year

    log.debug('Searching %s for zip links' % url)
    r = requests.get(url)
    doc = html.fromstring(r.content)    
    doc.make_links_absolute(url)
    
    return [l[2] for l in doc.iterlinks() if l[2].endswith('.zip')]

