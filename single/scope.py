def foo():
    b = 'hello'
    global a
    a = 200

    def bar():
        c = True
        print(a)
        print(b)
        print(c)

    bar()


if __name__ == '__main__':
    a = 100
    foo()
    print(a)
