num1=[2,4]
num2=[1,2,3,4]
x={}
z=[]
for i in range(len(num2)):
            x[num2[i]]=i
for num in num1:
        if num in x:
            if x[num]+1 !=len(num2):
                if num2[x[num]+1]>num2[x[num]]:
                 z.append(     num2[x[num]+1])
                else:
                        z.append(-1)
            else:
                   z.append(-1)
print(z)