# For loops

languages = ["Python", "Java", "JavaScript"]

for language in languages:
    print(language)

# range

for i in range(5):
    print(i)

# range(start, stop, step)

for i in range(2,10,2):
    print(i)

# while wiederholt code solange eine Bedingung True ist:

counter = 0

while counter < 5:
    print(counter)
    counter += 1

# break: Beendet die schleige

for number in range(10):
    if number == 5:
        break
    print(number)

# continue: Überspringt die aktuelle Iteration

for number in range(10):
    if number == 2:
        continue
    print(number)