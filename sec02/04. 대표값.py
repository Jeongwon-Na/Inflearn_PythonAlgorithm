import sys
#sys.stdin=open("input.txt", "rt")

N=int(input())
grade=list(map(int, input().split()))

#평균값의 도출
ave=sum(grade)/N
ave+=0.5
ave=int(ave)

#최소의 편차를 찾기 위한 값 x 추출 필요+그의 순서를 찾기 위한 인덱스 idex 추출 필요
min=2147000000
for idex,x in enumerate(grade):
    
    #편차의 절댓값
    value=abs(x-ave)
    
    #더 작은 편차를 발견했을 때
    if value<min:
        min=value     #편차값 갱신
        score=x       #그 때의 grade 저장
        order=idex+1  #그 때의 순서값 저장
        
    #같은 편차를 발견했을 때
    elif value==min:
        if score<x:   #저장한 값보다 탐색중인 값이 양수일 때 갱신
            score=x
            order=idex+1
print(ave, order)
