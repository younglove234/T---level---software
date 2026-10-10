def game():

    swim_or_wait = input(
        "You come to a lake. Do you either want to wait for a boat, or swim across? (swim/wait): "
    )

    if swim_or_wait == "swim":

        print("you have been eaten by some hungry sharks.  Game over.")

    elif swim_or_wait == "wait":

        print("you have safely arrived at the other side of the lake.")

        cave_or_stay = input(
            "you came accross a cave would you like to go inside or move on? (venture/move on):"
        )

    if cave_or_stay == "venture":

        print(
            "you venture into the cave but the cave colapses, you try to escape by you get crushed by boulders.  Game over."
        )

    elif cave_or_stay == "move on":

        print("You walk away from the cave along a narrow track in the forest.")

        crossroad_turn = input(
            "you have come across 3 different path on is dark, one is bright and one is silver. which way are you going?"
        )

    if crossroad_turn == "dark":

        print(
            "you walk in the into the dark path but soon get lost in the dark and cant seem to find your way"
        )

        sound_distance = input(
            "then you start to hear a sound in the distance will you (follow or stay)"
        )

        if sound_distance == "follow":

            print("you follow the sound and find your way out of the dark")

            master = input(
                "you find a temple and some random old man with white beard ask you to be his disciple(diss him/accept)"
            )

            if master == "diss him":

                print(
                    "old man gets pissed so and screams 'you are courting death' before using his sword to poke you.   Game over."
                )

            elif master == "accept":

                print(
                    "he takes you to his sect and gives you the lengendary sword technique."
                )

        elif sound_distance == "stay":

            print(
                "you continue wondering in the dark and sleep in the dark.   Game over."
            )

    elif crossroad_turn == "bright":

        print("you get teleported into a room ")

        training = input(
            "you find a door but you have to be level 2 to enter(enter/stay)"
        )

        if training == "enter":

            print("you encoounter a massive mutatated dog.   Game over")

        elif training == "stay":

            print("Congratulatin you got the legendary book of magic")

    elif crossroad_turn == "silver":

        print("you walk in and disintigrate into a bueatiful silver.   Game over.")


game()
