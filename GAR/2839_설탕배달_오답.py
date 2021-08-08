N = int(input())

if N % 5 == 0 or N % 3 == 0:

    if (N % 5) == 0:
        bag_5 = N//5
        print(bag_5)
    elif (N % 5) % 3 == 0:
        bag_5 = N//5
        bag_3 = (N % 5)//3
        bag_total = bag_5 + bag_3
        print(bag_total)
    elif (N % 5) == 1 or (N % 5) == 4:
        if ((N % 5) + 5) % 3 == 0:
            bag_5 = N//5 -1
            bag_3 =  ((N % 5) + 5) // 3
            bag_total = bag_5 + bag_3
            print(bag_total)
    elif (N % 5) == 2:
        if ((N % 5) + 5*2) % 3 == 0:
            bag_5 = N//5 -2
            bag_3 =  ((N % 5) + 5*2) // 3
            bag_total = bag_5 + bag_3
            print(bag_total)
    else:
        bag_3 = N // 3
        print(bag_3)

elif (N % 5) % 3 == 0:
        bag_5 = N//5
        bag_3 = (N % 5)//3
        bag_total = bag_5 + bag_3
        print(bag_total)

elif (N % 5) == 1 or (N % 5) == 4:
    if ((N % 5) + 5) % 3 == 0:
        bag_5 = N//5 -1
        bag_3 =  ((N % 5) + 5) // 3
        bag_total = bag_5 + bag_3
        print(bag_total)

elif (N % 5) == 2:
    if ((N % 5) + 5*2) % 3 == 0:
        bag_5 = N//5 -2
        bag_3 =  ((N % 5) + 5*2) // 3
        bag_total = bag_5 + bag_3
        print(bag_total)

else:
    print(-1)

