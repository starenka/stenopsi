#!/usr/bin/env python
# coding=utf-8
from __future__ import unicode_literals

import pytest

from bs4 import BeautifulSoup

from stenopsi.parser import parse_para
from stenopsi.utils import normalize_whitespace, merge_by_prop


@pytest.mark.parametrize("test_input,expected", [
    ('\n\n     space    oddity', ' space oddity'),
    ('      ', ' '),
    ('\n\n', '\n'),
    ('\n', '\n'),

])
def test_normalize_whitespace(test_input, expected):
    assert normalize_whitespace(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('<p></p>', None),
    ('<p> </p>', None),
    ('<p>\xa0</p>', None),
    ('<p>\n </p>', None),

])
def test_para_is_empty(test_input, expected):
    assert parse_para(BeautifulSoup(test_input)) == expected


@pytest.mark.parametrize("test_input,expected", [
    ('<p><b><u>Místopředseda vlády a ministr financí ČR Jan Fischer</u></b></p>',
     'Místopředseda vlády a ministr financí ČR Jan Fischer'),
    ('<p align="justify"><a href="/sqw/detail.sqw?id=303">Místopředseda PSP Vojtěch Filip</a></p>', 'Místopředseda PSP Vojtěch Filip'),
])
def test_para_person_name(test_input, expected):
    assert parse_para(BeautifulSoup(test_input))['name'] == expected


def test_merge_by_prop():
    assert merge_by_prop([
        dict(name=None, text='1'),
        dict(name=None, text='2'),
        dict(name='a', text='a1'),
        dict(name=None, text='a2'),
        dict(name='b', text='b1'),
        dict(name=None, text='b2'),
        ], 'name', 'text') == [
        dict(name=None, text='12'),
        dict(name='a', text='a1a2'),
        dict(name='b', text='b1b2'),
        ]
