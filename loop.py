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