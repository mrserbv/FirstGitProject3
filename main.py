from first import nums

def my_func():
    print('OK')

if __name__ == '__main__':
    a = 10
    b = 2
    while b >=0:
        c = nums.devide(a, b)
        my_func()
        print(c)
        b -= 1