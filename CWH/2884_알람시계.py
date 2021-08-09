# 알람시계

## 전역 변수 설정
H, M = map(int, input().split())

## 메인 코드 부분
if M > 44:
    print(H, M - 45)
elif H > 0 and M < 45:
    print(H - 1, M + 15)
else:
# elif H <= 0 and M < 45:
    print(23, M + 15)

#
#
# #
# H, M = map(int,input().split())
# MM=0
# if (45<=M<=59):
#   MM = M-45
#   print(H, MM)
# elif (M <45 and 1<=H):
#   H +=-1
#   MM = M+15
#   print(H, MM)
# else:
#   print(23, M+15)
