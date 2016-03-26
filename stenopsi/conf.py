#!/usr/bin/env python
# coding=utf-8

import multiprocessing

DATA_DIR = 'data'
YEARS = (  # 1993, 1996, 1998, 2002, 2006, #these don't have zips
    2010, 2013,)

WORKERS = multiprocessing.cpu_count()
