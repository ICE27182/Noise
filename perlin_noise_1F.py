

def color(val,R=96,G=216,B=250):
    return f"\033[38;2;{int(val*R/255)};{int(val*G/255)};{int(val*B/255)}m██\033[0m"

def Int(val):
    return int(round(val,0))

def dot_product(v,u):
    return v[0]*u[0] + v[1]*u[1]

def fade(x):
    return 6*x**5-15*x**4+10*x**3

def val(x,y,a,v1,v2,v3,v4):
    # P4 (a,0)     P3 (a,a)
    # P1 (0,0)      P2 (0,a)  
     
    u1,u2,u3,u4 = (-x,-y),(-x,1-y),(1-x,1-y),(1-x,-y)
    # u1,u2,u3,u4 = (x,y),(x,y-a),(x-a,y-a),(x-a,y)

    
    V1,V2,V3,V4 = dot_product(v1,u1),dot_product(v2,u2),dot_product(v3,u3),dot_product(v4,u4)
    # V ∈ [-√(2)a², √(2)a²]

    n1 = V1 * fade(1-x) + V2 * fade(x)
    n2 = V4 * fade(1-x) + V3 * fade(x)

    W = n1 * fade(1-y) + n2 * fade(y)
    # return Int(W)
    return W

if __name__ == "__main__":
    from random import randint,seed,uniform
    from time import sleep
    from os import system
    from math import sin,cos,pi
    system('cls')
    print("")
    a = 128
    # seed(0)
    cmax,cmin = 0,0
    while True:
        v1,v2 = uniform(-pi,pi),uniform(-pi,pi)
        v1,v2 = (cos(v1),sin(v1)),(cos(v2),sin(v2))
        v3,v4 = uniform(-pi,pi),uniform(-pi,pi)
        v3,v4 = (cos(v3),sin(v3)),(cos(v4),sin(v4))
        
        for y in range(a):
            for x in range(a):
                c = val(x/a,y/a,a,v1,v2,v3,v4)
                # c = Int((c+512)/4)
                # print(color(c,255,255,255),end="")
                cmax = max(c,cmax)
                cmin = min(c,cmin)
            # print("")   
        # sleep(0.5)
        # if cmin <= -2**0.5 or cmax >= 2**0.5:
        print(cmin,cmax)
