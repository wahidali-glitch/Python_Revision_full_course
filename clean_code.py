age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to vote")
else:
    print("You are not old enough to vote") 
    print("Please wait until you are 18.")

#chaining comparison operators

age = int(input("Enter your age: "))
if 18 <= age < 65:
    print("You are eligible to work")
else:
    print("You are not eligible to work")