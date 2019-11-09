import weakref, gc

from array import array
from collections import deque

class A:
    def __int__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)


a = A(10) # create a reference

d = weakref.WeakValueDictionary()

d['priamry'] = a
d['primary']

del a

gc.collect() # garbage collect

a = array('H',[4000,10,700,22222])
sum(a)

a[1:3]


d = deque(["task1","task2","task3"])
d.append("task4")
print("Handling",d.popleft())

