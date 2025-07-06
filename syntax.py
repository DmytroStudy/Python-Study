import random

from pyexpat.errors import messages



# Variables

a = None # empty var
b1 = int # assign an object of int type to the var
b2 = 444 # int number
print(a, b1, b2)

c1 = 0b110111100 # 444 in binary system
c2 = 0o674 #  444 in octal system
c3 = 0x1BC #  444 in hexadecimal system

print(c1, c2, c3)

d1 = 3.14 # float number
d2 = 3. # also float
d3 = 4.44e2 # 4.44 * 10^2
print(d1, d2, d3)

e = 1+2j # complex number
print(e, e.real, e.imag)

f1 = "\\Letter1"
f2 = '\tLetter2'
f3 = ("Let" 
      "Ter3")
f4 = '''Let
ter
4'''
print(f1)
print(f2)
print(f3)
print(f4)

g = r"C:\python\name.txt" # r disables \n \t ...
print(g)

h1 = "Dima"
h2 = 44
h3 = f"Name: {h1}, age: {h2}" # with f we can insert vars
print(h3)

i = 37
i = "Abc"
print(i, type(i))



# Console
print("")

print("Hello", end=", ") # automatically end = \n
print("World")

# a = input("a: ")
a = 18
print(f"a = {a}") # insert vars inside ""
print(f"a = {a:0b}") # in binary system



# Operations
print("")

print("6/4 = ", 6/4)
print("6//4 = ", 6//4) # integer division
print("6%4 = ", 6%4)
print("6**4 = ", 6**4)

a=1
a*=4
print("a*=4 = ", a)

b=1.444
print("round(b) = ",round(b), "round(b, 2) = ", round(b, 2)) # round to int, to 2 numbers after '.'



#Binary operations
print("")

print("2&5 = ", 2&5) # logical AND
print("2|5 = ", 2|5) # logical OR
print("2^5 = ", 2^5) # logical XOR
print("~2 = ", ~2) # logical !
print("5>>2 =", 5>>2) # shift digits to the right
print("5<<2 = ", 5<<2) # shift digits to the left



# Comparison operations
print("")

a = 10
b = 1
print("1 < 5 and 10 < 5 :", 1 < 5 and 10 < 5) # and
print("1 < 5 or 10 < 5 :", 1 < 5 or 10 < 5) # or
print("not 1 < 5:", not 1 < 5) # not

print("Hel in Hello :", "Hell" in "Hello") # in
print("Hel not in Hello :", "Hell" not in "Hello") # not in



# If statement
print("")

a = 5
if a < 5:
      print("a < 5")
      print("00000")
elif a > 5:
      print("a > 5")
      print("11111")
else:
      print("a = 5")
      print("22222")



# Cycles
print("")

a = 10
while a > 0:
      print(a, end=" ")
      a = a - 1
      if a == 2: break
else: print("end")


message = "Hello"
for letter in message:
      print(letter, end=" ")
else: print("")


for  i in range(1, 20, 2): # sequence from 1 to 10 by 2
      if i % 5 == 0: continue
      print(i, end=" ")
else: print("")



# Functions
print("")

def add(a, b):
      print(a+b)

add(10, 5)


def sub(a, b):
      def calculate(a,b): return a - b # local function
      print(calculate(a,b))

sub(10, 5)


def hello(name="Dima"): # default value
      print(f"Hello, {name}")

hello()
hello("Phineas")
hello(name = "Ferb")


def register(name, *, age, password): # All parameters (to the right of *) or (to the left of /) receive values by name only
      print(f"Hello, {name}, {age}, {password}")
      id = random.randint(1, 100000)
      print("Your id:", id)

register("Dima", age = 18, password = "123456789")


def nums(*nums): # indefinite number of values
      for n in nums: print(n, end="/")
      print("")

nums(10, 6, 99, 52, 67)


a = nums # function as a type
a(1, 2, 3)


def do_function(a, b, func):
      func(a, b)

do_function(1, 2, add)


def div(a,b): return a/b
def mul(a,b): return a*b

def select_op(op):
      if op == "/": return div
      elif op == "*": return mul
      elif op == "+": return add
      elif op == "-": return sub
      return None

operation = select_op("*")
print(operation(1, 2))

calc_x2 = lambda x: x^2 # anonymous function



# Type conversion: int -> float -> complex
print("")

# int()
a1 = int(4.9) # 4
a2 = int("4") # 4
a3 = int(True) # 1
a4 = int(False) # 0

# float()
b1 = float(4) # 4.0
b2 = float("4.9") # 4.9

# str()
c1 = str(4.9) # "4.9"
c2 = str(True) # "True"



# Scope of variables
print("")

name = "Tom"

def say_hi():
      name = "Ben" # local var hides a global var with the same name
      print("Hi, " + name + "!")

def say_bye():
      global name # global variable
      print("Bye, " + name + "!")

def say_whatsup():
      word = "whats"

      def say_whats():
            nonlocal word # var from the surrounding function
            print(word, end="")

      say_whats()
      print("up")

say_hi()
say_bye()
say_whatsup()



# Closure
print("")

def outer():
      n = 5  # lexical environment - local variable

      def inner():
            nonlocal n
            n += 1  # lexical environment operations
            print(n)

      return inner


fn = outer()  # fn = inner
# function has memorized its lexical environment and can access and modify it
fn()  # 6
fn()  # 7
fn()  # 8



# Decorator
print("")

def decorate(input_func): # Decorator function
      def output_func():
            print("*****************")
            input_func()
            print("*****************")

      return output_func



@decorate  # decorator application to function hello()
def hello():
      print("Hello World!")

hello()
