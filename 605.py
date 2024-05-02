flowerbed=[1,0,0,0,0,1]
j=0
n=1
for i in range(len(flowerbed)):
            
                if flowerbed[i] !=1:
                    if i+1 <len(flowerbed) and i-1>=0:
                        if flowerbed[i+1] == 0 and flowerbed[i-1] == 0:
                            j+=1
                            flowerbed[i]=1 
                    elif i+1 >=len(flowerbed):
                        if flowerbed[i-1]==0:
                           j+=1
                           flowerbed[i]=1
                    elif i-1==-1:
                        if flowerbed[i+1]==0:
                            j+=1
                            flowerbed[i]=1 
                           
                        
if j==n:
            print(j)
else:
            print(j)
print(flowerbed)