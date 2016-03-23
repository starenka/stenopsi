#!/usr/bin/env python
# coding=utf-8

import re

import requests

URL_ZIPPED_BASE = 'http://www.psp.cz/eknih/%dps/stenprot/zip/'
URL_ZIPPED = URL_ZIPPED_BASE + 'index.htm'
RE_ZIP_FILE = re.compile(r'.*(\d{3}schuz.zip).*')


def get_zipped_links(start_year):
    base = URL_ZIPPED_BASE % start_year
    r = requests.get(URL_ZIPPED % start_year)
    doc = r.content
    return [base+one.groups()[0] for one in re.finditer(RE_ZIP_FILE, doc)]

