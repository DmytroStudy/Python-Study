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



