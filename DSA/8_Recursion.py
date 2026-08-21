'''Fibonacci series'''
def fib(n):
    if n == 1 or n == 2: return 1
    num = fib(n-2) + fib(n-1)
    return num

# print(fib(5))

'''Multiplication by Addition'''
def multiply(n, m):
    if(m == 1): return n
    return n + multiply(n, m - 1)

# print(multiply(10,9))

'''Reverse a string'''
def reverseStr(s: str):
    if len(s) <= 1: return s
    return s[-1] + reverseStr(s[:-1])

# print(reverseStr('abc'))

'''Sum of elements of an array'''
def sumElements(arr: list):
    if len(arr) < 1: return 0
    elif len(arr) == 1: return arr[0]
    first = arr[0]
    arr.pop(0)
    return first + sumElements(arr)

# print(sumElements([3,3,3]))

'''Count number of digits in a number'''
def countDigits(n):
    if n < 10:
        return 1
    return 1 + countDigits(n // 10)

# print(countDigits(333111))

'''Highest number in an array'''
def highestNumber(arr: list):
    if len(arr) == 1: return arr[0]
    elif not arr: return 0
    return max(arr[0], highestNumber(arr[1:]))

# print(highestNumber([1,2,382,12,4,23,123,234,0,8]))