nums=[]
z=0
x={}
y={}
words = ["hello","world","leetcode"]
chars = "welldonehoneyr"

#print(len(nums))
#print(nums[0])
for char in chars:
    y[char]=chars.count(char)
for word in words:
    count=0
    for i in word:
        x[i]=word.count(i)
        if i in y and x[i]<=y[i]:
            count+=1
    if(count==len(word)):
        z+=count
print(z)
def countCharacters(self, words: List[str], chars: str) -> int:
        
        result = 0
        d={chr(i+96):0 for i in range(1,27)}
        for i in chars:
            d[i]+=1
        for i in words:
            for j in i:
                if  d[j]< i.count(j):
                    break
            else:
                result+=len(i)
        return result
        
