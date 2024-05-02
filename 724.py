nums=[1,2,3]
x=sum(nums)
print(x)
y=0
a=-1
for i in range(len(nums)):
            z=x-y-nums[i]
            if y==z:
                a=i
            y+=nums[i]
print(a)