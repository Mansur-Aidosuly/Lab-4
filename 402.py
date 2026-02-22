def even(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

n = int(input())
first = True
for i in even(n):
    if not first:
        print(",", end = "")
    print(i, end = "")
    first = False
    