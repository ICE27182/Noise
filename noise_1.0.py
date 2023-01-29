#噪声算法 自己先写写玩玩呗
#介绍
print('噪声地形生成v1.0')
print('''生成一个区块内的地形(其实就是条直线XD)
两端点数值可手动输入或随机 有检错功能
''')

#输入

print('输入一个区块的大小, 按回车则默认为16')
while True:
    try:
        chunk = input()
        if chunk == '':
            chunk = 16
        if float(chunk) <= 1:
            print(float(chunk))
            chunk = ''
        chunk = int(chunk)
        break
    except ValueError:
        print('输入大于1的数字')
print('输入区块两端点大小, 按回车则随机')
while True:
    try:
        val_1 = input('val_1 = ')
        if val_1 == '':
            import random
            val_1 = random.randint(0,chunk-1)
            print('val_1 = ', val_1)
        if float(val_1) < 0:
            print(float(val_1))
            val_1 = ''
        val_1 = int(float(val_1))
        break
    except ValueError:
        print('输入大于0的数字')
while True:
    try:
        val_2 = input('val_2 = ')
        if val_2 == '':
            import random
            val_2 = random.randint(0,chunk-1)
            print('val_2 = ', val_2)
        if float(val_2) < 0:
            print(float(val_2))
            val_2 = ''
        val_2 = int(float(val_2))
        break
    except ValueError:
        print('输入大于0的数字')

#计算
noise = [val_1]
for x in range(1,chunk):
    noise.append(int(val_2*x/chunk+val_1*(chunk-x)/chunk))
noise.append(val_2)
print(noise)
for x in noise:
    print('██'*x)
print('\n\n\n')
for x in noise:
    print('  '*(x-1),end='')
    print('██')