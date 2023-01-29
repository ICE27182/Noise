

def color(val,R=96,G=216,B=250):
    return f"\033[38;2;{int(val*R/255)};{int(val*G/255)};{int(val*B/255)}m██\033[0m"

def Int(val):
    return int(round(val,0))

def fade(x):
    return 6*x**5-15*x**4+10*x**3

def val(x,y,P1,P2,P3,P4):
    # P4 (a,0)     P3 (a,a)
    # P1 (0,0)      P2 (0,a)   
    n1 = P1 * fade((a-x)/a) + P2 * fade(x/a)
    n2 = P4 * fade((a-x)/a) + P3 * fade(x/a)
    W = n1 * fade((a-y)/a) + n2 * fade(y/a)
    return Int(W)

if __name__ == "__main__":
    from random import randint,seed
    from time import sleep
    from os import system
    system('cls')
    print("")
    a = 16
    s = 0
    while True:    
        seed(s)
        P1,P2,P3,P4 = randint(0,255),randint(0,255),randint(0,255),randint(0,255)
        for y in range(a-1,-1,-1):
            for x in range(a):
                print(color(val(x,y,P1,P2,P3,P4)),end="",flush=True)
            print("",flush=True)
        print("\033[F"*(a+15))
        s+=1
        sleep(1/5)