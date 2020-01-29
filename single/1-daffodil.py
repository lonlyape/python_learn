'''
水仙花数
1^3 + 5^3+ 3^3=153
'''

for x in range(100, 1000):
    low = x % 10
    mid = x // 10 % 10
    hig = x // 100
    if low**3+mid**3+hig**3 == x:
        print(x)
