

n=int(input())
x=set(int(i)for i in input().split())
n=int(input())
s=set()
for i in range(n):
    e=int(input())
    s.add(e)
print(len(s))