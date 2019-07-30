def main():
    str1 = 'hello world'
    print('str1 = hello word')
    print('字符串长度 len(str1)：%d' % len(str1))
    print('首字母大写 str1.capitalize()：%s' % str1.capitalize())
    print('大写 str1.upper()：%s' % str1.upper())
    print('查找字符串位置 str1.find("or")：%d' % str1.find('or'))
    print('检是否以hel开头 str1.startswith("hel")：%s' % str1.startswith('hel'))
    print('检是否以hel结尾 str1.endswith("hel")：%s' % str1.endswith('hel'))
    print('将字符串以指定的宽度居中并在两侧填充指定的字符 str1.center(50, "*")')
    print(str1.center(50, '*'))
    print('将字符串以指定的宽度靠右放置左侧填充指定的字符str1.rjust(50, " "')
    print(str1.rjust(50, ' '))

    str2 = 'abc123456'
    print('str2 = abc123456')
    print('str2[2]：%s' % str2[2])
    print('str2[2:5]：%s' % str2[2:5])
    print('str2[2:]：%s' % str2[2:])
    print('str2[1::2]：%s' % str2[1::2])
    print('str2[::2]：%s' % str2[::2])
    print('str2[::-2]：%s' % str2[::-2])
    print('检查字符串是否由数字构成 str2.isdigit()：%s' % str2.isdigit())
    print('检查字符串是否以字母构成 str2.isalpha()：%s' % str2.isalpha())
    print('检查字符串是否以数字和字母构成 str2.isalnum()：%s' % str2.isalnum())

    str3 = '   6546   '
    print(str3)
    print('获得字符串修剪左右两侧空格的拷贝 str3.strip()：%s' % str3.strip())


if __name__ == '__main__':
    main()
