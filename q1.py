def reverse(r):
    str = ""
    for i in r:
        str = i + str
    return str
 
r = str(input('Please enter the string to be reversed:'))
 
print("The reversed string is : ", end="")
print(reverse(r))
