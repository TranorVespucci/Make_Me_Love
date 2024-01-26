# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define  T = Character("Tranor", color="#4700a5")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg keanu uchiha

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show tranor idle

    # These display lines of dialogue.

    T "You know what I always wondered..."

    show tranor sad

    T "What is the purpose of living?"

    show tranor sad:
        xalign 0.95

    menu :
        T "What is the purpose of living?"
        "Public Breastfeeding!":
            jump choice1_BF

        "To support horny chicken dating sim!":
            jump choice1_HC

    label choice1_BF :
        $ menu_flag = True
        show tranor idle:
            xalign 0.5
            yalign 0.99 
    
        T "The German Parliament forbid me to participate on public Breastfeeding, due to my War Crimes on brazillian Bicycle drivers..."
        show tranor angry
        T "Who the fuck would obey the german law anyway?!"
        T "I have been committing Tax Fraud since you were in you dads milkballs!"
        jump choice1_done
    
    label choice1_HC :
        $ menu_flag = False
        show tranor idle:
            xalign 0.5
            yalign 0.99 
        
        T "I saw a horny propose to his boyfriend by laying an egg as a marriage gift."
        T "His way of replying to the proposal was to crack the egg on his boyfriends asshole and beat it until it was scrambled."
        T "What a wonderfull world we live in!"

        jump choice1_done

    label choice1_done :

    # This ends the game.

    return
