import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())

numlist=[0]*(N+1)
count=0

for i in range(2, N+1):
    if(numlist[i]==0):
        count+=1
        numlist[i]+=1
        for k in range(i, N+1, i):
            numlist[k]+=1

print(count)
