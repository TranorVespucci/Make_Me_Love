# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define  C = Character("Cupid", color="#ffffff")
define  N = Character("Nena", color = "#b7007d")
define  Z = Character("Zayn", color = "#ffffff")
default opponent = "Opponent"
default backdrop = "bg classroom"
default opponent_pic = "nena"
default zayn_stats = 0
default randall_stats = 0
default cynthia_stats = 0


#Defining animations here

transform a_middle_to_right:
    xalign 0.5 yalign 1.0
    linear 1.0 xalign 1.2

transform a_right_to_middle:
    xalign 1.2 yalign 1.0
    linear 1.0 xalign 0.5


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cupid mischievous

    # These display lines of dialogue.

    C "We'll meet again in a week."

    C "If you've fallen in love by then, you have to admit that I was right and know more about the ways of love."

    show cupid neutral

    C "If that's not the case, too bad for you, but you've proved to the god of love that he too is not done with learning."

    C "And of course, you can claim that you have won against a god."

    show screen loveStatButton

    label play_pong:

        window hide
        $ quick_menu = False

        call screen pong(opponent = "Cupid", backdrop = "bg classroom", opponent_pic = "cupid neutral")

        $ quick_menu = True
        window show

        show cupid neutral

        if _return == opponent:
            C "I win!"

        else:
            C "Ahh, well done. You got me all beat."


    # This ends the game.

    return
