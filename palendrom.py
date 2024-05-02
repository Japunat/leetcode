low=100
high = 1782
count=0
tot=0
tt=0
m=[]
for i in range(low,high+1):
    tot=0
    tt=0
    if i>10:
        s=str(i)
        if len(s)%2==0:
                mid=len(s)//2
                f=int(s[:mid])
                while(f):
                    z=f%10
                    tot+=z
                    f=f//10
                l=int(s[mid:])
                while(l):
                    j=l%10
                    tt+=j
                    l=l//10
                if tot==tt:
                    count+=1
                    m.append(i)
print(m)
