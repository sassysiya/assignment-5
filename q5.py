alpha = 65
n=int(input('Enter the number of rows:'))
for i in range(0,n):
    for j in range(0,i+1):
        char = chr(alpha)
        print(char,end="")
        alpha+=1
    print()
