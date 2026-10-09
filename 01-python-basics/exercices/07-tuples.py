# AUFGABE 1
person = ("Erik", 24, "Software Engineering")

name, age, degree_programm = person
print(age)

# Aufgabe 2
product = ("Laptop", 1299.99, 5)
name, price, stock = product
print(name)
print(price)
print(stock)

#Aufgabe 3
numbers = (10,20,30,40,50)
first, *middle, last = numbers

print(last)
print(middle)
print(first)

#Aufgabe 4
users = {
    "Erik": 24,
    "Anna": 22,
    "Max":  27
}

for name, user in users.items():
    print(f"{name} is {user} years old")

#Aufgabe 5
def get_product():
    return "Keyboard", 99.99, 10

name, price, stock = get_product()

print(name)
print(price)
print(stock)