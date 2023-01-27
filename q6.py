x=int(input('Please enter the Lower limit of the Range: '))
y= int(input('Please enter the Upper Limit of the Range: '))
for num in range(x,y+1):
    if num>1:
        for i in range(2,num):
            if (num%i==0):
                break
        else:
                print(num)
