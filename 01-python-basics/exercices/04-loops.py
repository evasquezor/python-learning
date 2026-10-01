# Aufgabe 1 Filtern

numbers = [12, 7, 4, 19, 22, 8, 31, 10]

for number in numbers:
    if number % 2 == 0:
        print(number)

# Aufgabe 2 Summe und Durchscnit
numbers = [10, 20, 30, 40, 50]
count = 0
summe = 0
for number in numbers:
    count += 1
    summe += number

average = summe / count
print(f"Sum : {summe}")
print(f"Count : {count}")
print(f"Average : {average}")

## Aufgabe 3 Users Filtern
users = [
    {"name": "Erik", "age": 24, "active": True},
    {"name": "Anna", "age": 17, "active": True},
    {"name": "Max", "age": 32, "active": False},
    {"name": "Lisa", "age": 21, "active": True},
]
for user in users:
    if user["age"] >= 18 and user["active"]:
        print(user["name"])

## Aufgabe 4 Suche mit break
users = ["Anna", "Max", "Erik", "Lisa", "Tom"]

for user in users:
    if user == "Erik":
        print("User found: Erik")
        break

# Aufgabe 5 continou
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number %3 != 0:
        print(number)
        continue

## Aufgabe 6 Backend Logik
products = [
    {"name": "Laptop", "price": 999, "stock": 5},
    {"name": "Mouse", "price": 29, "stock": 0},
    {"name": "Keyboard", "price": 79, "stock": 12},
    {"name": "Monitor", "price": 299, "stock": 3},
    {"name": "USB Cable", "price": 9, "stock": 0},
]

for product in products:
    if product["stock"] > 0:
        print(f" {(product["name"])} - {(product["price"])} - {(product["stock"])} available")
        continue

## Aufgabe 7 
count = 0
total_items_in_stock = 0
inventory_value = 0
for product in products:
    if product["stock"] > 0:
        count += 1
        total_items_in_stock += product["stock"]
        inventory_value += product["stock"] * product["price"]

print(f"Availabkle products {count}")
print(f"Total items in stock {total_items_in_stock}")
print(f"invetory_value {inventory_value}")

## Aufgabe 8
categories = {
    "backend": ["Python", "Java", "C#"],
    "frontend": ["JavaScript", "TypeScript", "React"],
    "database": ["PostgreSQL", "MySQL"]
}

for name, catagorie in categories.items():
    print(name)
    for eintrag in catagorie:
        print(f"-{eintrag}")
