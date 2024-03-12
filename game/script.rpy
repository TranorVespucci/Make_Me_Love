# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#Cupid
image i_cupid neutral= At('cupid neutral', sprite_highlight('cupid'))
image i_cupid mischievous= At('cupid mischievous', sprite_highlight('cupid'))
image i_cupid laughing= At('cupid laughing', sprite_highlight('cupid'))
image i_cupid blushing= At('cupid blushing', sprite_highlight('cupid'))

#mystery Cupid
image i_mystery mischievous= At('cupid mischievous', sprite_highlight('mystery'))

#mystery randall
image i_mysteryR neutral= At('randall mail normal', sprite_highlight('mystery_randall'))
image i_mysteryR mischievous = At('randall mail mischivous', sprite_highlight('mystery_randall'))
image i_mysteryR laughing = At('randall mail laughing', sprite_highlight('mystery_randall'))
image i_mysteryR blushing = At('randall mail blushing', sprite_highlight('mystery_randall'))

#mystery cynthia
image i_mysteryC neutral= At('cynthia neutral', sprite_highlight('mystery_cynthia'))
image i_mysteryC mischievous = At('cynthia mischievous', sprite_highlight('mystery_cynthia'))
image i_mysteryC laughing = At('cynthia laughing', sprite_highlight('mystery_cynthia'))
image i_mysteryC blushing = At('cynthia blushing', sprite_highlight('mystery_cynthia'))

#Cynthia
image i_cynthia neutral= At('cynthia neutral', sprite_highlight('cynthia'))
image i_cynthia mischievous= At('cynthia mischievous', sprite_highlight('cynthia'))
image i_cynthia laughing= At('cynthia laughing', sprite_highlight('cynthia'))
image i_cynthia blushing= At('cynthia blushing', sprite_highlight('cynthia'))

#Zayn
image i_zayn neutral= At('zayn neutral', sprite_highlight('zayn'))
image i_zayn mischievous= At('zayn mischievous', sprite_highlight('zayn'))
image i_zayn laughing= At('zayn laughing', sprite_highlight('zayn'))
image i_zayn blushing= At('zayn blushing', sprite_highlight('zayn'))

#Randall Mail
image i_randall neutral = At('randall mail normal', sprite_highlight('randall'))
image i_randall mischievous = At('randall mail mischivous', sprite_highlight('randall'))
image i_randall laughing = At('randall mail laughing', sprite_highlight('randall'))
image i_randall blushing = At('randall mail blushing', sprite_highlight('randall'))

#Randall Pizza
image i_randall pizza neutral = At('randall pizza neutral', sprite_highlight('randall'))
image i_randall pizza mischievous = At('randall pizza mischivous', sprite_highlight('randall'))
image i_randall pizza laughing = At('randall pizza laughing', sprite_highlight('randall'))
image i_randall pizza blushing = At('randall pizza blushing', sprite_highlight('randall'))

#Randal Normal
image i_randall normal neutral = At('randall neutral', sprite_highlight('randall'))
image i_randall normal mischievous = At('randall mischivous', sprite_highlight('randall'))
image i_randall normal laughing = At('randall laughing', sprite_highlight('randall'))
image i_randall normal blushing = At('randall blushing', sprite_highlight('randall'))

#Becky
image i_becky neutral= At('becky outline', sprite_highlight('becky'))

#Defining these Characters
define Narrator = Character(callback=name_callback, cb_name=None,)
define Me = Character('Leyla', callback=name_callback, cb_name=None, color="#ffffff")
define cupid = Character('Cupid', image='i_cupid', callback=name_callback, cb_name='cupid', color="#ffffff")
define cynthia = Character('Cynthia', image='i_cynthia', callback=name_callback, cb_name='cynthia', color="#ffffff")
define zayn = Character('Zayn', image='i_zayn', callback=name_callback, cb_name='zayn', color="#ffffff")
define becky = Character('Becky', image='i_becky', callback=name_callback, cb_name='becky', color="#ffffff")
define randall = Character('Randall', image = 'tranor idle', callback=name_callback, cb_name='randall', color="#ffffff")

define Dane = Character('Dane')
define devs = Character('???')

#defining mysterious Cupid
define mystery = Character('???', image='i_cupid', callback=name_callback, cb_name='mystery')

#define mysterious randall
define mystery_randall = Character('???', image='i_mysteryR', callback=name_callback, cb_name='mystery_randall')

#define mysterious cynthia
define mystery_cynthia = Character('???', image='i_mysteryC', callback=name_callback, cb_name='mystery_cynthia')


define met_randall = False
define met_cynthia = False
define met_zayn = False

define pong_games_won = 0


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

    jump scene_opening

    label scene_opening_over:

    jump scene_randall_1

    label scene_over_randall_1:

    jump scene_cynthia_introduction

    label scene_over_cynthia_intro:

    jump scene_Zayn_Car

    label scene_over_zayn_car:

    jump scene_zayn_bar

    label scene_over_zayn_bar:

    jump scene_cynthia_closing

    label scene_over_cynthia_closing:

    jump scene_randall

    label scene_over_randall_closing:

    jump scene_cupid_closing

    label scene_over_cupid_closing:

    scene bar dark
    with Fade(5, 2, 1)

    "Thank you SO MUCH for playing our Game!"
    "We made it over the course of 48h at the Global Game Jam 2024."
    "This project was a lot of fun to make and, if you made it this far, we hope you enjoyed reading and playing with us as much as we enjoyed developing it!"
    "Unfortunately the story ends here for now (whoops, time constraints only let you get so far!!)"
    "Buuuut perhaps, if we get enough requests (dontmakemeloveggj@gmail.com), we'll create more content to round off the game with more elaborate endings ;)"
    
    if pong_games_won < 7:
        "Don’t forget that the Pong-events and deciding whether a joke ended up landing or not had an influence on your ending!" 
        "You unfortunately don’t get any more scenes with the Love Interests, but you might be able to get a different scene with Cupid if you play your cards right..."

    "Please take our gratitude and our love to heart!\n
    Yours, Gorgeous Gorgeous Görlies <3"

    return
