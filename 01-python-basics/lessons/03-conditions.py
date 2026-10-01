# Grundprinzip
age = 24

if age >= 18:
    print("Adult")

###

age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")

###

age = 24

if age >= 18:
    print("Adult")
elif age < 65:
    print("Adult")
else:
    print("Senior")

###

age = 24
has_ticket = True
is_vip = False

if age >= 18 and (has_ticket or is_vip):
    print("Entry allowed")
else:
    print("Entry denied")