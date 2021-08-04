
n = int(input())
p = list(map(int, input().split()))
time = []
count = n
sum = 0
p.sort()
for i in range(n):
    sum += p[i] * count
    count -= 1
print(sum)



