#Tow sum---index ??
nums=[2,7,11,15]

target=9
y={}
s=list()
for i in range(len(nums)):
            z={nums[i]:target - nums[i]}
            y.update(z)
for i in range(len(nums)):
        if y[nums[i]] in nums:
            s.append(i)
print(s)