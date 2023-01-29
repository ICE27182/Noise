

from random import randint,seed
from time import sleep
'''不管那些个 第一版就这么简单怎么来 一个晶格 5次的缓和曲线 梯度向量四选一'''

def color(val,R=255,G=255,B=255):
    return f"\033[38;2;{int(val*R/255)};{int(val*G/255)};{int(val*B/255)}m██\033[0m"

def Int(val):
    return int(round(val,0))

def dot_product(v,u):
    return v[0]*u[0] + v[1]*u[1]

def fade(x):
    return 6*x**5-15*x**4+10*x**3

def ran_dot(u:tuple,gradient):
    if gradient == 0:
        return u[0]+u[1]
    elif gradient == 1:
        return u[0]-u[1]
    elif gradient == 2:
        return -u[0]-u[1]
    elif gradient == 3:
        return -u[0]+u[1]

def value(x,y,gradient1,gradient2,gradient3,gradient4):
    u1,u2,u3,u4 = (-x,-y),(1-x,-y),(1-x,1-y),(-x,1-y)
    val = (ran_dot(u1,gradient1)*fade(1-x) + ran_dot(u2,gradient2)*fade(x)) * fade(1-y) +\
        (ran_dot(u3,gradient3)*fade(1-x)+ran_dot(u4,gradient4)*fade(x)) * fade(y)
    val = val / (2**0.5)
    return (val+1)/2

if __name__ == "__main__":
    seed(0)
    # ran = tuple([randint(0,255) for _ in range(256)])
    # ran = ran+ran
    a = 64
    while True:
        gradient1,gradient2,gradient3,gradient4 = randint(0,3),randint(0,3),randint(0,3),randint(0,3)
        for y in range(a):
            for x in range(a):
                print(color(255*value(x/a,y/a,gradient1,gradient2,gradient3,gradient4)),end="")
            print("")
        sleep(0.75)