#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import os
import json
import logging

import click

from stenopsi import conf, scrape, parser

PWD = os.path.dirname(os.path.abspath(__file__))
log = logging.getLogger(__name__)


@click.group()
@click.option('--log-level', type=click.Choice([logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR]), default=logging.INFO)
def cli(log_level):
    logging.basicConfig(level=log_level)


@cli.command()
@click.argument('var')
@click.option('--rettype', type=click.Choice(['iterable', ]))
def get_conf_var(var, rettype):
    """Gets a conf var"""
    val = getattr(conf, var.upper(), None)
    if rettype == 'iterable':
        for one in val:
            print(one)
    else:
        print(val)


@cli.command()
@click.argument('year', type=int)
def obdobi_links(year):
    """Gets links for zipped obdobi files"""
    for one in scrape.get_zipped_links(year):
        print(one)


@cli.command()
def parse():
    """Parse all years and stores them as json"""

    for year in conf.YEARS:
        log.info('Parsing year %d' % year)
        path = os.path.join(PWD, conf.DATA_DIR, str(year))
        parsed = parser.parse_year(path)

        tar = os.path.join(path, 'parsed.json')
        log.info('Dumping parsed data as JSON to %s' % tar)
        with open(tar, 'wb') as f:
            json.dump(parsed, f, ensure_ascii=True, indent=4)


if __name__ == '__main__':
    cli(obj={})
