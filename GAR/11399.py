n = int(input())
time = list(map(int, input().split()))

time.sort()

time_wait = 0
time_sum = 0

for i in range(n):
    time_wait += time[i]
    time_sum += time_wait

print(time_sum)
