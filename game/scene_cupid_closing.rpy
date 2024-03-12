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

    Narrator "Cupid just stands there, pulling up one eyebrow as I recognize him, giving me a playful little wave-"
    Narrator "What a bastard."
    Narrator "It’s at this moment that I notice that the street has cleared."
    Narrator "Cars are rare in this street at this time of day anyway, but I'm used to the lulling chatter and rambles of drunkern smokers and bouncers in the night."
    Narrator "A little bit too silent for my taste, even if I did wish for some peace and quiet."
    Narrator "But I don't quite regret that wish."
    Narrator "I settle into the quiet slowly but surely, my muscles untensing, my jaw unclenching."
    Narrator "All night I've been slightly on edge, wondering of the influence of Cupid upon me and my surroundings."
    Narrator "Now we play fair."
    Narrator "He's out in the open, his face bared."
    Narrator "No more random coffee stalls, heart shaped pebbles, whispers of romantic dramas, weird coincidences and washed out tropes-"
    Narrator "We both know what's going on, I can relax and face someone that knows it all, if not more than I."
    Narrator "Cupid winks at me playfully, and I don't try to hold back the rolling of my eyes-"
    Narrator "We're alone in this road, him and I."
    Narrator "It’s just me and the god of love under the starlight."
    Narrator "His eyes sharp, his grin wide, his handywork laid out in front of him."
    Narrator "He must have been watching me all day at this point."
    Narrator "I hate how proud of himself he looks, letting me just run into his layed out traps and tricks all evening."
    Narrator "Though I must admit, he's played a good game." 
    Narrator "I won't admit that to his face just yet though."
    Narrator "That wicked grin on him is really straining my nerves."

    Me "Enjoying the show now, are we?"

    Narrator "I shout, half-jokingly, half-seriously annoyed."

    show i_cupid laughing

    Narrator "This seems to be the punch line of some kind of joke to him, errupting into laughter as he starts walking my way."

    cupid "Oh Leyla, of course I did! You made it so very, very entertaining."

    Narrator "Cupid teases as he comes to a halt and... lays down on the floor, in the middle of the street."

    show i_cupid mischievous

    Narrator "He raises his hand to make a gesture, lazily beckoning me to join him at his side."
    Narrator "And so I do."
    Narrator "Uncertain of his plans but curiousity getting the best of me, I walk toward him."
    Narrator "He has propped up one leg, layed his head on crossed arms, his eyes closed, his face at peace."
    Narrator "Looks like he's relaxing on vacation on a sandy beach somewhere, not precareously placed on the middle of the road."
    Narrator "Roolking my eyes I decide after a few moments to join him, lying down at his side."
    Narrator "And so... there we lie. Under the weirdly clear sky..."
    Narrator "For the first time in the entire day I am not overwhelmed, I am not scared or confused or worried-"
    Narrator "I just am."

    cupid "So?"

    Narrator "He doesn't change his demeanor and I grow tired of the day, so I just copy in his stead and fold my arms on my chest."
    Narrator "Closing my eyes I let out a heavy yawn, trying to make my head lay comfortably on the smooth but heard tar beneath it."

    Me "So... what?"

    show i_cupid laughing

    cupid "Soooo? Did you enjoy the evening?"
    cupid "I'd rather hope so, I tried my very best to put on a good show."

    Me "For your own amusement, you mean?"

    show i_cupid neutral

    Narrator "Cupid hisses at my words."
    Narrator "I don't bother to open my eyes and see how genuine his display of hurt is."

    cupid "Come now, don't treat me so unjust!"
    cupid "The entire evening's soirée was ALL catered toward yourself and YOUR amusement, darling."
    cupid "Tsk, to think of the lenghts I went to, to make it such a perfect, personalized endavour in your very honour!"

    Me "Hah, how very thoughtful of you-"

    cupid "-Yes, I personally would descibe such actions as VERY thoughtful indeed!"

    Narrator "The God shifts beside me, I can hear him gesturing wildely as he speaks."
    Narrator "Kind of amusing really, that I can get such a rise out of him-"
    Narrator "The meek, mere mortal being that I am."













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


    if _return == opponent or pong_games_won < 7:

        show i_cupid neutral

        Me "...Hilarious."

        cupid "...Hm?"

        Narrator "I cannot contain myself anymore, I fall into a fit of laughter."
        Narrator "I writhe on the floor, convulsing in spasms of laughter, unable to breathe until I lay there exhausted and with the ghost of a smile on my face."
        Narrator "My muscles ache."

        cupid "..."
        cupid "Have you calmed down now?"
        Narrator "I let out one last, painful chuckle."

        Me "... yes."

        Narrator "Cupid nods to himself and starts smirking as he sees an opportunity in his words."

        show i_cupid mischievous

        cupid "Good girl."

        show i_cupid neutral

        cupid "So, you also understand that what happens next, Is up to you?"

        Narrator "He turns to look at me as he says this. His eyes reflect the stars more than they should. "
        Narrator "They glimmer and flicker within, an entire solar system within his gaze. "
        Narrator "He’s beautiful."
        Narrator "And I know that no matter how enchanting he is, he is the only one that I cannot choose."
        Narrator "Nor do I want to... someone else has caught my eye."

        Me "Yes. Yes I do... I’ll see to it tomorrow."

        cupid "One last thing please..."

        Me "...Hm?"

        Narrator "He looks at me expectantly, increasinly playfully offended as I do not act in the way I am supposed to-"
        Narrator "Oh."
        Narrator "Ah, yes. Ugh"

        Me  "I hereby admit that I was wrong about the ways of love."
        Me "... Is that fine?"

        Narrator "Cupid folds his arms behind his head and gazes proudly into the sky."

        cupid "Hmm yes, yes I suppose that should do."

        Narrator "We lie there for a moment."

        cupid "Good luck, Leyla."

        Narrator "I chuckle to myself, not wanting to quite thank him- his ego is too large, it’s a public safety hazard to do so."

        Me "Fuck off, Cupid."

        hide i_cupid neutral
        with dissolve

        Narrator "I trail off in my laughter as I look to my side and..."
        Narrator "He is gone."
        Narrator "It is just me, the weirdly clear night sky, and the choice of that comes next..."

        Me "...Fuck."
        Me "I think my break is over."

        show bar dark
        with Fade(2, 1, 1)

        if zayn_stats < randall_stats > cynthia_stats:
            show i_randall normal blushing
            "The person Leyla feels most drawn to after the nights events is Randall!"
            hide i_randall normal blushing

            "Before her lies a beautiful journey at the side of this person, as they truly get to know one another and figure out the rest of their lives..."

        elif randall_stats < cynthia_stats > zayn_stats:
            show i_cynthia normal blushing
            "The person Leyla feels most drawn to after the nights events is Cynthia!"
            hide i_cynthia normal blushing

            "Before her lies a beautiful journey at the side of this person, as they truly get to know one another and figure out the rest of their lives..."

        elif randall_stats < zayn_stats > cynthia_stats:
            show i_zayn normal blushing
            "The person Leyla feels most drawn to after the nights events is Zayn!"
            hide i_zayn normal blushing

            "Before her lies a beautiful journey at the side of this person, as they truly get to know one another and figure out the rest of their lives..."


        else:
            "The people Leyla feels most drawn to after the night's events are..."

            if (randall_stats >= cynthia_stats) and (randall_stats >= zayn_stats) or (randall_stats >= 2) :
                show i_randall normal blushing
                "Randall."
                hide i_randall normal blushing

            if (cynthia_stats >= randall_stats) and (cynthia_stats >= zayn_stats) or (cynthia_stats >= 2):
                show i_cynthia blushing
                "Cynthia."
                hide i_cynthia blushing

            if (zayn_stats >= randall_stats) and (zayn_stats >= cynthia_stats) or (zayn_stats >= 2):
                show i_zayn blushing
                "Zayn"
                hide i_zayn blushing

            "Before her lies a beautiful journey in which she tries to figure out what she truly wants... Or who. But, the time to decide remains to be kept for another day."

        

    else:

        Me "... Pathetic."

        show i_cupid neutral

        Narrator "Cupid whips his head around to me immediately, genuinely shocked at my words."

        cupid "EXCUSE me?"

        Narrator "I turn to look at him."
        Narrator "His eyes reflect the stars more than they should. They glimmer and flicker within, an entire solar system within his gaze."
        Narrator "He's beautiful."
        Narrator "I liked the others, sure."
        Narrator "But it’s him I've been longing to see again, all evening."
        Narrator "I didn’t notice it at first, not until this very moment."
        Narrator "But the one time i haven’t worried, the one time I have felt truly, truly at easy and my mind stood still was..."
        Narrator "...now"
        Narrator "He looks at me quizzically."
        Narrator "He can truly not figure out what is happening right now."
        Narrator "He expected... Something else. He is well and truly surprised and doesn’t understand what I am up to."
        Narrator "I have bessted a God."

        Me "Cupid, why did you make that bet with me?"

        Narrator "He looks confused to the point of distress; he sits up and lets his hands run through his hair, his mind running, his eyes darting."

        cupid "What do you mean I..."
        cupid "You... You challenged me! Yea, I heard you speak ill of me, and I wanted to prove you wrong!"
        cupid "I grin at him, propping myself up on the side."

        Me "You can’t tell me you’re the God of Love and cannot see romance when it scares you in the face."

        Narrator "I stand up and turn away for a moment, letting him figure himself out."
        Narrator "When I turn around again, he is... squinting."
        Narrator "He's still puzzled, but it is more by the nature of the realization he has just made."
        Narrator "He knows."

        Me "You know, normal people just... Ask their crushes on a date, they don’t chicken out and try to make them ACTIVELY unavailable instead?!"

        show i_cupid blushing

        Narrator "As I speak Cupid begins to marvel at me. The realization is sinking in... He finds relief in understanding. Finally."

        Me "I mean really, what were you hoping to achieve? I don’t know what kinda fucked up dating shows you’re responsible for in your free time, but I prefer not to be used as a prop for someone’s romantic entertainment?!"

        Narrator "He starts to stand up, a grin, not playful like before but earnest and amused emerges slowly."

        Me "Like, if you like someone, tell them, that was pretty much the most confusing social experiments of “why not to have Gods roam the earth” ..."

        Narrator "His grin widens and his hands cover his face, a shiny row of teeth almost reflecting the starlight above. "

        Me "...Which come to think of it, makes this less of a dating show and more of a documentar-"

        Narrator "His hands find the side of my face... the small of my back."

        Me "-ry..."

        Narrator "I stare at him, my pulse rising, my vision blurring, my only anchor to this world a waving sky and a man with eyes like starlight."
        Narrator "His hands are warm, and firm and I am breathless as his face is inches from mine."
        Narrator "He smells of vanilla, salt, amber and caramel... sweet, rich and intoxicating."
        Narrator "He's biting his lip and lets out a slow breath that strives over my face like a spring breeze."
        Narrator "I lean forward and my lips slowly connect with his."
        Narrator "He leans in, the both of us kissing tenderly..."
        Narrator "And so we stand there, locked in each other's embrace."
        Narrator "In the middle of the starlight street, on the empty road and with the flickering of broken streetlights and neon signs surrounding us."
        Narrator "Just me and the God of Love."




    jump scene_over_cupid_closing

    return

