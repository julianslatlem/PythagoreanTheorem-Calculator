import math
import log

errors=["69420"]

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

print("x = unknown value\n")
pv=2

currentX=0
x=0
side=0
doInput=True
while doInput:
    
    while side==0:
        a=input("a: ")
        if isfloat(a):
            a=float(a)
            side+=1
            currentX=f"a"
        elif a=="x":
            if x!=1:
                side+=1
                x+=1
            else:
                log.warning('"'+"x"+'"'+" variable already exists.")
        else:
            log.error(f'Invalid input "{a}".', errors[0])
    
    while side==1:
        b=input("b: ")
        if isfloat(b):
            b=float(b)
            side+=1
            currentX=f"b"
        elif b=="x":
            if x!=1:
                side+=1
                x+=1
            else:
                log.warning('"'+"x"+'"'+" variable already exists.")
        else:
            log.error(f'Invalid input "{b}".', errors[0])
    
    while side==2:
        c=input("c: ")
        if isfloat(c):
            c=float(c)
            if isfloat(a) and c<=a or isfloat(b) and c<=b:
                log.warning("Value must be bigger than "+'"'+f"{currentX}"+'"')
            else:
                side+=1
        elif c=="x":
            if x!=1:
                side+=1
                x+=1
            else:
                log.warning('"'+"x"+'"'+" variable already exists.")
        else:
            log.error(f'Invalid input "{c}".', errors[0])
    
    if x==1:
        doInput=False
    else:
        side=0
        x=0
    
if a=="x":
    print(round(math.sqrt((c*c)-(b*b)),pv))
elif b=="x":
    print(round(math.sqrt((c*c)-(a*a)),pv))
elif c=="x":
    print(round(math.sqrt((a*a)+(b*b)),pv))

log.misc("Press enter to exit.")