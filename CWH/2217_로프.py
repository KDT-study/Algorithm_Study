## 전역 변수 설정
N = int(input())  # 로프의 개수
k = []  # 중량


## 메인 코드 부분
for i in range(N):
    k.append(int(input()))

max_w = min(k) * N
print(max_w)


# ## 전역 변수 설정
# N = int(input())
# rope = []
# num = []
#
# ## 메인 코드 부분
# for i in range(N):
#     rope.append(int(input()))
# rope.sort(reverse=True)
# for j in range(N):
#     num.append(rope[j]+(j + 1))
# print(max(num))












