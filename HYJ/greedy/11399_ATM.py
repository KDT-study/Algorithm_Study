N = int(input())
a = list(map(int, input().split())) ###

a.sort()
sum=0

for i in range(N):
  sum += a[i]*(N-i)

sum

# p=[]
# for i in range(N):
#   p.append([])
#   p[i]=int(input())

# for i in range(N):
#   p.append(int(input())) 

# ----------잘못된 코드--------
# N = int(input())
# p=[]
# for i in range(N):
#   p[i] = int(input())
