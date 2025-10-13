age = int(input("Enter your age:"))  
has_id=input("Do you have ID (yes/No):")
if age>=18:
    if has_id == "yes":
        print("you can vote")
    else:
        print("you need id to vote")
else:
    print("you are too ypung to vote")