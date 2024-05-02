nums=[1,2,1,1,2]
x={}
for nu in nums:
    x[nu]=nums.count(nu)
    if x[nu]>(len(nums)/2):
        y=nu
print(y)      

