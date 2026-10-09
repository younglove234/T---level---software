print("welcome to the mad libs generator! This project will generate a silly sentence")


def sentence():
    name = input("what is your name?")
    adjective = input("Enter an adjective (describing word):")
    verb = input("Enter a verb:")
    place = input("Enter a place:")
    food = input("Enter a food:")
    vehicle = input("Enter a vehicle:")

    print(
        f"{name} is a very {adjective} person to be around. They love to {verb} in {place}. Their favourite food is {food} which they eat in a {vehicle}"
    )


sentence()
