n = int(input())

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n):
        yield a
        a, b = b, b + a
first = True
for i in fibonacci(n):
    if not first:
        print(",", end = "")
    print(i, end = "")
    first = False