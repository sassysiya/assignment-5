x=int(input('Please enter the Lower limit of the range: '))
y=int(input('Please enter the Upper limit of the range: '))
for i in range(x,y+1):
    if i%7==0 and i%11==0:
        print(i)
