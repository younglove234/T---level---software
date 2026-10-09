def generate_name(b, a):
    return b + " " + a


print("welcome to the superhero name generator!")

user_adjective = input("Enter an adjective (descibing word):")
user_animal = input("Enter your favourite species of animal: ")

superhero_name = generate_name(user_adjective, user_animal)
print("your super hero is called: ", superhero_name)
