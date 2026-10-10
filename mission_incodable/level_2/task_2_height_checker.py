def check_height(height):
    if height < 80:
        print("you have to be 80 cm to use this")
    elif height >= 80 and height < 90:
        print(
            "you are about the same height as a snooker tabbl, which is roughly 80cm tall!"
        )
    elif height >= 90 and height < 100:
        print(
            "you are about the same height as the uk's royal sceptre,which is nearly 92cm tall"
        )
    elif height >= 100 and height < 110:
        print(
            "you are about the same height as an olympic hurdle in the men's high hurdle event, which os 106.7cm tall!"
        )
    elif height >= 110 and height < 120:
        print("you are the same height as a wild turkey, which is roughly 115cm tall!")
    elif height >= 120 and height < 130:
        print(
            "you are the same height as the emperor penguin, which is roughly 120cm tall"
        )
    else:
        print("you are too all bro")


print("welsom to the height checker!")
user_height = int(input("enter the height to the nearest "))

check_height(user_height)
