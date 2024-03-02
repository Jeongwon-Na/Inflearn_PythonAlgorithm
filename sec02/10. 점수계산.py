import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())
resultlist=list(map(int,input().split()))

grade=0
plus=0
for i in resultlist:
    if i==0:
        plus=0
    else:
        plus+=1
    grade+=plus
print(grade)
