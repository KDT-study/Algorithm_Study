# 틀림: line 14, in <module>
#     del box[i]
# IndexError: list assignment index out of range

n=int(input())
box=[]

for i in range(n):
    box.append(i + 1)

print(box)

while n != 1:
    for i in range(0,n,+2):
        del box[i]
    n = len(box)

print(box[0])