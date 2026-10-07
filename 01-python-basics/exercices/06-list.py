### AUFGABE 1
languages = ["Python", "Java", "C++", "JavaScript", "Go"]

erstes_element = languages[0]
letztes_element = languages[-1]
drittes_element = languages[2]

print(erstes_element)
print(letztes_element)
print(drittes_element)

### AUFGABE 2
languages = ["Python", "Java", "C++"]

languages.append("Go")
languages.remove("Java")
languages.insert(1, "JavaScript")
print(languages)

### AUFGABE 3
languages = ["Python", "Java", "C++", "JavaScript", "Go"]
languages.remove("Java")
languages.pop()
print(languages)

### AUFGABE 4
numbers = [12, 5, 8, 21, 30, 17, 44, 9]
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

### AUFGABE 5
languages = ["Python", "Java", "C++", "JavaScript"]
for index, language in enumerate(languages):
    print(f"{index}:", language)


### AUFGABE 6
numbers = [10, 20, 30, 40, 50, 60, 70, 80]
first_three = numbers[0:3]
last_three = numbers[-3:]

print(first_three)
print(last_three)

### AUFGABE 7 
original = ["Python", "Java", "C++"]
original_copy = original.copy()

original_copy[1] = "JavaScript"

print(original)
print(original_copy)

### AUFGABE 8 
users = [
    {"name": "Erik", "active": True},
    {"name": "Anna", "active": False},
    {"name": "Max", "active": True},
    {"name": "Lisa", "active": True},
]
active_users = []
for user in users: 
    if user["active"]:
        active_users.append(user)

print(active_users)

### AUFGABE 9
numbers = [12, 5, 8, 21, 30, 17, 44, 9]
even_numbers = [number for number in numbers if number %2 == 0]
print(even_numbers)

### AUFGABE 10
products = [
    {"name": "Laptop", "price": 999, "stock": 5},
    {"name": "Mouse", "price": 29, "stock": 0},
    {"name": "Keyboard", "price": 79, "stock": 12},
    {"name": "Monitor", "price": 299, "stock": 3},
    {"name": "USB Cable", "price": 9, "stock": 0},
]

available_products = [ product for product in products if product["stock"] > 0]
product_names = []
for product in available_products:
    product_names.append(product["name"])

print(available_products)
print(product_names)

### QUIERO VOLVER A SENTIR, A CUANDO NO TENIA QUE FINJIR, YO, QUIERO VOLVER A SER YO 