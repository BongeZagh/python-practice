for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:  #这里是算余数 
            #  range(start, stop, step) 如果3个数字
            # sum(range(2,5,3)) 所以等于2
            # (n,10)
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number质数')

