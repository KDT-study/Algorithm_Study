list1 = []
num, price = map(int, input().split())
count = 0

for i in range(num):
    list1.append(int(input()))
    #print(list1)
list1.sort(reverse = True)
for coin in list1:
    count += price // coin
    price %= coin

print(count)
