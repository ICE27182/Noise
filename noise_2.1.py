#通过缓和曲线加权
import random,time
print('噪声地形生成v2.1')
print('1 增加了自定义 区块大小 高度限制 刷新速度 的功能')
print('2 使山没那么平淡 连接处变得粗糙')
print('3 使生成平均斜率大于30度的地形的概率减半 即增加了平地的量')
print('4 我写代码注释了')

#输入
def TypeIn(default):
    while True:
        try:
            v = input('')
            if v == '':
                v = default
            if float(v) <= 1 or float(v) != int(float(v)):
                v = ''
            v = int(float(v))
            break
        except ValueError:
            print('输入大于1的整数')
    return(v)
print('输入区块两端点大小, 按回车则默认16 (不确定就默认)')
chunk = TypeIn(16)
print('输入高度限制大小, 按回车则默认72 (如果图像有错误应减小)')
len = TypeIn(72)
print('输入每秒刷新的行数, 按回车则默认 50 行/s')
speed = TypeIn(50)

#取随机数
val_1,val_2 = random.randint(int(len/72),len),random.randint(int(len/72),len)

def smth(x,chunk):
    return(chunk*(6*(x/chunk)**5-15*(x/chunk)**4+10*(x/chunk)**3))

while True:
    val_3 = val_2
    val_2 = random.randint(int(len/36),len)
    
    if ((val_2-val_3)/chunk)**2 >= 1/3:   #让地形平一点 平均斜率超过30°就再尝试一次生成
        val_2 = random.randint(int(len/36),len)

    val_1 = val_3

    #计算值
    noise = [val_1]
    for x in range(1,chunk):
        noise.append(int(val_1*(chunk-smth(x,chunk))/chunk+val_2*smth(x,chunk)/chunk))
        noise.append(int(val_2*smth(x,chunk)/chunk+val_1*(chunk-smth(x,chunk))/chunk))
    noise.append(val_2)

    #显示图像
    for x in noise:
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
    
        time.sleep(1/speed)