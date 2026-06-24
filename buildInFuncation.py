course = "python programming"
length = len(course)
print(length) #length of string
upper_course = course.upper()
print(upper_course) #this will convert the string to uppercase
lower_course = course.lower()
print(lower_course) #this will convert the string to lowercase
print(course.title()) #this will convert the first character of each word to uppercase
name = "         Wahid"
print(name.strip()) #this will remove the leading whitespace from the string
# to find the index of a character in a string we can use the find() function
index = course.find("p")
print(index) #this will return the index of the first occurrence of the character in the string 
#replace() function is used to replace a character in a string with another character
new_course = course.replace("p", "P")   
print(new_course) #this will print the string with the replaced character
print("python" in course) #this will return True if the string is present in the string, otherwise it will return False