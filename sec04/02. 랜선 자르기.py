import sys
#sys.stdin=open("input.txt", "rt")

K, N=map(int, input().split())
linelist=[]
for _ in range(K):
    linelist.append(int(input()))

startcount=1
endcount=max(linelist)

#같은 길이의 막대기를 몇 개 가지고 있는지
def Count(len):
    cnt=0
    for x in linelist:
        cnt+=(x//len)
    return cnt

#탐색 시작
while startcount<=endcount:
    midcount=(startcount+endcount)//2
    #원하는 개수 이상만큼 얻었을 때
    if Count(midcount)>=N:
        result=midcount
        startcount=midcount+1
    #아직 원하는 개수를 얻지 못했을 때
    else:
        endcount=midcount-1
print(result)
