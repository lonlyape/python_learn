import sys

print('---------------------string')
s1 = 'hello, world'
s2 = "hello, world"
s3 = """
hello, 
world
"""
print(s1, s2, s3)

s4 = '\u9a86\u660a'
s5 = '\141\142\143\x61\x62\x63'
print(s4, s5)

s6 = 'hello ' * 3
print(s6)
print(s6+s4)
print('lle' in s1)

s7 = '0123456789'
print(s7[3::2])
print(len(s7))
print('upper:', s1.upper())
print('title:', s1.title())
print('find', s1.find('ll'))
print('find', s1.find('k'))
print('startswith:检查字符串是否以特定字符开头:', s1.startswith('he'))
print('endswith:检查字符串是否以特定字符结尾:', s1.endswith('he'))
print('isdigit:检查字符串是否由数字构成:', s7.isdigit())
print('isalpha:检查字符串是否以字母构成:', s1.isalpha())
print('isalnum:检查字符串是否以字母和数字构成:', s1.isalnum())
print('strip:获得字符串修剪左右两侧空格之后的拷贝:', s1.strip())

print('\n\n---------------------list')
list_1 = [0, 2, 1, 3, 4, 5, 6, 7, 8, 9]
print(sorted(list_1))
list_1.sort(reverse=True)
list_2 = ['hello', 'world']
print(list_1)
print(list_2*2)
print(list_1[-1])
for index, item in enumerate(list_2):
    print(index, item)
list_1.append(10)
list_1.insert(1, 'insert')
list_1.extend(['extend'])
if 3 in list_1:
    list_1.remove(3)
list_1.pop(1)
list_1.clear()
print(list_1)

f = [x**2 for x in range(1, 100)]
print(sys.getsizeof(f))
