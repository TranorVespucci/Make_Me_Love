label scene_Zayn_Car:

window hide
$ quick_menu = False

scene street dark
with Dissolve(3.0)

play music "dialogue_song.mp3" loop

$ renpy.pause()

$ quick_menu = True
window show

Narrator "The world passes me by in ever-darkening tones. The last rays of sunlight transform the tall buildings to my sides into brushstrokes of fiery colours"
Narrator "The smooth tones of the golden hour turn as I continue my walk into the blinding, buzzing lights of the city nightlife."
Narrator "I've always felt a little disorientated in this light show, but the combination with my already confused mind adds to the feeling."
Narrator "I wander alongside my normal path as I step casually onto to crosswalk."
Narrator "The next seconds happen faster than my mind can possess them. There was not a chance I could have reacted in time."
Narrator "Lights flash before my eyes."
Narrator "A loud honk bursts my ears and I hear the squeal of car tyres."
Narrator "This is officially my end. Thanks, Cupid that you made me so confused that I got myself killed."
Narrator "Just as I thought it's over a strong arm wraps around my waist tearing me from the street moments before the car dashes past me."
Narrator "I am in shock."
Narrator "My body refuses to react to the commands my mind is sending. Even though I feel pain my body stays in place."
Narrator "But there is something else besides the shock that keeps me in place."
Narrator "A steady rise and fall of the soft surface on which I had landed and the steel cage of arms that embraced me."
Narrator "I transform into a bright red headlight and immediately gain back control over my body. I shoot up."
Narrator "As get hold of myself and take a glance at my saviour my jaw drops in disbelief."

Me "Zayn!?"

Narrator "Unlike me, his get-up was not so light-hearted."
Narrator "Although he tries to hide it, I notice his slightly distorted face and the way he rubbs his back."
Narrator "I feel kind of guilty for not helping him up immediately. He exhales sharply."
Narrator "I blush and turn down my eyes."

show i_zayn neutral
with dissolve

zayn "Well that’s me. A simple “thank you for saving me” would be enough. Are you alright?"

Me "ehm. Yeah of course thanks."

zayn "And what the hell were you doing on the streets? Can´t you just open your eyes when you walk?"
zayn "I am not always there to get you out of trouble."

Narrator "The shame was instantly replaced by anger. He had the audacity to act as if I needed him."

Me "Don´t be such a prick about it. Nobody forced you to help me."
Me "Next time you are more than welcome to watch and let me die."

show i_zayn blushing

zayn "And have to cover all your shifts. No thanks."

show i_zayn mischievous

zayn "You owe me one now. But I´ll keep that favour for later."

Narrator "Why did he always have to be such an asshole? He has a talent for making me furious."
Narrator "How could Becky fall for one of his friends?  "
Narrator "I breathe in and out and try to regulate my anger. I am better than that."
Narrator "I won't let him provoke me. I give him one better."

Me "As if. I think that I have to put up with you every day is compensation enough."

Narrator "I wink at him mischievously and turn around. Leaving him alone gives me a sense of achievement that I really enjoyed."
Narrator "As if he would let me have this success."

hide i_zayn mischievous

Narrator "Just as I turn and am about to leave him standing there, I feel his breath tingling over my neck as he bends down to me."

zayn "You know, it's not particularly nice to just turn your back on your saviour like that sweety."

Narrator "Although his words seem perfectly normal, the tone of his whisper eliminate any confidence I had had a few seconds ago."
Narrator "I mean He is right but out of shame or something else the red headlight costume somehow reappears."

show i_zayn laughing

zayn "I am just playing with you, sweetie."
zayn "Come let's get you to work. I´ll chase away the pigeons for you if they turn out to eat human flesh. "

# Pong Gameplay Starts!
    
window hide
$ quick_menu = False

stop music

play music "pong_song.mp3" loop

call screen pong(opponent = "Zayn", backdrop = "street dark", opponent_pic = "zayn neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

$ quick_menu = True
window show

stop music

play music "dialogue_song.mp3" loop

show i_zayn neutral

if _return == opponent: #loose

    $ zayn_stats += 1

    Me "Thank you for your selfless sacrifice."
    Me "You are certainly a tastier dessert than I am. So I can just walk away relaxed."

    show i_zayn mischievous

    zayn "It's interesting to see that you think I'm so irresistible."
    zayn "And just for the record, I am convinced that you are a very delicious dessert."

    show i_zayn laughing
        
    zayn "I couldn't hide my reaction to his words, so he started laughing out loud."
    zayn "It was a beautiful sound. I wasn't sure when I had last heard him laugh."
    zayn "Maybe there was something good about the whole bet with Cupid after all."

    show i_zayn neutral

    zayn "Come on little one. We'll be late."


# if the Player wins
else:
   
    Me "And I would laugh as they spit out your meat again because you are inedible.
    So not much help. Thanks for the offer, but unfortunately I have to decline."

    show i_zayn mischievous

    zayn "I don't think you can know for sure if I'm inedible if you don't try it yourself."
    zayn "But joking aside."
    zayn "You realise that we have the same workplace. Should I walk in the other direction or how did you imagine that little one?"

    Narrator "He managed to completely wipe my mind."
    Narrator "I nodded briefly and started walking in any direction, regardless of whether it was the right one."

stop music fadeout 1.0

jump scene_over_zayn_car

