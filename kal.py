candies=[12,1,12]    
extraCandies=10
a=max(candies)
result=[]
for i in range(len(candies)):
            x=candies[i]+extraCandies
            if x>=a:
                result.append('true')
            else:
                result.append('false') 
print(result)
       