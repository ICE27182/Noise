#噪声算法 自己先写写玩玩呗
print('噪声地形生成v1.1')
print('1 随机生成区块大小 各区块大小不一样')
print('2 随机生成端点大小')
print('3 一定程度上减小了过大的斜率')
print('4 对于不同高度的地形加以改变组成的字符 可以生成 水 地面 山 有雪的高山')
print('5 会无限绘制区块 每行时间间隔0.02s')
print('6 删除了输入界面')

#输入
import random,time
chunk = random.randint(12,32)
val_1 = random.randint(0,72)
val_2 = random.randint(0,72)


while True:
    #生成端点
    k1 = (val_2-val_1)/chunk
    chunk = random.randint(12,32)
    if val_2 > 64:
        chunk = random.randint(2,24)
    val_3 = val_2
    val_2 = random.randint(0,72)
    n = 0
    while n < 5: 
        if val_2 > 64 or val_2 <32 or (val_2-val_3)*(val_3-val_1) < -0.2 or ((val_2-val_3)*(val_3-val_1) < -0.2 and val_2-val_3 > 0):
            val_2 = random.randint(0,72)
        n+=1
    if k1 < -1:
        chunk = random.randint(4,16)
        val_2 = random.randint(val_3-10,val_3+10)
    if val_3 <= 30 and val_2-val_3 > 30:
        val_2 = random.randint(val_3-10,val_3+30)

    #计算 int(val_2*x/chunk+val_1*(chunk-x)/chunk)
    val_1 = val_3
    noise = [val_1]
    for x in range(1,chunk):
        noise.append(int(val_2*x/chunk+val_1*(chunk-x)/chunk))
    noise.append(val_2)
    
    #绘图  ██  ░░  ░░  ▓▓  ꧁꧂
    for x in noise:
        if x <= 20:
            print('~~'*2,end='')
            print('~~'*(x-2),end='')
            print('||'*(20-x))
        elif x <= 40:
            print('~~'*x)
        elif x <= 60:
            print('~~'*40,end='')
            print('**'*(x-40))
        else:
            print('~~'*40,end='')
            print('**'*20,end='')
            print('██'*(x-60))
        time.sleep(0.02)