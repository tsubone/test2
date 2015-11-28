#!/usr/bin/env python

import enum

Mbool = enum.Enum("Mbool", "T F I M")

def IsMbool(a):
    if a == Mbool.T or a == Mbool.F or a == Mbool.I or a == Mbool.M:
        return Mbool.T
    else:
        return Mbool.F

print Mbool(1)
print Mbool(2)
print Mbool(3)
print Mbool(4)
print Mbool.T.value
print Mbool.T.name
a = Mbool.T
print a
if a == Mbool.T:
    print "hoge"
else:
    print "koko"

kkk = "hoo:" + IsMbool(Mbool.M).name
print kkk

for i in Mbool:
    print i

def mand(a,b):
    print ""

print "Hello world\n"

