#working Variables
#syntax -->var_name =value
#syntax for text data is to enclose the text inside ' ' or " "
student_name = "Ravi"
student_age = 20
student_gpa = 9.5
student_passed = True

dynamic_variable = 10
print(type(dynamic_variable))
dynamic_variable = 9.5
print(type(dynamic_variable))
dynamic_variable = False
print(type(dynamic_variable))
dynamic_variable = "Hello world"
print(type(dynamic_variable))

a=10
print(id(a))

b=20
print(id(b))

c=10
print(id(c))

a_list = [10,20,30]
print(type(a_list))
print(id(a_list))

c_list = [10,20,30]
print(id(c_list))

x = "Python "
y = "is "
z = "Awesome"

#output is "Python is Awesome"
# print(xyz) NameError: name 'xyz' is not defined
# + (add two numeric values and add them)
# + (when used with numeric it is called as addition operator)
# +(when used with text it is called as "Concatenation")

#what is Concatenation? -> Joining of multiple strings.
print (x+y+z) #Concatenation

x=10
y=20
z=30
print(x+y+z) #addition operator

a = "10"
b = "10"
print (a+b)
