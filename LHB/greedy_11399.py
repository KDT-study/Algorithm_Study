n = int(input())
time = 0
total = 0
a = list(map(int,input().split()))
a.sort()
for i in range(n):
    time += a[i]
    total += time
print(total)


