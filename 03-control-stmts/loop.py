# While 
#syntax
#while condition:
#code to repeat
count = 1
while count <=5:
    print(count)
    count += 1

#simulate real world use case for while
atm_correct_pin = 1234
user_given_pin = 0
while user_given_pin != atm_correct_pin:
    user_given_pin = int(input("Enter PIN:"))
print("you can withdraw")

#Infinite Loop
#count = 1
#while True:
    #print(count)
   # count +=1
   #For Loop: use to iterate over a sequence(Multiple)
   #syntax
   #for elements in sequence:
   #statements
text = "python is a general purpose programming language"
for character in text:
    print(character)

#Test to check given object is terable

num = 10
print(type(num))
print(dir(num))

text = "python"
print(type(text))
print(dir(text))

list_nums = [10,20,30]
print(type(list_nums))
print(dir(list_nums))
for num in list_nums:
    print(num)

#For Loop: repeat block of code, if you know number of iterations in advance
print("hi")

#range()
for num in range(10):
    print(num)
for num in range(10):
    print("hi")

for num in range(1,6):
    print(num)

for num in range(1,6,1):
    print(num)

for num in range(2,10,2):
    print(num)

for num in range(1,10,1):
    print(num)

for num in range(10,1,-1):
    print(num)

for num in range(10,1,-2):
    print(num)

#get even numbers Loop with condition
print("printing even numbers from 1 to 20")
num = 2
while num <=20:
    print(num)
    num += 2

#get even numbers Loop with condition
#print("printing even numbers from 1 to 20")
#num = 2
#while num <=20:
   # if num % 2 ==0:
       # print(num)
        #num += 1

#get even numbers
#print("printing even numbers from 1 to 20")
#for num in range(2,22,2):
   # print(num) 

#List of Courses
course_list = ["python", "cloud","devops", "ai"]
for course in course_list:
    print(course)

#Nested Loops
for i in range(1,4):
    for j in range(1,4):
        print(f"{i}x{j} = {i*j}")
    print("---")
#nested Loops
i=1
while i<4:
    j=1
    while j<4:
        print(f"{i}x{j} = {i*j}")
        j+=1
    print("----")
    i+=1
#Branching statements (Jump statements)
#break : exists the loop entirely
for num in range(5):
    if num == 3:
        break #loop will stop here
        print(num)
#branching statements(Jump statements)
#break :exists the loop entirely
for num in range(5):
    if num == 3:
        break
    print(num)
#continue : skip the current iteration and continue the loop
for num in range(5):
    if num == 3:
        continue
    print(num)
# used as place holder:Pass
if 5>9:
    pass
# used as place holder:Pass
for num in range(5):
    if num == 3:
        pass
    print(num)