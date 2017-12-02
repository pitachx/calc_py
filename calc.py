#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def multip(one, two):
    m = one*two
    return m

if __name__ == '__main__':
    one = int(sys.argv[1])
    two = int(sys.argv[2])
    print(multip(one, two))
    