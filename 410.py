def new_list(n, k):
    for i in range(k):
        yield n

n = list(input().split())
k = int(input())

for i in new_list(n, k):
    print(*n, end = " ")