import sys
#sys.stdin=open("input.txt", "rt")

#역전함수: 정수형 파라미터, 정수형 반환형
def reverse(x):
    newnum=0
    while x>0:
        newnum=newnum*10+(x%10)
        x=x//10
    return newnum

#소수판단함수: 정수형 파라미터, 불형 반환형
def isPrime(x):
    if x==1: return False
    for a in range(2,x):
        if x%a==0:
            return False
    return True

N=int(input())
numlist=list(map(int,input().split()))

for k in numlist:
    value=reverse(k)
    if isPrime(value):
        print(value, end=' ')
