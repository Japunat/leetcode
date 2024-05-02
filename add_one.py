sum=0
digits=[1,2,3]
y=[]
for i in range (len(digits)):
            x=len(digits)-(i+1)
            sum+=digits[i]*pow(10,x)
total=sum+1
res = list(map(int, str(total)))
print(res)
    ##
     
class Solution(object):
    def plusOne(self, digits):
        my_str = ''.join(map(str,digits))
        add = int(my_str)+1
        return [int(num) for num in str(add)]
        
     
