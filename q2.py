x=int(input('Please enter the Lower limit of range:'))
y=int(input('Please enter the Upper limit of range:'))
p=int(input('Please enter the number to be divided by:'))
for i in range(x,y+1):
    if i%p==0:
        print(i)
