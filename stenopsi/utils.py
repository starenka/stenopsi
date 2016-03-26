#!/usr/bin/env python
# coding=utf-8

import os
import re


def get_dirs(path):
    return filter(os.path.isdir, [os.path.join(path, f) for f in os.listdir(path)])


def normalize_whitespace(text):
    return re.sub(r'(\s)+', r'\1', text)


def merge_by_prop(data, key='name', val='text'):
    if not data:
        return []

    ret, prev, acc = [], data[0].get(key), ''
    for one in data:
        if one.get(key) == prev or one.get(key) is None:
            acc += one.get(val)
        else:
            ret.append(dict(name=prev, text=acc))
            prev, acc = one.get(key), one.get(val)

    ret.append(dict(name=prev, text=acc))

    return ret
