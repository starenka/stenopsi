#!/usr/bin/env python
# coding=utf-8

import click

from stenopsi import conf, scrape

@click.group()
def cli():
    pass

@cli.command()
@click.argument('var')
@click.option('--rettype', type=click.Choice(['iterable',]))
def get_conf_var(var, rettype):
    """Gets a conf var"""
    val = getattr(conf, var.upper(), None)
    if rettype == 'iterable':
        for one in val:
            print one
    else:
        print val


@cli.command()
@click.argument('year', type=int)
def jednani_links(year):
    """Gets links for zipped jednani files"""
    for one in scrape.get_zipped_links(year):
        print one

if __name__ == '__main__':
    cli(obj={})        
