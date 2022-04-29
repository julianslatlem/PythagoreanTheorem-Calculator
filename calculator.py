import math,log,pyperclip

pv,currentX,x,side,doInput,a,b,c=2,0,0,0,True,0,0,0
errors=["69420"]

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

def isvalid(test):
    global x,side,currentX,a,b,c
    if isfloat(test):
        if side==0:
            a=float(a)
            currentX="a"
        if side==1:
            b=float(b)
            currentX="b"
        if side==2:
            c=float(c)
            if x==0:
                side-=1
                log.warning('Equation must have at least 1 "x" variable.')
            elif x==1 and  isfloat(a) and c<=a or x == 1 and isfloat(b) and c<=b:
                side-=1
                log.warning("Value must be bigger than "+'"'+f"{currentX}"+'".')
        side+=1
    elif test=="x":
        if x!=1:
            side+=1
            x+=1
        else:
            log.warning('"'+"x"+'"'+" variable already exists.")
    else:
        log.error(f'Invalid input "{test}".', errors[0])
        
print("x = unknown value\n")

while side==0:
    a=input("a: ")
    isvalid(a)

while side==1:
    b=input("b: ")
    isvalid(b)

while side==2:
    c=input("c: ")
    isvalid(c)
    
if a=="x":
    answer = round(math.sqrt((c*c)-(b*b)),pv)
    print(f"\n√({c}² - {b}²) = \33[3m{answer}\33[0m")
elif b=="x":
    answer = round(math.sqrt((c*c)-(a*a)),pv)
    print(f"\n√({c}² - {a}²) = \33[3m{answer}\33[0m")
elif c=="x":
    answer = round(math.sqrt((a*a)+(b*b)),pv)
    print(f"\n√({a}² + {b}²) = \33[3m{answer}\33[0m")
pyperclip.copy(answer)

log.misc("Press enter to exit.")