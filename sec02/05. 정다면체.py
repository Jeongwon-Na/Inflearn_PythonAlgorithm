import sys
#sys.stdin=open("input.txt", "rt")

N,M=map(int, input().split())

#출현 빈도수를 저장할 리스트의 생성: 인덱스 번호 0 ~ N+M
count=[0]*(N+M+1)

#모든 경우의 수를 돌며 합을 구해 해당하는 인덱스에 출현 빈도수 저장
for n in range(1, N+1):
    for m in range(1, M+1):
        count[n+m]+=1

#최대 빈도수가 저장된 곳의 추출
max=0
for cnt in count:
    if cnt>max:
        max=cnt

#최대 빈도수인 max에 해당하는 값이 저장된 인덱스의 값을 출력
for i in range(N+M+1):
    if(count[i]==max):
        print(i,end=' ')
