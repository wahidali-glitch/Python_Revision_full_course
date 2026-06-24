name = 'Wahid' 
print(name) #string
# but if we want to print a message we can use """ code """
message = """This is a multi-line string.
It can span multiple lines."""
print(message)
# useful function for getting the length of string is len() function
course = "Python Programming"
print(len(course)) #length of string
# also string with index 
print(course[0]) #first character of string
print(course[-1]) #last character of string
print(course[-1]) #last character of string
print(course[0:6]) #first 6 characters of string
course = "Python \"Programming\"" # this is how we can use double quotes inside a string
print(course)
 # hash sign (#) is used to write comments in python, comments are ignored by the interpreter and are used to explain the code to other developers or to yourself when you come back to the code after a long time  
course = "Python \n Programming"
print(course) # \n is used to create a new line in a string