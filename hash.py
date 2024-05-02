# geek for geek question 
x=list(input().split())
#x=[1,2]
print(x)
y={}
for i in range(len(x)):
    if x[i] == 'a':
        y[x[i+1]]=x[i+2]
    elif x[i]=='b':
        if y[x[i+1]] in y:
           print(y[x[i+1]])
        else:
            print('-1')
    elif x[i]=='c':
        print(len(y))
    elif x[i]=='d':
        y.pop(x[i+1])

