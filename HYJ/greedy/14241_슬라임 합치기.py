n=int(input())
a=list(map(int, input().split()))
a.sort()

w = a[n-1] + a[n-2]
score = a[n-1]*a[n-2]

if (n-2) > 0 :
  for i in range (n-2,0,-1): # -1을 넣고 안 넣고 차이가 있네?
    score += a[i-1] * w
    w += a[i-1]

print(score)


# s1 = a[n-1] + a[n-2]
# score = a[n-1] * a[n-2]

# s2 = a[n-3] + s1
# score += a[n-3] * s1

# s3 = a[n-4] + s2
# score += a[n-4]*s2

# x, y = map(int, input().split())
# 4 / 2.5.7.9 => 185 
