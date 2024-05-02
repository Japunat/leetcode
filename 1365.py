
nums=[3,1,2,4]
for i in range(len(nums)):
            if nums[i]%2==0:
                j=i-1
                while j>=0:
                    temp=nums[j+1]
                    nums[j+1]=nums[j]
                    nums[j]=temp
                    j-=1
print(nums)