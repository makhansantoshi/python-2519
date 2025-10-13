# Conditional Statements
#if Syntax
#if Condition:
#    statements
if True:
    print("Correct Indentation")
    print("correct")
if 5 < 2:
    print("valid condition")

#if else
if 5 > 2:
     print("valid condition")
else:
     print("Invalid condition") 

#Voting App
age = 12
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")   

#input() - >for taking input from user
value = input("Enter some value:")
print(value)
print(type(value))

#dynamic Voting App
age = int(input("Enter your age:"))  
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")   

# Teranary Operator
# value-if-true if condition else value-if-false
age = int(input("Enter your age:"))  
status = "you can vote" if age >= 18 else "you cannot vote"
print(status)

#elif Ladder - Multiple conditions
Marks = int(input("Enter your Marks:"))
if Marks>=90:
    print("A")
elif Marks>=80:
    print("B")
elif Marks>=75:
    print("c")
elif Marks>=50:
    print("D")
elif Marks>=35:
    print("E")
else:
    print("Fail")

#Match-case - (using Switch in java)
#this was introduced in python 3.1 version onwards
Choice = int(input("Enter your Choice (1-5):"))
match Choice:
    case 1:
        print("Python")
    case 2:
        print("Java")
    case 3:
        print("Cloud")
    case 4:
        print("Devops")
    case _:
        print("Please select from valid Coice (1-5) only")

     