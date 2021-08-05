n = int(input())
ropeL = []

# 리스트에 넣기
for i in range(n):
    ropeL.append(int(input()))

# 내림차순 정렬
ropeL.sort(reverse = True)

# 최고 중량 설정할 max_value
max_value = 0

for i in range(n):
    res = ropeL[i] * (i+1)
    max_value = max(max_value, res)

print(max_value)