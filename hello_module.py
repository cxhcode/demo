#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test hello module'

__author__ = 'Jack Chan'

import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print("Hello,World!!!")
    elif len(args) == 2:
        print("Hello,%s" % args[1])
    else:
        print("Too many params!!!")


print(__name__)
# test()
