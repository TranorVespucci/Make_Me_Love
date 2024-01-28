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

#Randall

image i_randall neutral = At('tranor idle', sprite_highlight('randall'))
image i_randall mischievous = At('tranor idle', sprite_highlight('randall'))
image i_randall laughing = At('tranor idle', sprite_highlight('randall'))
image i_randall blushing = At('tranor idle', sprite_highlight('randall'))

#Becky
image i_becky neutral= At('becky silhouette', sprite_highlight('becky'))

#Defining these Characters
define Narrator = Character(callback=name_callback, cb_name=None,)
define Me = Character('Layla', callback=name_callback, cb_name=None, color="#ffffff")
define cupid = Character('Cupid', image='i_cupid', callback=name_callback, cb_name='cupid', color="#ffffff")
define cynthia = Character('Cynthia', image='i_cynthia', callback=name_callback, cb_name='cynthia', color="#ffffff")
define zayn = Character('Zayn', image='i_zayn', callback=name_callback, cb_name='zayn', color="#ffffff")
define becky = Character('Becky', image='i_becky', callback=name_callback, cb_name='becky', color="#ffffff")
define randall = Character('Randall', image = 'tranor idle', callback=name_callback, cb_name='randall', color="#ffffff")

#defining mysterious Cupid
define mystery = Character('???', image='i_cupid', callback=name_callback, cb_name='mystery')
define mystery_randall = Character('???', image='tranor idle', callback=name_callback, cb_name='mystery_randall')



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

    with Dissolve(.5)

    pause .5

    scene street dark:
        alpha 3

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    # These display lines of dialogue.

    Narrator "It is a late summer evening. The molten gold of the last sunrays rests gently on my skin as I feel its soothing warmth."
    Narrator "I stop for a moment and close my eyes. The pungent odour of car fumes mixed with the loud conversation seems to engulf me."
    Narrator "But for that one moment, the sun pulls me out of this all-encompassing cloud and grants me a moment of peace before my stressful workday starts."
    Narrator "Just as I decided to stay here for a lifetime I get thrown out of this perfect moment by an annoying vibration deep down in my back pocket."
    Narrator "I pull out my mobile phone and see my best friend's name light up on the screen."
    Me "9 missed calls. Oh shit, something terrible must have happened."

    show i_becky neutral

    Me "Becky is everything alright?"

    becky "No ..."
    Narrator "After a long pause while she is catching her breath she continues."
    becky "Life is so unfair. Nobody loves me."

    Narrator "I inhale deeply"

    Me "Come on girl you know you are loved by so many people. Me being one of them."
    Me "So what is actually your problem?"

    becky "I know but you know what I mean."

    hide i_becky neutral

    Narrator "While I am on the phone I reach the highway, where masses of people are trying to find their way through the sidewalk jungle."

    show i_becky neutral

    Me "No Becky I do not. Please enlighten me."

    Narrator "I'm just squeezing my way between two shrilly giggling women when Becky continues."

    becky "Remember that guy Zayn brought along at your last shift?"

    Narrator "I nod and realize the next moment that she can't see me at all, whereupon I answer her."

    becky "Well maybe I checked him out on Insta and found him posing with the same girl over and over again."

    becky "HE HAS A GIRLFRIEND!!!!"

    becky "He is so handsome and sooooo nice. I thought we had a thing."

    Me "Don't be sad. Any friend of Zayn can't be good company. You deserve so much more sweety."

    Me "Now get your shit together, throw on the most marvelous dress you have, and come to the club."

    Me "Drinks are on me. Fuck Cupid, we don't need love or men."

    hide i_becky neutral

    Narrator "I don't leave her the opportunity to change her mind and abruptly hang up."

    Narrator "As I'm putting my mobile phone away in my pocket, an angelic voice intrudes my consciousness."

    show i_mystery mischievous

    mystery "I love the energy but don't you think we should get to know each other first, my dear?"

    Narrator "His words wash over me like a wave of butterflies tingling every part of my body."
    Narrator "Rose clouds make me feel lightheaded as I turn around to see the most handsome man I have ever seen in life."
    Narrator "Dressed in shades of pink, red, and white and with hair of the same variation, his image resembles that of an angel."
    Narrator "My breath instantly stops and I can't help but stare."

    Me "Oh my God!"

    mystery "Guilty as charged. Well, not that God, but still one of them. Smart girl."

    Narrator "I close my eyes and shake my head to chase away the dizziness this incredibly gorgeous person created in my head."
    Narrator "I am not sure I want him gone when I open my eyes just to prove my sanity."

    hide i_mystery mischievous
    show i_cupid neutral

    cupid "How rude of me not to introduce myself."
    cupid "I'm Cupid, Amor, or Eros depending on who you ask."
    cupid "I have many names, but in all of them, I am the god of love. At your service my dear."

    Me "I think halfway through my brain completely stopped working cause I could swear that you just said that you were a God."

    show i_cupid mischievous

    cupid "Not just one God. I am the God you declared to not need just moments ago."

    Narrator "Heat rises in my cheeks. Is this man really accusing me of blasphemy against himself?"
    Narrator "I have to get my head clear and set things right."

    Me "For a moment, I was afraid I had said the wrong thing because he didn't answer and just seemed to study me intensely. Then he started to smile."

    show i_cupid laughing

    cupid "Do you know the easiest way to make someone fall in love with you? Make them laugh."

    show i_cupid neutral

    cupid "Because an honest laugh says a lot more about the person's affection for you than most words could."
    cupid "It's nothing that should be complicated or tiring."

    Me "That sounds idealistic don't you think? Unfortunately, life isn't that easy."

    Narrator "A mischievous grin appeared on his face."

    show i_cupid mischievous

    cupid "If you're so certain about it, I'm sure you won't mind if I show you a little sample of my magic."

    show love rahmen
    with Dissolve(.5)

    cupid "Of course, I won't play unfairly. That wouldn't be any fun either."

    Narrator "I don't have time to respond to his offer because the moment he speaks, my body starts tingling all over again."
    Narrator "All the clearing of my mind seems to have been in vain and I let myself fall completely into his lulling warmth."

    hide love rahmen
    with Dissolve(.5)

    hide i_cupid mischievous

    # Pong Gameplay Starts!
    
    window hide
    $ quick_menu = False

    call screen pong(opponent = "Cupid", backdrop = "bar dark", opponent_pic = "cupid neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

    $ quick_menu = True
    window show

    show i_cupid neutral

    if _return == opponent:
    
        Narrator "Heat makes its electrifying way through my body until my cheeks turn red and my heart starts beating wildly."
        Narrator "I smile, unsure how to react to this feeling.\n
                Even though I want to prove him wrong, I have to admit that he is very good at what he is doing."
        Narrator "His smile softens and radiates such a pleasant sense of security that I melt away."

        cupid "Don't be sad my dear. It's no shame to get seduced by the god of love"

        show i_cupid laughing
        with dissolve

        cupid "Well, I have to admit this is not the most realistic scenario to prove your point."
        cupid "So let's make a deal."

        show i_cupid neutral

        cupid "We'll meet again in a week."

        show i_cupid mischievous

        cupid "If you've fallen in love by then, you have to admit that I was right and know more about the ways of love."

        show i_cupid laughing

        cupid "If that's not the case, too bad for you, but you've proved to the god of love that he too is not done with learning."
        cupid "And of course, you can claim that you have won against a god."

        Me "There is something you are not telling me. What's the catch?"

        cupid "Well maybe I'll sprinkle a bit of my magic here and there to make things more interesting,"

        show i_cupid mischievous

        extend " but that won't be a problem for you my dear, right?"

        Narrator "His grip on my mind seems to tighten all at once, because all I want to do is agree with him and make him happy."
        Narrator "It's as if my head is moving and nodding on its own, as if in a trance. The smile he gave me in response made me completely lose touch with reality."

        cupid "Good girl."
        cupid "I'm really looking forward to our little bet. Surprise me."

        show screen loveStatButton


    # if the Player wins
    else:
   
        show i_cupid blushing

        Narrator "His face brightened in a smile that melted my heart."

        cupid "Well it looks like you know more about the techniques of seduction than you wanted to admit before"
        cupid "if you can even beat the god of love in his own game."

        hide i_cupid blushing
        show i_cupid mischievous

        cupid "I can't really let that go."

        hide i_cupid mischievous
        show i_cupid blushing

        cupid "I have to say I'm impressed. You make me want to prove myself."

        hide i_cupid blushing
        show i_cupid mischievous

        cupid "What do you think about a little bet?"

        Narrator "Heat makes its electrified way through my body. It must have something to do with his magic!"

        show screen loveStatButton
        show screen loveStats


    Narrator "that's it for now."

    jump scene_randall_1

    jump scene2

    # show screen loveStatButton


    # This ends the game.

    return
