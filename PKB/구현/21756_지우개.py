num = int(input())
list1 = [-1]    # index=0의 값 임의로 설정 ( 0 이외 값 )

# 데이터 넣기
for i in range(1, num+1):
    list1.append(i)

while len(list1) != 2:    # index=0,1만 존재할 때까지

    for i in range(1, len(list1), 2):
        list1[i] = 0
    while 0 in list1:
        list1.remove(0)   # 모든 0을 제거

print(list1[1])