import sys
#sys.stdin=open("input.txt", "rt")

N, M=map(int, input().split())
numlist=list(map(int, input().split()))
numlist.sort()

startpoint=0
endpoint=N-1

while startpoint<=endpoint:
    midpoint=(startpoint+endpoint)//2
    if numlist[midpoint]==M:
        print(midpoint+1)
        break
    elif numlist[midpoint]>M:
        endpoint=midpoint-1
    else:
        startpoint=midpoint+1
