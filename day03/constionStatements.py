# Condition Statements

# if statement

a = 20
if a > 10:
    print(f"{a} is greater than 10")

# if else statement

age = int(input("Enter your age: "))

if age > 17:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# if elif else statement

marks = int(input("Enter your marks: "))

if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("F")

# nested if statement

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Negative")

# shorthand if statement

num = 10
if num > 0: print("Positive")

# shorthand if else statement

num = 10
print("Positive") if num > 0 else print("Negative")
