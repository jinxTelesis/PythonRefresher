
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












