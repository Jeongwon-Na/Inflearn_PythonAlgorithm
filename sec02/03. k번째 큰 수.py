import sys
#sys.stdin=open("input.txt", "rt")

N, K=map(int, input().split())
mylist=list(map(int, input().split()))
result=set()

#3개씩 뽑을 수 있는 모든 경우 실행
for a in range(N-2):
    for b in range(a+1, N-1):
        for c in range(b+1, N):
            result.add(mylist[a]+mylist[b]+mylist[c])      #자체적으로 값을 중복시키지 않고 저장함

#집합 자료형을 리스트 자료형으로 전환한 후 내림차순 정리
result=list(result)
result.sort(reverse=True)

#K번째에 해당하는 값 출력
print(result[K-1])
