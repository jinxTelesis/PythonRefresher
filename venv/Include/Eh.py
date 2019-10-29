
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







