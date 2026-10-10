def check_age(age):
    if age >= 18:
        print("you are old enough to vote")
    else:
        print("you are not old wnough to vote")


def check_age_a(age):
    if age >= 16:
        print("you are old enough to vote")
    else:
        print("you are not old enough to vote")


user_age = int(input("How old are you? "))
user_country = input("what is your country")

if user_country.lower == "austria":
    check_age_a(user_age)
else:
    check_age(user_age)
