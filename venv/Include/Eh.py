
import fibo

s ='hi'

print(s[1])

squares = [1,4,9,16,25]

print(squares)

print(squares[:])

squares + [36,49,64,81,100]

cubes = [1,8,27,65,125]

4 ** 3

cubes.append(216)
cubes.append(7 ** 3)
cubes

letters =['a','b','c','d','e','f','g']
print(letters)

letters[2:5] = ['C','D','E']

letters = ['a','b','c','d']

len(letters)

# Fibonacci series
# sum of two elements defines next
a, b = 0,1
while a < 10:
    print(a)
    a, b = b, a+b # that slick double assignment

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a + b


x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative chagned to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

words = ['cat','window','defensestrate']

for w in words:
    print(w, len(w))

# Strategy: Iterate over a copy
for user, status in user.copy.items():
    if stats == 'inactive':
        del users[user]

# Strategy: Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

for i in range(5):
    print(i)

range(5,10)

range(0,10,3)

range(-10,-100,-30)

a = ['Mary','had','a','little','lamb']
for i in range(len(a)):
    print(i, a[i])

sum(range(4))


for n in range(2,10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals',x,'*',n//x)
            break
    else:
        # loop fell through without find a factor
        print(n, 'is a prime number')


words = ['cat','window','defensestrate']

for w in words:
    print(w,len(w))

words = ['cat','window','defensestrate']

for w in words:
    print(w, len(w))

# Strategy: Iterate over a copy, so you dont have currenceny issues
for user, status in users.copy().items():
    if status == 'inactive':
        del  users[user]

for i in range(5):
    print(i)

range(5,10)

range(0,10,3)

a = ['Mary','had','a','little','lamb']

for i in range(len(a)):
    print(i,a[i])

print(range(10))

sum(range(4))

list(range(4))

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without find a factor

while True:
    pass

class MyEmptyClass:
    pass

def initlog(*args):
    pass # Remember to implement this!

def fib(n):
    '''Print a Fibonacci series up to n.'''
    a, b = 0, 1 # double assignment so cool!
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)

def foo(name, **kwargs):
    return 'name' in kwargs

#def foo(name,/,**kwargs):
#    return 'name' in kwargs

def concat(*args, sep="/"):
    return sep.join(args)

def concatalso(*args, sep="-"):
    return sep.join(args)

def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

f(0)


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])

pairs

def my_function():
    '''Do nothing, but domcument it.

    No, really, it does not do anything bro.
    :return:
    '''
    pass

print(my_function.__doc__)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

fruits.count('apple')

fruits.count('tangerine')

fruits.index('bannana')

fruits.index('banana',4) # Find next banana starting a postion 4 bro

fruits.reverse()

fruits.append('grade')

fruits.sort()

fruits.pop()

stacke =[3,4,5]

stacke.append(6)
stacke.append(7)

stacke

stacke.pop()

stacke.pop()

stacke.pop()

from collections import  deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")

squares = []
for x in range(10):
    squares.append(x**2)

squares

squares = list(map(lambda  x: x**2,range(10)))

squares = [x**2 for x in range(10)]

vec = [-4,-2,0,2,4]

[x * 2 for x in vec]

[x for x in vec if x >= 0]

[abs(x) for x in vec]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

[(x, x**2) for x in range(6)]

# this creates a list of 2-tuples like (number,square)
[(x,x**2) for x in range(6)]

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]

vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

vec = [[1,2,3], [4,5,6], [7,8,9]]

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]

del a[2:4]

t = 12345, 54312, 'hello!'
t[0]

u = t,(1,2,3,4,5)
v = ([1, 2, 3], [3, 2, 1])


empty = ()

singleton = 'hello',

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

'orange' in basket

a = set('abracadabra')
b = set('alacazam')

# set comprehension
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)

a | b
a - b
a & b

# dictionary comprehension
{x: x**2 for x in (2,4,6)}

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

for k, v in knights.items():
    print(k,v)


for i in reversed(range(1,10,2)):
    print(i)

import math

