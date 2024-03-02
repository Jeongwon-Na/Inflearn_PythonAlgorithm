import sys
#sys.stdin=open("input.txt", "rt")

#답안코드는 N개의 자연수를 숫자로 변환해서 리스트에 저장했음
N=int(input())
numlist=list(map(int, input().split()))

#숫자를 입력 받아 그 합을 반환하는 함수
def digit_sum(x):
    sum=0
    while x>0:
        sum+=x%10
        x=x//10
    return sum

#리스트에 저장된 숫자 각각을 사용자정의함수에 전달해 최대값인지 비교
max=float('-inf')
for x in numlist:
    result=digit_sum(x)
    if result>max:
        max=result
        output=x
print(output)
    
