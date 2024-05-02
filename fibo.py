a=1
b=2
n=4
if n>2:
    for i in range(n-2):
       c=a+b
       a=b
       b=c
    print(c) 
else:
    print(n)

