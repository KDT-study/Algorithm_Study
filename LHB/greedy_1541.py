a = input().split('-')
s = 0
for i in a[0].split('+'):
    s += int(i)
for i in a[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)