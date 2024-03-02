import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())
casenum=0

for i in range(N):
    str=input().lower()
    cnt=len(str)
    for k in range(cnt//2):
        if str[k]!=str[cnt-1-k]:
            answer="NO"
            break
        else:
            answer="YES"
    casenum+=1
    print(f'#{casenum} {answer}')
