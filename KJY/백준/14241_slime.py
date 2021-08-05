N = int(input())
size = list(map(int, input().split()))
size.sort(reverse=True)  # 최댓값을 구하기 위해, 내림차순으로 정렬

score = 0
total = 0

for i in range(0, N-1): #슬라임 하나 남을 때까지 반복
    score = size[i] * size[i+1] # 슬라임을 합칠 때 얻게되는 점수 (x*y)  # 아래의 size[i+1]을 먼저 받으면, 사이즈가 바껴서 순서는 바꾸면 안됨.
    size[i+1] = size[i] + size[i+1]  ## 슬라임 두개가 합쳐지면 다시 1개가 됨. (x+y)
    total += score

print(total)




