#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import glob
import os
import logging
import itertools

from bs4 import BeautifulSoup
from joblib import Parallel, delayed

from conf import WORKERS
from utils import get_dirs, normalize_whitespace, merge_by_prop

log = logging.getLogger(__name__)


def parse_para(el):
    text = normalize_whitespace(el.text).strip()

    if not text:
        return None

    name = None

    name_els = el.select('a') or el.select('b > u')
    if name_els:
        first = name_els[0]
        first.extract()
        name = first.text

    return dict(name=name, text='\n'.join(el.stripped_strings))


def parse_session_html(html):
    soup = BeautifulSoup(html, 'lxml')  # better results with broken docs in these cases

    return filter(None, map(parse_para, soup.select('body > p')))


def parse_session_file(path):
    log.debug('Parsing %s' % path)
    with open(path, 'rb') as f:
        return parse_session_html(f.read())


def parse_session(path):
    log.debug('Parsing session %s' % path)
    files = glob.glob(os.path.join(path, 's*.htm'))

    return path, merge_by_prop(list(itertools.chain.from_iterable([parse_session_file(f) for f in files])))


def parse_year(path, workers=WORKERS):
    #@TODO add & parse session metadata
    log.info('Parsing year data at "%s", using %d workers' % (path, workers))
    sessions = sorted(get_dirs(path))

    return dict(Parallel(n_jobs=workers)(delayed(parse_session)(one) for one in sessions))
