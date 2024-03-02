import sys
#sys.stdin=open("input.txt", "rt")

str=input()
numlist=[]

for i in str:
    if i.isalpha():
        continue
    else:
        numlist.append(i)

value=int("".join(numlist))
print(value)

count=0
for k in range(1, value+1):
    if value%k==0:
        count+=1
print(count)