knights = {'gallahad': 'the pure', 'robin': 'the brave'}

filtered_data = []

for value in raw_date:
    if not math.isnan(value):
        filtered_data.append(value)




fibo.fib(1000)

import fibo as fib
fib.fib(500)

from fibo import fib as fibonacci

import sys

sys.path.append('/ufs/guido/lib/python')

s = 'Hello, world.'

str(s)

repr(s)

print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))


f = open('workfile','w')

with open('workfile') as f:
    read_data = f.read()

# can check that the file was automatically closed with resources
f.closed

f.read()

f.read() # will be blank


f.readline()

f.readline()

f.readline()

for line in f:
    print(line, end='')

f.write('This is a test\n')

value = ('the answer', 42)

s = str(value) # convert the tuple to string
f.write(s)

f = open('filex','rb+')

f.write(b'01234567def')

f.seek(5)

f.read(1)

f.read(1)

import json
json.dump([1,'simple','list'])

#json.dump(x f)

# x = json.load(f)

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Opps! That was no valid number. Try again...")

# raise NameError('HiThere')


class Error(Exception):
    '''Base class for exceptions'''
    pass

class InputError(Error):
    """Exception raised for erros in the input.

    Attributes:
        expression -- input expression in whcih the error occured"""

    def __init__(self, expression,message):
        self.expression = expression
        self.message = message


class TransitionError(Error):
    """Raised when an operation attemps a state transiion that not allowed"""

    def __init__(self,previous,next,message):
        self.previous = previous
        self.next = next
        self.message = message

try:
    raise keyboardInterrupt
finally:
    print('Goodbye, world!')

def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

class MyClass:
    """A simple class"""
    i = 12345

    def f(self):
        return 'hello world'

x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0,-4.5)
x.r, x.i

class Dog:

    kindr = 'canine'

    def __init__(self,name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')

d.kind
e.kind

def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)

f(0)

# Function Annotations

def f(ham: str, eggs: str = 'eggs')-> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

'12'.zfill(5)

'-3.14'.zfill(7)

#entire file
f.read()

# first line
f.readline()


for line in f:
    print(line, end='')

f.write('blah blah')

value = ('the answer',42)

s = str(value)

f.write(s)

json.dumps([1,'simple','list'])

json.dump(x,f)

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()


try:
    raise Exception('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:',err)


raise NameError('HiThere')

try:
    raise NameError("HiThere")
except NameError:
    print('An exception flew by!')
    raise

class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input"""

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed."""

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

try:
    raise KeyboardInterrupt
finally:
    print('Goodbye,world!')

def bool_return():
    try:
        return True
    finally:
        return False

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2,1)

#bad
for line in open("myfile.txt"):
    print(line, end="")

with open("myfile.txt") as f:
    for line in f:
        print(line, end="")


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "global spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment test:", spam)
    do_nonlocal()
    print("After nonlocal assignment test:", spam)
    do_global()
    print("After global assignment test:", spam)


scope_test()
print("In global scope test:", spam)

class MyClass:
    """A class example"""
    i = 12345

    def f(self):
        return 'hello world'


x = MyClass()

class Complex:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0,-4.5)
x.r, x.i

#instance objects

x.counter = 1
while c.counter <10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter

class Dog:

    kind = 'canine' # class variable shared by all instances

    def __init__(self, name):
        self.name = name

d = Dog('Fido')
e = Dog('Buddy')

d.kind
e.kind
d.name
e.name

class Dog:

    tricks = []

    def __init__(self,name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)


# python lookup if name occurs in both instance and class, lookup will mask based on instance

class Warehouse:
    purpose = 'storage'
    region = 'west'

w1 = Warehouse()

print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose,w2.region)


# Function defined outside the class
def f1(self, x, y):
    return min(x, x+y)

class C:
    f = f1

    def g(self):
        return 'hello world'

    h = g

class Bag:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def addtwice(self, x):
        self.add(x)
        self.add(x)

# base class can be in another module as so
class DerivedClassName(modname.BaseClassName):
    pass

class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)








