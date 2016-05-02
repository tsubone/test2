#!/usr/bin/env python
# -*- coding: utf-8 -*-


def f():
#    return (1, "abc")
        return 1, "abc"
# 以下のようにリストにしても同じ
# return [1, "abc"]

a, b = f()
print(a) # => 1
print(b) # => abc
print f()
