name = input("Enter your name: ")
print("Hello", name)
#input("X: ")
#y = X + 1 
# this would case an error because X is not defined X is string from the input function, and you cannot perform arithmetic operations on a string. To fix this, you should convert X to an integer before performing the addition. Here's the corrected code:
#Two objects can be concatenated using the + operator, but they must be of the same type. For example, you can concatenate two strings or two lists, but you cannot concatenate a string and an integer directly. To concatenate a string and an integer, you need to convert the integer to a string first. Here's an example:
# We need to convert the input to an integer before performing arithmetic operations. Here's the corrected code:
x = int(input("X: "))
print(type(x))  # This will print <class 'int'>, confirming that x is now an integer
y = x + 1
print("Y:", y)  
# only tricky one is bool
z = bool(input("Enter a boolean value (True/False): "))
# falsy values in Python include: False, None, 0, 0.0, '', [], {}, set(), and any other empty or zero-like value. Any non-empty or non-zero value is considered truthy.
print("Z:", z)
print("bool(0):", bool(0))  # This will return False
