# how to write your own function in python
def greet():
    print("Hello, welcome to the Python course!")
greet()  # This will call the greet function and print the welcome message.
def salam(name):
    print(f"Hello {name}, welcome to the Python course!")
print("Enter your name:")
name = input()  # This will take user input and store it in the variable user  
salam(name)  # This will call the salam function and print a personalized welcome message.
# Two types of functions in python: built-in functions and user-defined functions. Built-in functions are those that are already defined in Python, such as print(), len(), and type(). User-defined functions are those that you create yourself, like greet() and salam() in this example.
# in user defined functions, we can also pass parameters to the function. Parameters are variables that are passed to the function when it is called. In the salam() function, name is a parameter that is passed to the function when it is called.
# we can get the return value of a function by using the return statement. The return statement is used to exit a function and return a value to the caller. Here's an example:
def add(a, b):
    return a + b  # This will return the sum of a and b to the caller.
result = add(5, 3)
print("The sum is:", result)  # This will print the result of the add function.
def multiply(a, b):
    return a * b  # This will return the product of a and b to the caller.
result = multiply(5, 3)
print("The product is:", result)  # This will print the result of the multiply function

#function with multiple return values
def calculate(a, b):
    sum_result = a + b
    product_result = a * b
    return sum_result, product_result  # This will return both the sum and product of a and b to the caller.
sum, product = calculate(5, 3)
print("The sum is:", sum)  # This will print the sum result of the calculate function.
print("The product is:", product)  # This will print the product result of the calculate function.