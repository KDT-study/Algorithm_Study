

rope_n = int(input())
rope =[]

for i in range(rope_n):
    rope.append(int(input()))

rope.sort()

k = rope[0]*rope_n
for i in range(rope_n):
    if rope[i]*(rope_n-i) >= k:
        k= rope[i]*(rope_n-i)
        total = rope[i]*(rope_n-i)
    else:
        total = k
print(k)