result=[]

for i in range(0,10):
   num= int(input('Enter the value: '))
   result.append(num)

print('Positive values:',[a for j,a in enumerate(result) if a>=0])
print('Negative values:',[a for j,a in enumerate(result) if a<0])    

print('Odd values:',[a for j, a in enumerate(result) if a%2==1 and a>0 ])
print('Even Values:',[a for j,a in enumerate(result) if a%2==0 and a>0 ])

from collections import Counter
count=Counter(result)
print(count)
