h, m = map(int, input().split())
if h == 0 and m < 45:
    m = 60+(m-45)
    h = 23
else:
    if m < 45:
        m = 60 + (m-45)
        h -= 1
    else:
        m -= 45
print("%d %d" %(h,m))