# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

default romance_points = 2


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    show screen bars

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    menu:
        "I LOVE YOU UNDEFINED PNG":
            $ romance_points += 1
            jump choice_done

        "I have no strong feelings one way or the other":
            $ romance_points -= 1
            jump choice_done

    label choice_done:

    e "Huh.."

    # This ends the game.

    return
