## 전역 변수 설정
N = int(input())
A = [i for i in range(1, N + 1) if i % 2 == 0]  # 문자열 사용 위해 A 생성
# list comprehension 사용

## 메인 코드 부분
while len(A) != 1:
    # print(A)
    for i in range(0, len(A), 2):
        # A.pop(i)
        A.pop()
        # print(A)

    result = A[0]
    print(result)
    break

