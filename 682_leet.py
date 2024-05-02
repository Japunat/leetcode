operations = ["5","-2","4","C","D","9","+","+"]
x=[]
for ops in operations:
    if ops=='C':
                x.remove(x[-1])
    elif ops=='D':
                y=2*x[-1]
                x.append(y)
    elif ops=='+':
               tot=x[-1]+x[len(x)-2]
               x.append(tot)
    else:
                x.append(int(ops))
print(sum(x))