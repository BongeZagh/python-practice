# 4.7. 定义函数o
# 这一段用的循环函数
# return 那一段没学，快速过下 July 26 2023
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(3000)

