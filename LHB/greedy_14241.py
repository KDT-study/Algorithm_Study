n = int(input())
slime = list(map(int, input().split()))
slime.sort(reverse=True)
score = 0
result = 0
for i in range(0,n-1):
    result = slime[i] * slime[i+1]
    slime[i+1] += slime[i]
    score += result
print(score)
