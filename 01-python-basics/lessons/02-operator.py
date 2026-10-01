# Arithmetische Operatoren 
a = 10
b = 3

a + b  # 13
a - b  # 7
a * b  # 30
a / b  # 3.333
a // b # 3
a % b  # 1
a ** b #1000

# Vergleich Operatoren 
x = 10 

x == 10    # True
x != 10    # False
x > 5      # True
x < 5      # False
x >= 10    # True
x <= 10    # True

x = 10 # Zuweisung
x == 10 # Vergleich 

# Logische Operatoren 
age = 24
has_license = True

age >= 18 and has_license # Beide müssen True sein 
age >= 18 or has_license # Mindestens einer Bedingugn muss true sien 

not has_license # kehrt den Boolean um 

# Membership Operatoren
languages = ["Python", "Java", "JavaScript"]

"Python" in languages
"C++" in languages

# Identity: is vs ==

a == b  # Fragt: Haben a und b denselben Wert?
a is b  # Fragt: Sind a und b dasselbe Objekt?   