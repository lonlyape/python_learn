'''
斐波那契数列
20个
'''
list = [1, 1]
while len(list) < 20:
    a = list[-1]+list[-2]
    list.append(a)
print(list)
print(len(list))
