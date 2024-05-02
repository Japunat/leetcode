x={}
s="dog dog dog dog"
pattern="baab"
d=set(pattern)

x={}
s=s.split(" ")
y=[]
i=0
for r in d:
        x[r]=s[i]
        i+=1  
for pat in pattern:
            y.append(x[pat])
            i+=1
print(x)
print(y)


    