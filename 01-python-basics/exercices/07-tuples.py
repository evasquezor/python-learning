# Tuples erstellen
numbers = (10,20,30,40)
print(numbers[0])
print(numbers[0:2])

# WICHTIG tuples sind immutable das heisst man kann den werten innerhalb einer tuplle nciht verändern 

# Listen benutzt man wenn man Daten verändern will 
# Tuppel ist eher für feste Daten geeignet

# Tuple Unpacking
 
point = (10, 20)
x, y = point

print(x)
print(y)

# Unpacking mit *
numbers = (1,2,3,4,5)
first, *middle, last = numbers

print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5

# *middle bedeutet: mPack alle übrige werten in middle
# funktioniert auch mit Listen 
numbers = [1, 2, 3, 4, 5]

first, *rest = numbers

print(first)  # 1
print(rest)   # [2, 3, 4, 5]

# Tuples aus Funktionen zurückgeben

def get_user():
    return "Erik",24

result = get_user()
print(result)

name, age = get_user()

print(age)
print(name)

# Tuple und Liste umwandeln
numbers = [1,2,3]
numbers_tuple = tuple(numbers)
print(numbers_tuple)

numbers = (1, 2, 3)

numbers_list = list(numbers)

print(numbers_list)
# [1, 2, 3]