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