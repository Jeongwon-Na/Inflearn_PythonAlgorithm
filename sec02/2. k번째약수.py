import sys
#sys.stdin=open("input.txt", "rt")

N, K=map(int, input().split())      #map(함수, 객체)

divisor=[]

for i in range(1, N+1):
    if(N%i==0):
        divisor.append(i)

num=len(divisor)
if(K>num):
    print(-1)
else:
    print(divisor[K-1])
