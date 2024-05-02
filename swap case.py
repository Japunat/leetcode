strs=list(input().split())
strs.sort(key=len)
minmem=len(strs[0])
x=''
for i in range(minmem):
    for j in range(1,len(strs)):
        if strs[0][i]==strs[j][i]:
            y=strs[0][i]
        else:
            y=''
    x=x+y
print('the longest common word is ',x) 
