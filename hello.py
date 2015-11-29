#!/usr/bin/env python

import datetime
import math
import sys
import mycalc as hoho
from mycalc import add
#import enum
import sets

print "hoho.add=", hoho.add(1,2)
print "add=", add(1,2)

def squre (n):
    return n*n

class FirstClass:
    a = "hello"
    def m(self):
        print FirstClass.a
        

print "Hello world\n"

print 2

print squre (2)

#FirstClass.a

#FirstClass.m

i = FirstClass ()

print i.a
i.m ()

print "koko"

print datetime.date.today ()

print math.e
