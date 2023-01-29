

from random import randint,seed
seed(0)

def brightness(val):
    return f"\033[38;2;{val};{val};{val}m██\033[0m"

def Int(val):
    return int(round(val,0))

def fade(x):
    return 6*x**5-15*x**4+10*x**3

def val(x,y,P1,P2,P3,P4):
    # P4 (16,0)     P3 (16,16)
    # P1 (0,0)      P2 (0,16)   
    n1 = P1 * fade((16-x)/16) + P2 * fade(x/16)
    n2 = P4 * fade((16-x)/16) + P3 * fade(x/16)
    W = n1 * fade((16-y)/16) + n2 * fade(y/16)
    return Int(W)

P1,P2,P3,P4 = randint(0,255),randint(0,255),randint(0,255),randint(0,255)
for y in range(15,-1,-1):
    for x in range(16):
        print(brightness(val(x,y,P1,P2,P3,P4)),end="")
    print("")