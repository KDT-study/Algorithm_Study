# 설탕 배달

## 전역 변수 설정
N = int(input())
num = 0  # num = 봉지 수
num_5 = 0

## 메인 코드 부분
while N > 0:
    if N % 5 == 0:
        num_5 = N / 5
        num += num_5
        print(num)
        break
    N -= 3
    num += 1

# if N % 3 == 0:
#     num = N / 3  # num = 봉지 수
#     print(num)
#
# if N % 5 == 0:
#     num = N / 5
#     print(num)
#
# else:
#     print(-1)

else:
    print(-1)