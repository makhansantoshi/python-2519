student_Name = input("Enter your Name:") 
base_tution_fee = int(input("Enter your Name:base tution fee:"))
Grades = int(input("Enter student's grade level (1-12):"))
if Grades>=12:
    print("apply a 20% discount / apply a 10% discount : ")
elif Grades>=8:
    print("apply a 5% discount")
elif Grades<=6:
    print("apply a no discount")
else:
    print("you have additional discounts")

