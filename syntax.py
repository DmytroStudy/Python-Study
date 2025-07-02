# Variables
from pyexpat.errors import messages

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



#Cycles
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