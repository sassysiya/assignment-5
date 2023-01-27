a=float(input('Please enter the Length of First side: '))
b=float(input('Please enter the Length of Second side: '))
c=float(input('Please enter the Length of the second side: '))
while a and b and c>0:
    if a+b>c and b+c>a and a+c>b:
        s=(a+b+c)/2
        import math
        Area=math.sqrt(s*(s-a)*(s-b)*(s-c))
        print('The Area of the Triangle is: ',Area)   
        break 
    else:
        print('Triangle does not exists.')
        break
