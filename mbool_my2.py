#!/usr/bin/env python

import enum

__my_mode__=1


def IsMbool(a):
    if a == Mbool.T or a == Mbool.F or a == Mbool.I or a == Mbool.M:
        return Mbool.T
    else:
        return Mbool.F

if __my_mode__ == 1:
    Mbool = enum.Enum("Mbool", "T I F M")
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
              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))

#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.I, Mbool.T, Mbool.F, Mbool.M),
#              (Mbool.M, Mbool.M, Mbool.T, Mbool.M),
#              (Mbool.M, Mbool.M, Mbool.M, Mbool.T))
    
#OK1-hoge
#    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.I, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
#              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))
    

    MnotTbl=(Mbool.F, Mbool.I, Mbool.T, Mbool.M)
#    MnotTbl=(Mbool.F, Mbool.M, Mbool.T, Mbool.I)
elif __my_mode__ == 2:
    Mbool = enum.Enum("Mbool", "T F U M")
    print "use mode 2"

    def IsMbool(a):
        if a == Mbool.T or a == Mbool.F or a == Mbool.U or a == Mbool.M:
            return Mbool.T
        else:
            return Mbool.F

    MandTbl=((Mbool.T, Mbool.F, Mbool.U, Mbool.M),
             (Mbool.F, Mbool.F, Mbool.U, Mbool.M),
             (Mbool.U, Mbool.U, Mbool.U, Mbool.M),
             (Mbool.M, Mbool.M, Mbool.M, Mbool.M))
    
    MorTbl=((Mbool.T, Mbool.T, Mbool.T, Mbool.M),
            (Mbool.T, Mbool.F, Mbool.U, Mbool.M),
            (Mbool.T, Mbool.U, Mbool.U, Mbool.M),
            (Mbool.M, Mbool.M, Mbool.M, Mbool.M))

#OK1
    MImplTbl=((Mbool.T, Mbool.U, Mbool.F, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.F, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.M),
              (Mbool.T, Mbool.T, Mbool.T, Mbool.T))

    MnotTbl=(Mbool.F, Mbool.T, Mbool.U, Mbool.M)
else:
    Mbool = enum.Enum("Mbool", "T I F M")
    print "use mode 0"
    MandTbl=((Mbool.T, Mbool.T, Mbool.M, Mbool.M),
             (Mbool.T, Mbool.I, Mbool.F, Mbool.M),
             (Mbool.M, Mbool.F, Mbool.F, Mbool.M),
             (Mbool.M, Mbool.M, Mbool.M, Mbool.M))
    
    MorTbl=((Mbool.T, Mbool.I, Mbool.I, Mbool.T),
            (Mbool.I, Mbool.I, Mbool.I, Mbool.I),
            (Mbool.I, Mbool.I, Mbool.F, Mbool.F),
            (Mbool.T, Mbool.I, Mbool.F, Mbool.M))

    MImplTbl=((Mbool.T, Mbool.I, Mbool.F, Mbool.M),
              (Mbool.M, Mbool.T, Mbool.M, Mbool.M),
              (Mbool.M, Mbool.M, Mbool.T, Mbool.M),
              (Mbool.M, Mbool.M, Mbool.M, Mbool.T))

    MnotTbl=(Mbool.F, Mbool.M, Mbool.T, Mbool.I)

def Mnot(a):
    if IsMbool (a) != Mbool.T:
        return Mbool.M

    return MnotTbl[a.value-1];


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

def Meq(a, b):
    if IsMbool (a) != Mbool.T:
        return Mbool.M
    elif IsMbool (b) != Mbool.T:
        return Mbool.M
    
    if a == b:
        return Mbool.T
    else:
        return Mbool.F

# ===== zennken koutei ((A -> B) && A) -> B =======
def Zennkenn(p, q):
    return Mimpl(Mand(Mimpl(p, q), p), q)

# ===== Distribution law (A && (B || C)) == (A && B) || (A && C) =======
def DistributionLaw1(p, q, r):
    a = Mand(p, Mor(q, r))
    b = Mor(Mand(p, q), Mand(p, r))
    return Meq(a,b)

# ===== Distribution law (A || (B && C)) == (A || B) && (A || C) =======
def DistributionLaw2(p, q, r):
    a = Mor(p, Mand(q, r))
    b = Mand(Mor(p, q), Mor(p, r))
    return Meq(a,b)


# ===== De Morgan !(A || B) == !A && !B =======
def DeMorgan1(p, q):
    a = Mnot(Mor(p, q))
    b = Mand(Mnot(p), Mnot(q))
    return Meq(a,b)

#===== De Morgan !(A && B) == (!A || !B) =======
def DeMorgan2(p, q):
    a = Mnot(Mand(p, q))
    b = Mor(Mnot(p), Mnot(q))
    return Meq(a,b)

print "===== Distribution law (A && (B || C)) == (A && B) || (A && C) ======="
for i in Mbool:
    for j in Mbool:
        for k in Mbool:
            print i, j, k, " ---> ", DistributionLaw1(i,j , k)

print "===== Distribution law (A || (B && C)) == (A || B) && (A || C) ======="
for i in Mbool:
    for j in Mbool:
        for k in Mbool:
            print i, j, k, " ---> ", DistributionLaw2(i,j , k)

print "===== De Morgan !(A || B) == !A && !B ======="
for i in Mbool:
    for j in Mbool:
        print i, j, " ---> ", DeMorgan1(i,j)

print "===== De Morgan !(A && B) == (!A || !B) ======="
for i in Mbool:
    for j in Mbool:
        print i, j, " ---> ", DeMorgan2(i,j)        

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
#        t = Meq(h, m)
        print i, j, " : ", h, m, " ---> ", t

print "===== zennken koutei ((A -> B) && A) -> B ======="
for i in Mbool: #A
    for j in Mbool: #B
        t = Zennkenn(i, j)
        print i, j, "---> ", t

print "===== ganni paradox (A -> (B -> A))======="
for i in Mbool: #A
    for j in Mbool: #B
        t = Mimpl(i, Mimpl(j, i))
        print i, j, "---> ", t
        
