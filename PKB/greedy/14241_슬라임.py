n = int(input())
list = list(map(int, input().split()))

list.sort(reverse=True)
score = 0

for i in range(n-1):
    score += list[i] * list[i+1]
    list[i+1] += list[i]
print(score)