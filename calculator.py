def addition (a, b):
    return a + b
def substraction (a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

print("Enter two digits:")
a = float(input("First digit: "))
b = float(input("Second digit: "))

print("Choose the operation you want to perform:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1/2/3/4/5): "))

if choice == 1:
    print(a, "+", b, "=", addition(a, b))
elif choice == 2:
    print(a, "-", b, "=", substraction(a, b))
elif choice == 3:
    print(a, "*", b, "=", multiplication(a, b))
elif choice == 4:
    print(a, "/", b, "=", division(a, b))
    print("Exiting thr program...")
else:
    print("Invalid operation")
