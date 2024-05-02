# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
c=list(int(i) for i in input().split())
a=set()
a.update(c)
m=int(input())
d=list(int(i)for i in input().split())
b=set()
b.update(d)
e=a^b
f=sorted(e)
for f in f:
  print(f)