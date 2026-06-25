# in basic we use loops to repeat a block of code multiple times. In python we have two types of loops: for loop and while loop.
for num in range(5):
    print(num)
for message in ["Hello", "World", "Python"]:
    print(message)
for i in range(5):
    for j in range(3):
        print(f"i: {i}, j: {j}")

successful = True
for attempt in range(3):
    if successful:
        print("Successful")
        break
for x in range(5):
    if x % 2 == 0:
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
for a in range(5):
    for b in range(3):
        print(f"a: {a}, b: {b}")
# the concept of nested loops is that we have a loop inside another loop. The inner loop will run completely for each iteration of the outer loop. In this example, for each value of a from 0 to 4, the inner loop will run 3 times, printing the current values of a and b.
print(type(5))
print(type (range(5)))

number = 100
while number > 0:
    print(number)
    number //= 2  # This is equivalent to number = number // 2, which divides the number by 2 and updates it.
    command = ""
    while command != "quit":
        command = input("Enter a command: ")
        print("ECHO", command)
        break  # This break statement will exit the inner while loop after the first iteration, regardless of the input. If you want to allow multiple commands until "quit" is entered, you should remove this break statement.
    # concept of infinite loop is that the loop will continue to run indefinitely until a certain condition is met. In this case, the inner while loop will keep asking for a command until the user types "quit".
    while True:
        command = input("Enter a command: ")
        if command == "quit":
            break
        print("ECHO", command)

for i in range(1,10):
    if i % 2 == 0:
        continue  # This will skip the rest of the loop body for odd numbers and move to the next iteration.
    print(i)