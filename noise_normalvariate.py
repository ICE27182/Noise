import random,time

#H = int(input())
H = 72
len = H
m,s = 0,1

yf = random.randint(1,H+1)

while True:
    y = yf + int(round(random.normalvariate(m,s),0))
    if y < 1:
        y = 1
    elif y > H:
        y = H
    yf,x = y,y
    
    mis = random.randint(0,int(round(len/18,0)))   #让图像没那么平淡
    if x <= int(len/3):  #24
        print('~~'*x, end='')
        print('||'*int(len/3-x))
    elif x <= int(len*4/9):  #32
        print('~~'*x)
    elif x <= int(len*7/9):  #56
        print('~~'*(int(len*4/9)-1), end='')
        print('~'*mis, end='')
        print('**'*(x-int(int(len*4/9)-1+0.5*mis)))
    else:
        print('~~'*(int(len*4/9)-1), end='')
        print('~'*mis, end='')
        print('**'*(int(len*7/9)-int(int(len*4/9)-1+0.5*mis)), end='')
        print('██'*(x-int(len*7/9)))
    time.sleep(1/144)