import timeit
from timeit import Timer

def test1():
    l=[]
    for i in range(1000):
        l=l+[i]

def test2():
    l=[]
    for i in range(1000):
        l.append(i)

def test3():
    l=[i for i in range(1000)]#list comprehensation

def test4():
    l=list(range(1000))

t1=Timer("test1()","from __main__ import test1")
print("concat",t1.timeit(number=1000),"milliseconds")
t2=Timer("test2()","from __main__ import test2")
print("append",t2.timeit(number=1000),"milliseconds")

    
