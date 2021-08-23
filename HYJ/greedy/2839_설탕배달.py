

sugar = int(input())
bag_5 = sugar//5

if sugar % 5 == 0:
    print(bag_5)
elif sugar % 5 != 0:
    for i in range(bag_5,-1,-1):
        if (sugar - 5*i)%3 == 0:
            global bag_3
            bag_3 = (sugar - 5*i)//3
            print(i+bag_3)
            break
        else:
            bag_3 = 0
if bag_3 == 0:
    print("-1")     # 구현이 어려웠던 부분



################1차시도################
# n = int(input())
#
# if n >= 5 and n%5%3 == 0:
#     k = n//5
#     a = n%5
#     b = a//3
# elif n >= 5 and n%5%3 != 0 and n%3 ==0:
#     k = n//3
#     b = 0
# #elif
# else:
#     k = -1
#     b = 0
#
# print(k+b)