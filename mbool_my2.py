#!/usr/bin/env python

import enum

__my_mode__=1

Mbool = enum.Enum("Mbool", "T I F M")

def IsMbool(a):
    if a == Mbool.T or a == Mbool.F or a == Mbool.I or a == Mbool.M:
        return Mbool.T
    else:
        return Mbool.F

def IsMeq(a, b):
    if IsMbool (a) != Mbool.T:
        return Mbool.M
    elif IsMbool (b) != Mbool.T:
        return Mbool.M
    
    if a == b:
        return Mbool.T
    else:
        return Mbool.F


if __my_mode__ == 1:
    print "use mode 1"
    MandTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
             (Mbool.I, Mbool.I, Mbool.F, Mbool.M),
             (Mbool.F, Mbool.F, Mbool.F, Mbool.M),
             (Mbool.M, Mbool.M, Mbool.M, Mbool.M))
    
    MorTbl=((Mbool.T, Mbool.T, Mbool.T, Mbool.M),
            (Mbool.T, Mbool.I, Mbool.I, Mbool.M),
            (Mbool.T, Mbool.I, Mbool.F, Mbool.M),
            (Mbool.M, Mbool.M, Mbool.M, Mbool.M))

#Kleene- + Bochvar    
#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.I, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
#              (Mbool.M, Mbool.M, Mbool.M, Mbool.M))

#Kleene(tmp) + Bochvar    
#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))

#OK1->NG
#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.I, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))

# OK2->NG
#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.I, Mbool.I),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.T),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))

#OK1
    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.F, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))


    MnotTbl=(Mbool.F, Mbool.I, Mbool.T, Mbool.M)
#    MnotTbl=(Mbool.F, Mbool.M, Mbool.T, Mbool.I)
else:
    print "use mode 0"
    MandTbl=((Mbool.T, Mbool.T, Mbool.M, Mbool.M),
             (Mbool.T, Mbool.I, Mbool.F, Mbool.M),
             (Mbool.M, Mbool.F, Mbool.F, Mbool.M),
             (Mbool.M, Mbool.M, Mbool.M, Mbool.M))
    
    MorTbl=((Mbool.T, Mbool.I, Mbool.I, Mbool.T),
            (Mbool.I, Mbool.I, Mbool.I, Mbool.I),
            (Mbool.I, Mbool.I, Mbool.F, Mbool.F),
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

def Mimpl(a,b):
    if IsMbool (a) != Mbool.T:
        return Mbool.M
    elif IsMbool (b) != Mbool.T:
        return Mbool.M
    
    return MImplTbl[a.value-1][b.value-1]

def Mnot(a):
    if IsMbool (a) != Mbool.T:
        return Mbool.M

    return MnotTbl[a.value-1];

print "===== De Morgan !(A || B) == !A && !B ======="
for i in Mbool:
    for j in Mbool:
        a = Mnot(Mor(i, j))
        b = Mand(Mnot(i), Mnot(j))
        print i, j, " ---> ", IsMeq(a,b)

print "===== De Morgan !(A && B) == (!A || !B) ======="
for i in Mbool:
    for j in Mbool:
        a = Mnot(Mand(i, j))
        b = Mor(Mnot(i), Mnot(j))
        print i, j, " ---> ", IsMeq(a,b)

print "===== Law of noncontradiction !(A && !A) ======"
for i in Mbool:
    b = Mnot(Mand(i, Mnot(i)))
    print i, " ---> ",  b

print "===== A->B ======"
for i in Mbool:
    for j in Mbool:
        a = Mimpl(i, j)
        print i, j, a
    
print "===== Transitive relation ((A->B) & (B->C)) -> (A->C))======"
for i in Mbool: #A
    for j in Mbool: #B
        for k in Mbool: #C
            h1 = Mimpl(i, j)
            h2 = Mimpl(j, k)
            h = Mand(h1, h2)
            m = Mimpl(i, k)
            t = Mimpl(h, m)
            print i, j, k, " ---> ", t

print "===== Contraposition (A->B) -> (!B->!A)======"
for i in Mbool: #A
    for j in Mbool: #B
        h = Mand(i, j)
        m = Mimpl(Mnot(j), Mnot(i))
        t = Mimpl(h, m)
        print i, j, " : ", h, m, " ---> ", t
