#!/usr/bin/env python

import enum

Mbool = enum.Enum("Mbool", "T I F M")

def IsMbool(a):
    if a == Mbool.T or a == Mbool.F or a == Mbool.I or a == Mbool.M:
        return Mbool.T
    else:
        return Mbool.F

MandTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
         (Mbool.I, Mbool.I, Mbool.F, Mbool.M),
         (Mbool.F, Mbool.F, Mbool.F, Mbool.M),
         (Mbool.M, Mbool.M, Mbool.M, Mbool.M))

MorTbl=((Mbool.T, Mbool.T, Mbool.T, Mbool.T),
        (Mbool.T, Mbool.I, Mbool.I, Mbool.I),
        (Mbool.T, Mbool.I, Mbool.F, Mbool.F),
        (Mbool.T, Mbool.I, Mbool.F, Mbool.M))

MnotTbl=(Mbool.F, Mbool.M, Mbool.T, Mbool.I)

def Mand(a,b):
    if IsMbool (a) != Mbool.T:
        return Mbool.M
    elif IsMbool (b) != Mbool.T:
        return Mbool.M

    return MandTbl[a.value-1][b.value-1]

def Mor(a,b):
    if IsMbool (a) != Mbool.T:
        return Mbool.M
    elif IsMbool (b) != Mbool.T:
        return Mbool.M

    return MorTbl[a.value-1][b.value-1]


def Mnot(a):
    if IsMbool (a) != Mbool.T:
        return Mbool.M

    return MnotTbl[a.value-1];


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

print "kkk=%s,%i" % (kkk, 1)

for i in Mbool:
    print i

print MandTbl

print "Hello"

print Mand (1, 2)
print Mand (Mbool.T, Mbool.F)
print a.value

print "=====result======="

for i in Mbool:
    for j in Mbool:
        a = Mnot(Mor(i, j))
        b = Mand(Mnot(i), Mnot(j))
        print i, j, a == b


