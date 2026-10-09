def ageinmonths(age):
    return age * 12


def ageinweeks(age):
    return age * 52


def ageindays(age):
    return age * 365.24


def ageinhours(age):
    return age * 8765.76


def ageinminutes(age):
    return age * 525949.2


age = int(input("what is your age?"))
months = ageinmonths(age)
print("your age in months is", months)
weeks = ageinweeks(age)
print("your age in weeks is", weeks)
days = ageindays(age)
print("your age in days is", days)
min = ageinminutes(age)
print("your age in minutes is", min)
