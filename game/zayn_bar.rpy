label scene_zayn_bar:
    
    stop music

    window hide
    $ quick_menu = False

    scene bar bright
    with fade

    play music "bar_song.mp3" loop

    $ renpy.pause()

    $ quick_menu = True
    window show

    Narrator "Whilst walking, I manage to sort out my thoughts again."
    Narrator "I have to say that Cupid doesn't make things easy for me."
    Narrator "When we arrive at the club, Zayn is assigned to help in the warehouse while I prepare the bar. That gives me a little time to myself."
    Narrator "So I welcome the mindless work, which gives my head a little peace for a short while."
    Narrator "The hours pass. The club opens and the droning curtain of my workplace seems to slowly close around me."
    Narrator "The madness of my everyday life sets in, people order drinks, and ask for advice, to which I give half-qualified answers and the rest try to flirt with me."
    Narrator "Behind these half-hearted chat-up lines, however, I can't see the handwriting of my winged opponent and I find it easy to brush them all off."
    Narrator "Zayn joins me shortly after the club opens and supports me."
    Narrator "Now and then he steals customers from me or snatches bottles I am about to use from under my nose, but to my surprise, I enjoy our games more than they annoy me."
    Narrator "Not least, because I can get back at him from time to time with similar actions."
    Narrator "Finally, Betty appears."

    show i_becky neutral

    Me "Hello girl! I am so happy you’re here."

    Narrator "I grin at her and start making her favourite drink as she sits down at the counter."

    becky "Well you didn´t leave me much of a choice. You just hung up!"

    Narrator "I hand her the drink and almost collide with Zayn as I turn around to get her a straw. "

    becky "You! That friend you brought yesterday. Why did you just watch me make a fool of myself and not warn me?!"

    show zayn neutral:
        xalign 0.3 yalign 1.0
    with moveinleft
        
    show i_becky neutral:
        xalign 0.5 yalign 1.0
        linear 0.5 xalign 0.75

    zayn "Nice to see you too Becky. "
    zayn "I have the feeling that women would rather accuse me than greet me in a friendly way."
    zayn "I have absolutely no idea what you're talking about. You and Dane seemed to be having a lovely time together yesterday."

    becky "Yes, we had that. I'm glad you noticed."
    becky "But it would have been very kind of you to tell me that he has a girlfriend if you saw that I was obviously flirting with him."

    Narrator "Becky and I both bore Zayn with half accusatory half expectant looks. Zayn raises his arms in a defensive stance and stands completely unaware."

    hide zayn neutral

    show i_zayn neutral:
        xalign 0.3 yalign 1.0
    
    zayn "I have no clue what you are talking about. Dane is single."

    hide i_zayn neutral

    show i_zayn laughing:
        xalign 0.3 yalign 1.0
    

    zayn "I mean, yes, I'm a bit of a tease sometimes, but I wouldn't let you flirt with my best mate if he had a girlfriend."

    hide i_zayn laughing

    show i_zayn neutral:
        xalign 0.3 yalign 1.0

    Narrator "Beckie's confusion is well visible and I myself can´t read any dishonesty out of is face."
    Narrator "...Then Becky completely brakes down."

    becky "But his pictures. There was this girl. All over them. Why is everything so complicated?!"

    hide i_zayn neutral
    show i_zayn laughing:
        xalign 0.3 yalign 1.0

    zayn "Oh you mean his sister. Yeah, he recently posted a lot of photos with her because she moved in with him."

    Narrator "The disbelieve is written in both our faces." 
    Narrator "All of this just because becky couldn´t differentiate between a brother, sister and boyfriend, girlfriend dynamic?"
    Narrator "I exhale in frustration and then turn to Becky."

    Me "Well this is good news. Nothing changed. You two had a great time and I think there is a big chance he might like you back."

    becky "What if not? I don´t know how to engage in this. I am so nervous."

    Narrator "This girl really needs to relax. I look at Zayn expectingly."

    hide i_zayn laughing
    show i_zayn neutral:
        xalign 0.3 yalign 1.0  

    zayn "I don’t know if he likes you or not. That was yesterday. I hadn´t have time to talk to him."

    Narrator "I roll my eyes in frustration."

    Me "Ugh, are you good for anything?"

    hide i_zayn neutral
    show i_zayn mischievous:
        xalign 0.3 yalign 1.0 

    zayn "More than you would imagine."

    hide i_zayn mischievous
    show i_zayn neutral:
        xalign 0.3 yalign 1.0  

    zayn "He winks at me and then turns to Becky."

    zayn "If he doesn´t make a move, just ask him to dance with you."

    becky "But how?"

    zayn "You two are absolutely hopeless. Watch and learn."

    hide i_zayn neutral
    show i_zayn mischievous:
        xalign 0.3 yalign 1.0 

    zayn "He casually leans against the counter and smiles at me in a soft, heart-melting way. Not fair, damn Cupid."

    zayn "Next time let me hit on you and not the car."

    Narrator "We all burst out laughing. That was definitely not what I was expecting."

    Me "Oh that was so horrible."

    hide i_zayn mischievous
    show i_zayn laughing:
        xalign 0.3 yalign 1.0  

    zayn "But I made you laugh."
    
    hide i_zayn laughing
    show i_zayn neutral:
        xalign 0.3 yalign 1.0  


    zayn "No, but seriously, relax. Tonight is a couple-night. Slow dances and a lot of romantic interactions."

    zayn "Just let things happen."

    Narrator "Meanwhile, Dane appears behind Becky. She nearly falls off her chair as he starts speaking."

    Dane "Hey guys. Becky, do you want to dance?"

    Narrator "Completely paralysed she slowly takes his hand and walks away with him."
    Narrator "I slam my face in disbelief and silently curse everything possible. Zayn appears next to me."

    hide i_zayn neutral
    hide i_becky neutral
    show i_zayn laughing:
        xalign 0.3 yalign 1.0
        linear 0.5 xalign 0.5  

    zayn "See. Most of the time it`s that easy. You're just overthinking everything."

    Me "Oh shut up and stop being so happy that you were right!"

    show i_zayn blushing

    zayn "A warm smile appeared on his face again. He offered me his hand in invitation for a dance."

    Narrator "I grin. Sightly tempted to take his hand anyway."

    Me "Not a chance hot boy. It's really not that easy."

    show i_zayn mischievous

    Narrator "He leans downward, just as he did earlier so I can feel his warmth radiating into my skin and starts whispering. "

    zayn "You know that you own me. "

    Me "Stop that. You …"

    zayn "What? Make you nervous? Your cheeks are giving you away little one."

    window hide
    $ quick_menu = False

    stop music

    play music "pong_song.mp3" loop

    call screen pong(opponent = "Zayn", backdrop = "bar bright", opponent_pic = "zayn neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

    $ quick_menu = True
    window show

    stop music

    if _return == opponent: #loose

        $ zayn_stats += 1

        if zayn_stats >= 2:
            show zayn_silhouette_lover
            with fade

            pause

            play sound "heartbeat_sfx.wav"

            show zayn_silhouette_lover:
                truecenter
                zoom 1.0
                ease 0.5 zoom 1.2
                ease 0.5 zoom 1.0
        else:
            play music "bar_song.mp3" loop

        Narrator "I open my mouth, but nothing comes out of it."

        if zayn_stats >= 2:
            play sound "heartbeat_sfx.wav"

            show zayn_silhouette_lover:
                truecenter
                zoom 1.0
                ease 0.5 zoom 1.2
                ease 0.5 zoom 1.0

        Narrator "Not sure if frustrated over his win or weak from his gaze I turn down my eyes and try to slow my heartbeat."

        if zayn_stats >= 2:
            play sound "heartbeat_sfx.wav"

            show zayn_silhouette_lover:
                truecenter
                zoom 1.0
                ease 0.5 zoom 1.2
                ease 0.5 zoom 1.0

        Narrator "He gently grabs my chin and tilts it upwards so that I have to look at him."

        if zayn_stats >= 2:
            play sound "heartbeat_sfx.wav"

            show zayn_lover
            with dissolve

        zayn "Look it's not that complicated."

        hide zayn_lover
        hide zayn_silhouette_lover
        with fade

        play music "dialogue_song.mp3" loop

        show i_zayn blushing

        Narrator "To my relief, I detect the reddish tone of blush on his cheeks as well. I think we both lost this game."

        Narrator "I take his hand and let myself completely fall into his grip."

        Narrator "He rests his hand on the lower part of my back and we start to drift through the smoothing vial of the vibrating music."

        Narrator "A man on the other side of the counter clears his throat pointing at his empty glass."

        show i_zayn neutral

        Narrator "Zayn signs in disappointment but he steps back a bit holding my hand up to his mouth."

        show i_zayn blushing

        zayn "It was a pleasure little one."

        Narrator "He gently kisses my hand just before he lets me go and turns to the customer leaving me standing there in total confusion."


    else:
        play music "bar_song.mp3" loop

        $ pong_games_won += 1

        Me "Don't be so sure of yourself. It's just really warm inside here. Fine."

        show i_zayn mischievous

        Narrator "I take his hand and he pulls me closer, which doesn´t help neutralising the reddish tint of my face. My voice fails at my next words."

        Me "Just so you know. Its no win, when you had to use your favour so I would dance with you."

        zayn "Yeah, and I see you're resisting so hard."

        Narrator "His sarcastic undertone annoys but I can´t help but let myself fall into his grip."

        

    
    jump scene_over_zayn_bar









