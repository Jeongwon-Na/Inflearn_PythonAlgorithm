import sys
#sys.stdin=open("input.txt", "rt")

N, M=map(int, input().split())
numlist=list(map(int, input().split()))
count=0
lt=0   #lt와 rt는 인덱스를 의미
rt=1
total=numlist[0]

while lt<=N:
    #rt가 옮겨지는 조건: total이 기준값보다 작을 때
    #rt 옮겨지며 변화되는 효과: total에서 해당값을 더함&인덱스 rt 하나 증가
    if total<M:
        if rt<N:
            total+=numlist[rt]
            rt+=1
        #이 경우 total이 M보다 작은데 이미 rt는 공백종료항에 도착한 경우 => lt를 아무리 옮겨도 늘어날 total이 M에 다시 도달할 수 있게 늘어날 수 있는 방법 없음 => 종료
        else:
            break
    #lt가 옮겨지는 조건: total이 기준값보다 클 때
    #lt가 옮겨지면서 변화되는 효과: total에서 해당값을 뺌&인덱스 lt 하나 증가
    elif total>M:
        total-=numlist[lt]
        lt+=1
    #lt가 옮겨지는 조건2: total이 기준값과 같을 때
    #lt가 옮겨지면서 변화되는 효과: count 증가&total에서 해당값을 뺌&인덱스 lt 하나 증가
    else:  #total==M
        count+=1
        total-=numlist[lt]
        lt+=1

print(count)
