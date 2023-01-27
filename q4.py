size=int(input('Please enter the number of lines of pattern: '))
for i in range(size):
    for j in range(i+1):
        print('*', end='')    
    print()

for i in range(size):
    for j in range(size-i-1):
        print('*', end='')
    print()    
