label scene_cupid_closing:
    stop music

    window hide
    $ quick_menu = False

    scene street dark
    with fade

    $ renpy.pause()

    $ quick_menu = True
    window show

    play music "dialogue_song.mp3" loop

    show i_cupid mischievous

    Narrator "Cupid is standing there, pulling up one eyebrow as I recognize him and giving me a playful little wave-"
    Narrator "What a bastard."
    Narrator "It’s at this moment that I notice that the street has cleared. No more smokers on a break, not even the bouncers of the bars are outside anymore."
    Narrator "It’s just me and the god of love under the starlight, his eyes sharp, his grin wide, his handiwork laid out in front of him."
    Narrator "He must have been watching me all day at this point."

    Me "Enjoying the show now are we?"

    Narrator "I shout, half-jokingly and half-seriously annoyed."

    show i_cupid laughing

    Narrator "This seems to be the punch line of some kind of joke to him, as he starts walking my way."

    cupid "Oh Leyla, of course I did- you made it so very, very entertaining."

    Narrator "Cupid teases as he comes to a halt and laying down on the floor, in the middle of the street."

    show i_cupid mischievous

    Narrator "He raises his hand to make a gesture, lazily beckoning me to join him at his side."
    Narrator "And so I do."
    Narrator "And so... there we lie. Under the weirdly clear sky..."
    Narrator "For the first time of the entire day I am not overwhelmed, I am not scared or confused or worried."
    Narrator "I just am."
    Narrator "Staring into the stars, I can feel it all so clearly now."
    Narrator "My feelings are my own."
    Narrator "Their feelings were their own."

    show i_cupid neutral

    cupid "I assume you understand now?"

    Narrator "I don’t look over at him when he speaks, I close my eyes instead."

    Me "I do."

    cupid "Not even I have power over love, Leyla."
    cupid "I can observe it, I can find those who would feel it for each other and bring them together, but even the Gods can’t control what a Mortal can feel..."
    
    Narrator "He lets out a dramatically tragic sigh."

    cupid "Not even me!"

    show i_cupid laughing

    Narrator "This."
    Narrator "All of this- all day, it was all- "
    Narrator "He never controlled Love; he could only bring us all together through circumstances and... what... fate?"
    Narrator "That's..."

    window hide
    $ quick_menu = False

    stop music

    play music "pong_song.mp3" loop

    call screen pong(opponent = "Cupid", backdrop = "street dark", opponent_pic = "cupid neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

    stop music

    play music "dialogue_song.mp3" loop

    $ quick_menu = True
    window show




    jump scene_over_cupid_closing

    return

