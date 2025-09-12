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

#Multiple variables
x,y,z = 10,20,30
print (x+y+z)

x,y,z = 10,20,30
#x,y,z = 10,20,30,40 (LHS = RHS) ValueError: too many values to unpack (expected 3)
print (x+y+z)

s1,s2,s3 = "apple","orange","cherry"
print(s1,s2,s3)

#using Concatenation

name = "santoshi"
age = 25
#print ("My name is " + name + " and im " + age + "years old") 
#TypeError: can only concatenate str (not "int") to str

# using interpolation
print (f"My name is {name} and im {age} years old")

#using different values dynamically 
x,y,z = 10,20,30
age = 25
print(f"Sum of x,y,z,age is: {x+y+z+age}")

#School Student info

student_name = "Samaksh"
student_class = 1
Student_school = "Smart Kids"
print(f"My name is {student_name} im studying in {student_class} class in {Student_school} school")

#Usecase: 1
car_engine_type = "mHwak (CRDi)"
car_Displacement = "2198 cc"
car_Maxpower = "172.bhp@3500rpm"
car_MaxTorque = "400Nm@1750-2750rpm"
Car_No_of_cylinders = 4
car_Valves_per_cylinder = 4
car_turbo_charger = "\u2713"
car_Transmission_type = "automatic"
car_gearbox = "6-speed"
car_drivetype = "4wd"
print (f"Here are the car features: \n Engine type: {car_engine_type} \n Displacemt: {car_Displacement} \n"\
f"Max power: {car_Maxpower}\n Max Torque: {car_MaxTorque}\n No.of cylinders: {Car_No_of_cylinders}" \
f"valves per cylinder: {car_Valves_per_cylinder}\n turbo carger: {car_turbo_charger}\n transmission type: {car_Transmission_type}" \
f"gear box: {car_gearbox}\n drive type: {car_drivetype}" )

#Usecase: 2
product_title = "\033[1m HIGHLANDER"
product_description = "Men white Slim Fit Printed Casual Shirt"
product_ratings = 4.2
product_totalratings = input ("8.5k")
product_price = 461
Product_MRP = 1399
Product_discount = input("67% OFF")

print (f"price details: Maximum Retail Price (incl. of all taxes) RS. {Product_MRP} \n Discount {Product_discount}\n selling price (incl. of all taxes) {product_price}")
