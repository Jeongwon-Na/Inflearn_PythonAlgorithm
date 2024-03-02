import sys
#sys.stdin=open("input.txt", "rt")

#입력 받은 생성 리스트 관련 정보
N=int(input())
listN=list(map(int, input().split()))
indexN=0
M=int(input())
listM=list(map(int, input().split()))
indexM=0

#출력할 리스트 관련 정보
result_list=[]

#생성 리스트 간의 값 비교과정
while indexN<N and indexM<M:
    if listN[indexN]<listM[indexM]:
        result_list.append(listN[indexN])
        indexN+=1
    else:
        result_list.append(listM[indexM])
        indexM+=1

#잔여 요소 추가 후 최종 리스트 반환
if indexN!=N:
    result_list=result_list+listN[indexN::]
else:
    result_list=result_list+listM[indexM::]

for i in result_list:
    print(i, end=' ')
    
