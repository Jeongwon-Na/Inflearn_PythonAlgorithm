import sys
#sys.stdin=open("input.txt","rt")

T=int(input())

#전체 TC 실행
for tc in range(1, T+1):

    #입력받은 값을 정수형태로 변환해 각 변수에 저장
    N,s,e,k=map(int, input().split())

    #N 크기의 리스트의 생성과 그 값의 입력
    testlist=map(int, input().split())
    mylist=list(testlist)

    #슬라이싱을 통한 부분리스트 생성과 오름차순 정렬
    ordered_list=mylist[s-1:e]
    ordered_list.sort()
    print(f'#{tc} {ordered_list[k-1]}')
