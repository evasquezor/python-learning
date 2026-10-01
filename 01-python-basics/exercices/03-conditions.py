username = "erik"
password = "python123"

if username == "erik" and password == "python123":
    print("Login succesful")
else:
    print("Invalid credentials")

## Aufgabe 2 Altersprüfung
age = 24

if age < 13:
    print("You are a child")
elif age >= 13 and age <= 17:
    print("You are a Teenager")
elif age >= 18 and age >= 64:
    print("You are a adult")
else:
    print("You are nearly dead")

## Aufgabe 3 Rabatt
age = 24
is_student = True


if age < 18 or is_student or age >= 65:
    print("Discount available")
else:
    print("No discount")

## Aufgabe 4 mache ich nicht da ich es schon kann und sich alles eh wiederholt

## Aufgabe 5 Passwortstärke
password = "Python123!"

if len(password) <= 8 and not password.isalpha() and password.isalnum():
    print("Starkes passwrod")
else:
    print("weak password")

## Aufgabe 6 bussines Logik

age = 24
salary = 3500
has_experience = True
programming_language = "Python"

if age >= 19 and salary >= 3000 and ("Python" in programming_language or "Java" in programming_language) and has_experience:
    print("Application accepted")
else:
    print("Application rejected")