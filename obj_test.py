#!/usr/bin/env python

class MyClass2:
    def __init__(self):
        self.value = 0
        print "This is __init__() method !"

class Prism:
    def __init__ (self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def content (self):
        return self.width * self.height * self.depth

    def test (self, dim):
        return self.width * self.height * self.depth * dim

if __name__ == '__main__':
    print "start.."
    hoho = MyClass2()
    print "hoho.value=", hoho.value

    c1 = Prism (10, 20, 30)
    print "c1.content=", (c1.content())

    c2 = Prism (10, 20, 30)
    print "c1.test", (c1.test(10))

    print "finish.."

    
