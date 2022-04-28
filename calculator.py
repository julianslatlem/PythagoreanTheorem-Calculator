import math

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("x = unknown value\n")
pv = int(input("Precision value: "))

a = input("a: ")
if isfloat(a):
    a = float(a)
    
b = input("b: ")
if isfloat(b):
    b = float(b)
    
c = input("c: ")
if isfloat(c):
    c = float(c)
    
if a is "x":
    print(round(math.sqrt((c * c) - (b * b)), pv))
elif b is "x":
    print(round(math.sqrt((c * c) - (a * a)), pv))
elif c is "x":
    print(round(math.sqrt((a * a) + (b * b)), pv))
    
print("Press enter to quit.")
input()
