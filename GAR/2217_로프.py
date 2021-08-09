N = int(input())

w = []
for i in range(N):
    w.append(int(input()))


w.sort(reverse=True)

total_w = []
for j in range(N):
    total_w.append(w[j]*(j+1))

print(max(total_w))