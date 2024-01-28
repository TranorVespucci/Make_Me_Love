label scene_randall:

window hide
$ quick_menu = False

scene street dark
with Dissolve(3.0)

$ renpy.pause()

$ quick_menu = True
window show

Narrator "I step outside of the building, trying to take a deep breath and clear my head, as I step out onto the pavement."
Narrator "For some reason the night doesn’t grat me that pleasure- maybe it’s because I’m not alone yet. I’m still standing next to the smokers on their breaks."
Narrator "They laugh and play around drunkenly, daring each other to do a certain trick shot with an empty can."
Narrator "Not exactly the picture of peace."
Narrator "I walk a bit along the street, away from the direct proximity of the “AMOUR”."
Narrator "Breathing gets a bit easier as I step in front of the nearby Pizza Parlor and let myself settle down by the curb."
Narrator "I rub my eyes and let the day sink in. I’m glad it’s over soon, I need to be alone for just a minute, just an hour without weird romance magic-"

mystery_randall "Leyla?!"

Narrator "You have got to be kidding me."
Narrator "It takes me a moment to blink through my dizziness to recognize him, in the dim lighting of neon lights and malfunctioning street lanterns."

show i_randall pizza neutral

Narrator "It’s Randall."
Narrator "He looks way more exhausted, wiping away sweat from his forehead- "
Narrator "Oh, the biggest change by far obviously is the small matter of him no longer being in a postal, but pizza delivery uniform… after today that doesn’t faze me anymore."
Narrator "The moment I turn around and he recognizes me, his face lights up."

show i_randall pizza laughing

randall "Oh my god, it is you!"

show i_randall pizza blushing

Narrator "I can’t help but flinch and look around me as he says that, but I think I’m in the clear- I don’t see any signs of a god hanging around."
Narrator "Randall stares at me with an ever softening expression"
Narrator "his bag nearly dropping from his shoulder as he accidentally forgets that gravity exists and he bends his shoulders down in relaxation."
Narrator "I can’t help but chuckle."

Me "Yes, it is me- I can’t believe you work here too!"

Narrator "He looks at me quizzically, a soft smile on his lips."

randall "Yes, I have a few jobs- or do you mean “too” as in, you work around here aswell?"

Me "Both actually- I work at Amor- crazy that I’ve not seen you around before!"

Narrator "He nods at what I say but looks impatiently toward the door of the pizza place."

randall "That’s insane! Yea I’m pretty new, I recently lost my job at a corner store downtown so I needed something new-"
randall "sorry, listen, I have to go and clock out real quick- are you still here in 10 minutes?"

Narrator "I laugh and playfully tap my own watch."

Me "Make that 5 and you’ll have a deal- Time is money!"

show i_randall pizza blushing

Narrator "He nods enthusiastically and runs quickly, somehow without falling, into the parlor."

hide i_randall pizza blushing

Narrator "I have a moment to breathe and think."
Narrator "What if Cupid only brought these people to me?"
Narrator "What if this isn’t fake… Maybe, when Dawn is over. I’ll still want this, and they will want me."
Narrator "Who would I want to still like me the most though? "
Narrator "As I ponder this, I hear steps behind me already and the sound of items falling down, as someone stumbles into something."
Narrator "I hear the sound of Randall cursing at something. This man is ridiculous."

# Pong Gameplay Starts!
    
window hide
$ quick_menu = False

call screen pong(opponent = "Randall", backdrop = "street dark", opponent_pic = "randall pizza neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

$ quick_menu = True
window show

if _return == opponent:
    Narrator "I can barely stifle my laughter as the sounds of something crashing down and tearing something else down with it has a sort of domino effect."
    Narrator "I hear more cursing and frustrated grunts, though they are stifled by the corridor."
    Narrator "I like him."
else:
        Narrator "It does have a slight charm, being clumsy. But… I’m not attracted to the idea of having to help someone out at all times either?"

Narrator "It takes a few moments but finally, he emerges."

show i_randall normal neutral

Narrator "Fuck."
Narrator "He has really nice hair."
Narrator "I was hoping it would be really weird and really throw me off."
Narrator "It does not."

show i_randall normal laughing

randall "I hope I did alright? Did I do it all in time?"
Narrator "I put on a quizzical, pondering look as I circle him playfully."

show i_randall normal neutral

randall "He stands in place, playfully whipping his head around to follow my movements."
Me "Hmmm… not the best performance I’ve see- however… You get bonus points for being cute, so I guess, you’ll get away with it… This time."

show i_randall normal blushing 

Narrator "Randall grins warmly at me, and although he still bears the strains of the day on his face, he looks almost alive again, his entire face bearing the way he feels about me- "

randall "I… I’m honoured, truly!"

Narrator "He wears his heart on his sleeve."
Narrator "I stop walking in circles and lean against the pizza parlour's wall."

Me "I do have to go back soon though, my apologies."

show i_randall normal neutral

Narrator "Randall squints his eyes for a moment, that careful, delicate look wandering over me again."
Narrator "I love when he does that- it’s simply the way I feel with him. Not exciting or dangerous just… like a sigh of relief."
Narrator "Suddenly, he grins to himself, and his face falls to a neutral expression- The way it does not out of apathy or disinterest, but when he’s pursuing a focus."
Narrator "He moves up slowly toward me, leaning on the wall next to me, shoulder by shoulder, staring up at the sky."

randall "Can I draw you some time?"

Narrator "I look up at him. His glasses reflect the light of the road, and behind him, I see the glimmer of the night sky."
Narrator "It’s a very starry night. Clearer than I think I’ve ever seen it in the city."
Narrator "His eyes find mine."

Me "You draw?"

randall "I try."

Me "And you want to draw me?"

Narrator "I can’t look away. I felt the warmth of his body next to mine."

show i_randall normal blushing

randall "Yes."

Narrator "I want him to inch closer, to move forward but- he seems perfectly content just… looking at me. He drinks in every moment like it’s the force that keeps him alive."
Narrator "I want it to be."

show i_randall normal neutral

Narrator "And that’s when a bus drives by us, and by the panic and realization in Randall's eyes, I assume it’s his."

randall "Oh my God, I’m so sorry, I have to run, like, I have to go right this second, right now!"

Me "Yes I understand, go, go go!"

Narrator "He hesitates and his expression is filled with panicked regret as he decides to grab his bearings and start running."

randall "I WORK THERE!"

show i_randall normal laughing

Narrator "He shouts, pointing at the parlor behind me as he books it to the bus. I can see the drivers disapproving scowl in the review mirror."

Me "I KNOW, GO!"

Narrator "He nods, shaking his head and laughing at his own words… and just like that, he gets into the bus."

show i_randall normal blushing 

Narrator "I’m still waving him as he stumbles in the bus, almost falling when the driver begins moving just before he sits down-"

show i_randall normal blushing at left:

show i_cupid mischievous:
    xalign 0.7 yalign 1.0
with moveinright

Narrator " when I see, standing by the bus stop an all too familiar face."

return