result=[]

n=int(input('Enter the number of elements in the list:'))

for i in range(0,n):
    eleme=int(input())
    
    result.append(eleme)


print(result)

from collections import Counter

count=Counter(result)
print(count)
