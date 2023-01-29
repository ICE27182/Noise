#通过缓和曲线加权
import random,time
print('噪声地形生成v2.0')
print('1 将加权方式由原来的线性改为 6x⁵-15x⁴+10x³,x∈[0,1] 使图像更平滑')
print('2 加快了刷新速度 约为每秒66.67行')
print('3 固定了区块大小为16 且每个区块的后一个端点值与该区块后一个区块的前一个端点的值相同')
print('4 地面 水 山 有雪的高山 的高度不在固定 而是受预设的高度限制影响 尽管高度限制只能在代码里改')

chunk,len = 16,72
val_1,val_2 = random.randint(int(len/72),len),random.randint(int(len/72),len)

def smth(x,chunk):  
    return(chunk*(6*(x/chunk)**5-15*(x/chunk)**4+10*(x/chunk)**3))

while True:
    val_3 = val_2
    val_2 = random.randint(int(len/36),len)
    val_1 = val_3
    
    noise = [val_1]
    for x in range(1,chunk):
        noise.append(int(val_1*(chunk-smth(x,chunk))/chunk+val_2*smth(x,chunk)/chunk))
        noise.append(int(val_2*smth(x,chunk)/chunk+val_1*(chunk-smth(x,chunk))/chunk))
    noise.append(val_2)

    for x in noise:
        if x <= int(len/3):  #24
            print('~~'*x, end='')
            print('||'*int(len/3-x))
        elif x <= int(len*4/9):  #32
            print('~~'*x)
        elif x <= int(len*7/9):  #56
            print('~~'*(int(len*4/9)), end='')
            print('**'*(x-int(len*4/9)))
        else:
            print('~~'*int(len*4/9), end='')
            print('**'*(int(len*7/9)-int(len*4/9)), end='')
            print('██'*(x-int(len*7/9)))
    
        time.sleep(0.015)