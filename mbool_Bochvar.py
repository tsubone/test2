#!/usr/bin/env python

import enum

Mbool = enum.Enum("Mbool", "T F M")

def IsMbool(a):
    if a == Mbool.T or a == Mbool.F or a == Mbool.M:
        return Mbool.T
    else:
        return Mbool.F

#MandTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#         (Mbool.I, Mbool.I, Mbool.F, Mbool.M),
#         (Mbool.F, Mbool.F, Mbool.F, Mbool.M),
#         (Mbool.M, Mbool.M, Mbool.M, Mbool.M))

#MorTbl=((Mbool.T, Mbool.T, Mbool.T, Mbool.T),
#        (Mbool.T, Mbool.I, Mbool.I, Mbool.I),
#        (Mbool.T, Mbool.I, Mbool.F, Mbool.F),
#        (Mbool.T, Mbool.I, Mbool.F, Mbool.M))

MandTbl=((Mbool.T, Mbool.F, Mbool.M),
         (Mbool.F, Mbool.F, Mbool.M),
         (Mbool.M, Mbool.M, Mbool.M))

MorTbl=((Mbool.T, Mbool.T, Mbool.M),
        (Mbool.T, Mbool.F, Mbool.M),
        (Mbool.M, Mbool.M, Mbool.M))

MnotTbl=(Mbool.F, Mbool.T, Mbool.M)

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


print "=====result 1(De Morgan/Bochvar)======="

for i in Mbool:
    for j in Mbool:
        a = Mnot(Mor(i, j))
        b = Mand(Mnot(i), Mnot(j))
        print i, j, a, b, a == b

print "=====result 2(De Morgan/Bochvar)======="

for i in Mbool:
    for j in Mbool:
        a = Mnot(Mand(i, j))
        b = Mor(Mnot(i), Mnot(j))
        print i, j, a, b, a == b


