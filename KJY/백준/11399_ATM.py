n = int(input())

time = 0
total_time = 0

ppl = list(map(int, input().split()))
ppl.sort()

for i in range(n):
    time += ppl[i]
    total_time += time
print(total_time)

