def add(a,b):
    ans = a + b
    print(ans)
def sub(a,b):
    ans = a - b
    print(ans)
def mul(a,b):
    ans = a * b
    print(ans)
def div(a,b):
    ans = a/b
    print(ans)
a = int(input("Enter your first number "))
while a == "":
    try:
        a = int(input("Enter a number "))
    except ValueError:
        a = int(input("Must enter a number "))
b = int(input("Enter another number "))
while b == "":
    try:
        b = int(input("Enter a number "))
    except ValueError:
        b = int(input("Must enter a number"))
opp = int(input("What would you like to do with these numbers:\n"
"1. Addition\n"
"2. Subtraction\n"
"3. Multiplication\n"
"4. Division\n"
"Just enter the number "))
while opp < 1 and opp > 4:
    opp = int(input("Must enter a number from the operations "))
if opp == 1:
    add(a,b)
elif opp == 2:
    order = int(input(f"1. {a}-{b} or 2. {b}-{a}? "))
    if order == 1:
        sub(a,b)
    elif order == 2:
        sub(b,a)
    elif order > 2 and order < 1:
        order = int(input("Enter a number from the order list "))
elif opp == 3:
    mul(a,b)
elif opp == 4:
    order = int(input(f"1. {a}/{b} or 2. {b}/{a}? "))
    if order == 1:
        div(a,b)
    elif order == 2:
        div(b,a)
    elif order > 2 and order < 1:
        order = int(input("Enter a number from the order list "))