import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())

result=0

for i in range(N):
    caselist=list(map(int,input().split()))
    caselist.sort()
    a, b, c=caselist

    if a==b and b==c:
        award=10000+a*1000
    elif a==b or b==c:
        award=1000+b*100
    else:
        award=c*100

    if award>result:
        result=award

print(result)
