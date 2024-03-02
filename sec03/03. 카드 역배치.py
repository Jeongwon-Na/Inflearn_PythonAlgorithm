import sys
#sys.stdin=open("input.txt", "rt")

cardlist=list(range(1,21))   #[1, 2, 3, ..., 20]로 초기화

for i in range(10):
    input1, input2=map(int, input().split())

    count=input2-input1+1  #개수
    start_index=input1-1
    end_index=input2-1

    for k in range(count//2):
        tmp=cardlist[start_index]
        cardlist[start_index]=cardlist[end_index]
        cardlist[end_index]=tmp
        start_index+=1
        end_index-=1

for i in cardlist:
    print(i, end=' ')
