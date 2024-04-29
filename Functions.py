'''
Block of statements that perform the specific tasks & are reusable
'''

def add(num1,num2):
    num3=num1+num2
    return num3

n1=int(input("Enter the first Number"))
n2=int(input("Enter the second Number"))
n3=add(n1,n2)
print(n3)
    