def add(q, e):
    return q + e
def subtract(q, e):
    return q - e
def multiply(q, e):
    return q * e
def divide(q, e):
    return q / e

print("please enter you option")
print("a. add")
print("s. subtract")
print("m. multiply")
print("d. divide")

choice = input("please enter your choice")

q = int(input("enter the first num"))
e = int(input("enter the second num"))

if choice == "a":
    print(add (q, e))
elif choice == "s":
    print(subtract (q, e))
elif choice == "m":
    print(multiply (q, e))
elif choice == "d":
    print(divide (q, e))
else:
    print("invalid input")
