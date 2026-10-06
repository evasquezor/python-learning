### Aufgabe 1

def calculate_total (price, cuantity):
    return price * cuantity

### Aufgabe 2

def isEven (number):
    if number %2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is not even ")

isEven(11)


### Aufgabe 3

def is_valid_user(age:int, active:bool):
    if age > 18 and active:
        print("USer is valid")
    else:
        print("User sit not valid")

### Aufgabe 4
def calculate_average(numbers):
    total_sum = 0
    for number in numbers:
        total_sum += number
    average =  total_sum / len(numbers)

    print(f"The average is: {average}")

calculate_average([10, 20, 30, 40, 50])

### Aufgabe 5
products = [
    {"name": "Laptop", "price": 999, "stock": 5},
    {"name": "Mouse", "price": 29, "stock": 0},
    {"name": "Keyboard", "price": 79, "stock": 12},
    {"name": "Monitor", "price": 299, "stock": 3},
]

def get_available_products(products):
    count = 0
    total_items_in_stock = 0
    inventory_value = 0
    for product in products:
        if product["stock"] > 0:
            count += 1
            total_items_in_stock += product["stock"]
            

    print(f"Availabkle products {count}")
    print(f"Total items in stock {total_items_in_stock}")
    

get_available_products(products)

###Aufgabe 6
def calculate_inventory_value(products):
    inventory_value = 0
    for product in products:
            if product["stock"] > 0:
                inventory_value += product["stock"] * product["price"]
    print(f"invetory_value {inventory_value}")

calculate_inventory_value(products)

### Aufgabe 7 
def create_user(name, age, role="user"):
    user = [
        {
         "name" : name,
         "age": age,
         "role": role
        }
    ]
    print(user)

create_user("Erik", 24)
create_user("Erik", 24, "Admin")

### AUFGABE 8 
def calculate_sum(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    print(sum)

calculate_sum(5,5,5)

### AUFGABE 9
def create_product(**kwargs):
    return kwargs

product = create_product(name="Laptop", price=999, stock=5)
print(product)

### AUFGABE 10

users = [
    {"name": "Erik", "age": 24, "active": True},
    {"name": "Anna", "age": 17, "active": True},
    {"name": "Max", "age": 32, "active": False},
    {"name": "Lisa", "age": 21, "active": True},
    {"name": "Tom", "age": 15, "active": False},
]
def get_active_adult_users(users):
    active_users = []
    for user in users:
         if user["active"] and user["age"] > 18:
             active_users.append(user)

    return active_users

print(users)

