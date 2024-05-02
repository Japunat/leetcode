i=0
z=[]
while i<len(arr):
    arr.remove(arr[i])
    if len(arr)>0:
        y=max(arr)
        z.append(y)
    elif len(arr)==0:
        z.append(-1)    
print(z)    

