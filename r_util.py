#!/usr/bin/env python3
# -*- coding: utf-8 -*-





def as_dict(sa_result):
    _dict=[]
    for row in sa_result:
        _dict += row
    return _dict