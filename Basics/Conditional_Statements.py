'''

if-elif-else
if(condition):
    statement
elif(condition):
    statement2
else
    statement3

'''

light=input("Colour of light is:-")
if(light=="red"):
    print("Stop")
elif(light=="yellow"):
    print("Wait")
elif(light=="green"):
    print("Go")
else:
    print("Light is Broken")


'''
Conditional Statements can be of 3 types:-
if-elif-else
if-elif
if
'''

'''
Ternary Operator in python
Single line If, It can be written as:-
variable_name=value1 if condition else value2 or
statement1 if condition else statement2
'''

age=int(input("enter age:-"))
old="Yes" if age > 30 else "No"
print(old)

'''
Clever If- Ternary Operator
variable_name=(false_val,true_val)[condition]
'''

young=("No","Yes")[age<30]
print(young)
