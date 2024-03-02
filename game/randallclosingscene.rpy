label scene_randall:

stop music

window hide
$ quick_menu = False

scene street dark
with Dissolve(3.0)

play music "dialogue_song.mp3" loop

$ renpy.pause()

$ quick_menu = True
window show

Narrator "I step outside of the building, trying to take a deep breath and clear my head, finding my way onto the winding pavement."
Narrator "For some reason the night doesn’t grant me the pleasure of a peacfeful mind."
Narrator "Perhaps I need to be alone for that."
Narrator "Though I've found my way outside, the air isn't clear yet."
Narrator "My usual break-spot is on the curb infront of the bar, just a short distance away from where the customers like to take their smoke breaks."
Narrator "Their fumes fill my lungs, scratching my airways, the bitter stench of cigarrettes weaving thickly past me."
Narrator "The smokers laugh and play around drunkenly, daring each other to do a certain trick shot with an empty can."
Narrator "Some try with clumbsy vigor to get it right, getting frustrated at the others when they dismiss the arbitrairy rules and just kick the can around lazyly."
Narrator "Not exactly the picture of peace."
Narrator "So, I decide take a lingering walk further along the street, away from the direct proximity of the “AMOUR” and it's riviting visitors."
Narrator "Breathing gets a bit easier as I build my distance toward all of it, and as I step in front of the nearby Pizza Parlor I, let myself settle down at it's curb."
Narrator "The faint smell of herbs, flour and burnt tomatoes lingers in the air, for some reason, it makes for a quiet comfort."
Narrator "I rub my eyes and let the day sink in."
Narrator "I’m glad it’s over soon, I need to be alone for just a minute, just an hour without weird romance magic."
Narrtor "Breathe in... And out..."
Narrtor "Peace at last."
Narrator "..."

mystery_randall "Leyla?!"

Narrator "..."
Narrator "You have got to be kidding me."
Narrator "It takes me a moment to blink through my dizziness and recognize the voice, as the dim lighting of neon lights and malfunctioning street lanterns blind and distort my vision."

show i_randall pizza neutral

Narrator "It’s Randall."
Narrator "He looks way more exhausted than earlier today, wiping away beads of sweat from his forehead- "
Narrator "Oh, the biggest change however, obviously, is the small matter of him no longer being in a postal uniform."
Narrator "Of course he works at the pizzaria on this exact street."
Narrator "I mean, why wouldn't he?"
Narrator "After the day I've had, this doesn't faze me anymore."
Narrator "The moment I turn around and he recognizes me, his face lights up."

show i_randall pizza laughing

Narrator "Even though I'm tired of this whole bet and all I wanted was to be alone- seeing him light up at the sight of me eases me a bit."
Narrator "None of them are in on it, I think."
Narrator "And I can't help but feel a bit better about the world as his sight washes over me with earnest sweetness."
Narrator "Oh Randall... Somehow I feel like he's the only one who's company could calm me down right now."

randall "OH MY GOD, it IS you!!!"

show i_randall pizza blushing

Narrator "I can’t help but flinch and look around with haste as he says those words, but I think I’m in the clear-" 
Narrator "I don’t see any signs of a god hanging around, ready to complicate my day again."
Narrator "For now."
Narrator "Randall stares at me with an ever softening expression."
Narrator "His bag is nearly dropping from his shoulder as he forgets that gravity exists and lets his shoulders fall in relaxation."
Narrator "I can’t help but chuckle as he rushes to catch it at the last second, just barely avoiding a repeat of previous events."

Me "Yes, it IS me- I can’t believe you work here too!"

Narrator "He looks at me quizzically, a soft smile growing steadily."

randall "Yes, I have a few jobs- Or do you mean “too” as in that you work around here aswell?"

Narrator "I shake my head to try and focus, trying to trough of the dizziness that still hasn't quite let go."
Narrator "No matter how I shift my position, I cannot see him properly."
Narrator "The way he is standing in relation toward me and the lights illuminating the street around us, makes me unable to fully focus on his features."
Narrator "The lights behind him render him a glowing shilouette with only gimpses of sudden illumination"
Narrator "As he shifts on his feet nervously, the light lands on him differently, letting me view him for mere moments with a sudden, momentary sharpness."
Narrator "It's quite captivating, and I am lost for a moment in just... Watching."
Narrator "Waiting patiently for glimpses of his tired eyes, filled with an elemental gleam of joy."

