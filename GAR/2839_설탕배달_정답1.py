N = int(input())

quotient_5 = N //5
quotient_3 = 0

remainder_5 = N % 5

while (quotient_5 >= 0):
    if (remainder_5 % 3 == 0):
        quotient_3 = remainder_5 // 3
        remainder_5 = remainder_5 % 3
        break
    remainder_5 = remainder_5 + 5
    quotient_5 = quotient_5 -1

# print((remainder_5 == 0) and (quotient_5+quotient_3) or -1)
print(quotient_5 + quotient_3 if (remainder_5 == 0) else -1)
