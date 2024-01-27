# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define  C = Character("Cupid", color="#ff0000")
define  N = Character("Nena", color = "#b7007d")
default opponent = "Opponent"
default backdrop = "bg classroom"
default opponent_pic = "nena"


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

    scene bg keanu uchiha

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show cupid neutral

    # These display lines of dialogue.

    C "You know what I always wondered..."

  

    C "What is the purpose of living?"

    show cupid neutral at a_middle_to_right

    menu :
        C "What is the purpose of living?"
        "Public Breastfeeding!":
            jump choice1_BF

        "To support horny chicken dating sim!":
            jump choice1_HC

    label choice1_BF :
        $ menu_flag = True
        show cupid neutral at a_right_to_middle
    
        C "The German Parliament forbid me to participate on public Breastfeeding, due to my War Crimes on brazillian Bicycle drivers..."
        C "Who the fuck would obey the german law anyway?!"
        C "I have been committing Tax Fraud since you were in you dads milkballs!"
        jump choice1_done
    
    label choice1_HC :
        $ menu_flag = False
        show cupid neutral at a_right_to_middle
        
        C "I saw a horny propose to his boyfriend by laying an egg as a marriage gift."
        C "His way of replying to the proposal was to crack the egg on his boyfriends asshole and beat it until it was scrambled."
        C "What a wonderfull world we live in!"

        jump choice1_done

    label choice1_done :

    scene bg classroom
    with Dissolve(3.0)

    show nena
    with dissolve

    N "Geez, what an odd dream that was."

    
    label play_pong:

        window hide
        $ quick_menu = False

        call screen pong(opponent = "Cupid", backdrop = "bg classroom", opponent_pic = "cupid neutral")

        $ quick_menu = True
        window show

        show nena

        if _return == opponent:
            N "I win!"

        else:
            N "Ahh, well done. You got me all beat."


    # This ends the game.

    return
