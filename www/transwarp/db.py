#!/usr/bin/env python
# coding=utf-8

__author__ = "wqliceman"

'''
Database operation module
'''

import time, uuid, functools, threading, logging

# Dict object:

class Dict(dict):
    '''
    Simple dict but support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c=3)
    >>> d2.c
    '3'
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute 's'" % key)

    def __setattr__(self, key, value):
        self[key] = values

def next_id(t=None):
    '''
    Return next id as 50-char string

    Args:
        t: unix timestamp, default to None and using time.tiem().
    '''
    if t is None:
        t = time.time()
    return '%015d%s000' % (int(t*1000), uuid.uuid4().hex)

