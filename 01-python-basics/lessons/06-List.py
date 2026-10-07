### List
languages = ["Python", "Java", "C++"]

print(languages[0])
print(languages[2])
print(languages[-1])

## Elemte verändern

languages[1] = "javascript"
print(languages)

##Elemente Hinzufügen

languages.append("Go") # Am ende
languages.insert(1, "Rust") # An einer bestimmte position hier : 1

##Elemente entfernen
languages.remove("Java") #Nach wert
languages.pop(0) #Nach index
languages.clear() #Liste komplett leeren 

##Läbge
len(languages)

###Über listen iterieren
for language in languages:
    print(language)

for index, language in enumerate(languages):
    print(index, language)


### Slicing
numbers = [0,1,2,3,4,5]
print(numbers[1:4])

### Listen kopieren

numbers = [1, 2, 3]

copy = numbers.copy()

print(copy)

### List comprehension

numbers = [1, 2, 3, 4, 5]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)


even_numbers = [number for number in numbers if number % 2 == 0] ## Besser

# [expression for item in iterable if condition]