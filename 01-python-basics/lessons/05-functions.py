def calculate_price (price, cuantity):
    return price * cuantity

total = calculate_price(23, 2)
print(total)

### Default parameters

def greet(name, languague="de"):
    if languague == "de":
        return f"hello {name}"
    else:
        return f"Hallo {name}"

### Type Hintes
def calculate_price (price : float, quantity:int) -> float:
    return price * quantity

#   price -> float
#   quantyyt -> int
#   return -> float

### *args und *kwargs

def calculate_sum(*numbers): # Hiermit kann man beliebige werte beim aufruf der funktion mitgeben 
    total = 0

    for number in numbers:
        total += number

    return total

print(calculate_sum(10, 20))
print(calculate_sum(10, 20, 30, 40,50))

def print_user(**user):
    print(user)

print_user(name="Erik", age=24, active=True)