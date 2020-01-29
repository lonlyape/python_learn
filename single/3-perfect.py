'''
完美数又称为完全数或完备数，它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。
'''
import math

print('完美数：')
for x in range(1, 1000):
    list = []
    for y in range(1, int(math.sqrt(x))+1):
        if (x % y) == 0:
            list.append(y)
            list.append(x/y)
    if len(list) > 0:
        sum = 0
        for j in list:
            if j != x:
                sum += j
        if sum == x:
            print(x)


print('素数：')
for x in range(100):
    list = []
    for y in range(2, int(math.sqrt(x))+1):
        if (x % y) == 0:
            list.append(y)
    if len(list) == 0 and x > 1:
        print(x)
