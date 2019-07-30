import random

answer = random.randint(1, 100)
print('猜数字游戏，大小范围为1~100')
counter = 0
while True:
    counter += 1
    number = int(input('请输入：'))
    if(number > answer):
        print('大了点')
    elif(number < answer):
        print('小了点')
    else:
        print('恭喜你猜对了')
        break
print('你共猜了%d次' % counter)
if(counter > 7):
    print('你的智商余额明显不足')
