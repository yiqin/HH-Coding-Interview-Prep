print("hello world")

fruits = ['apple', 'banana', 'lime']

loud_fruits = [fruit.upper() for fruit in fruits]

print(loud_fruits)

print(enumerate(loud_fruits))

print(loud_fruits[1])

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a)
        a, b = b, a+b
fib(1000)

k = 0 if 1 >= 2 else -1
print(k)