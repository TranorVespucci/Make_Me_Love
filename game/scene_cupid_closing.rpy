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

    scene bar bright with Fade(0.5, 1.0, 0.5, color = '#ffffff')

    devs "Hey guys, Gorgeous Gorgeous Görlies here! We made this project withing 3 days at the Global Game Jam, and unfortunately were not able to *quite finish this scene and thereby the little ending scene we want you to have- it’s still in the works! "
    devs "Come back in a couple of days to see if we have the finished version uploaded on itch.io! Thank you soo much for playing, hope to see you soon <3"

    return

