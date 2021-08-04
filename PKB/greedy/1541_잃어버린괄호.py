x = input().split('-')

list = []
# 다 더하기
for i in x:
    sum = 0
    s = i.split('+')
    for j in s:
        sum = sum + int(j)
    list.append(sum)

# 다 빼기
res = list[0]
for i in list[1:]:
    res -= i

print(res)