Me "Both actually- I work at the “Amor” down the street!"
Me "It's crazy thactually, that we've never run into eachother before."

Narrator "As I begin to speak again, his genuinly happy expression starts to fade a bit."
Narrator "At first I grow sligthly confused. Are my words irrational or did I say soething wrong?"
Narrator "After a moment I notice, however, that his expression rather compares to that of someone growing uneasy in impatience, rather than being unamused with a situation."
Narrator "Phew."

randall "Insane that you work around here!" 
randall "It makes sense that we've never- Run into echother- though."
randall "I’m pretty new! Recently lost my job at a corner store downtown, so I'm glad I got this gig at such short notice-"

Narrator "Whist he speaks he tries to look at me, but keeps steearing nervously toward the door of the pizza place instead."

randall "Sorry, listen, I have to go and clock out real quick- Are you still going to be here in 10 minutes?"

Narrator "I laugh and playfully tap my own watch."

Me "Make that 5 and you’ll have yourself a deal."

show i_randall pizza blushing

Narrator "He nods enthusiastically and runs quickly, somehow, without falling, into the parlor."

hide i_randall pizza blushing

Narrator "Fondely I watch him, as he stumbles inside, hidded by the door swingin shut behind him with a creaking “thunk”."
Narrator "Finally, I have a moment to breathe and think."
Narrator "What if Cupid only brought these people to me but didn't... Magic them into liking me?"
Narrator "What if this isn’t fake?" 
Narratoe "Maybe, when dawn is over I’ll still want this, they will still want this."
Narrator "I like all of them... But who do I really want to still like me tomorrow?"
Narrator "As I ponder this, possibilities and roundabouts mulling over and over in my mind, something catches my attention."
Narrator "Within the parlor, behind me, there are at first simple steps of someone approaching-"
Narrtor "Then there is the sound of items falling down rapidly in sucession, tearing down further items on their way down, everything culminating in thunderous rattles and bangs-"
Narrator "Then, the unmistakeable sound of someone stumbleling into said created mess-"
Narrator "And finally, I hear the sound of Randall cursing something sharply under his breath, as further objects rattle in echoing collision."
Narrator  "Metal hits tiled flooring, something spins and spins uncontrollably, till it finally twindles it's momentum and collapses in a piercing shiek."
narrator "Further cursing ensues, as the figure beyond the door hastely tydies up the inconvenient mess."
Narrator "This man is ridiculous."

# Pong Gameplay Starts!
    
window hide
$ quick_menu = False

stop music

play music "pong_song.mp3" loop

call screen pong(opponent = "Randall", backdrop = "street dark", opponent_pic = "randall pizza neutral") with Fade(0.5, 1.0, 0.5, color = '#fff')

stop music

play music "dialogue_song.mp3" loop

$ quick_menu = True
window show

if _return == opponent:
    
    $ randall_stats += 1

    Narrator "I can barely stifle my laughter as the attempted clearing seems to cause further unrest."
    Narrator "Sounds of more things crashing down follow- I'm honestly suprised theres still enough objects left standing to be torn down dramatically in that place."
    Narrator "More cursing and crustrated grunts follow, though they are stifled by the corridor."
    Narrator "I like him."
else:

    $ pong_games_won += 1

    Narrator "It does have a slight charm, being clumsy. But… I’m not attracted to the idea of having to help someone out at all time either?"

Narrator "It takes a few moments but finally, he emerges in, for the first time, what I assume is his every-day attire."

show i_randall normal neutral

Narrator "Fuck."
Narrator "He has really nice hair."
Narrator "I was hoping his style would be weird or something and really throw me off."
Narrator "It does not."

show i_randall normal laughing

randall "Sorry about that- I hope I did alright? Did I get back in time?"
Narrator "I put on a quizzical, pondering look as I stand up and circle him thoughtfully."

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

show i_randall normal blushing at left

show i_cupid mischievous:
    xalign 0.7 yalign 1.0
with moveinright

Narrator " when I see, standing by the bus stop, an all too familiar face."

jump scene_over_randall_closing