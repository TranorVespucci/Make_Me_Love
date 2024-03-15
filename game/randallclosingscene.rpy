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
Narrator "At first I grow sligthly confused. Are my words irrational or did I say something wrong?"
Narrator "After a moment I notice, however, that his expression rather compares to that of someone growing uneasy in impatience, rather than being unamused with a situation."
Narrator "Phew."

randall "Insane that you work around here!" 
randall "It makes sense that we've never- Run into echother- though."
randall "I’m pretty new! Recently lost my job at a corner store downtown, so I'm glad I got this gig at such short notice-"

Narrator "Whist he speaks he tries to look at me, but keeps steearing nervously toward the door of the pizza place instead."

randall "Sorry, listen, I have to go and clock out real quick- Are you still going to be here in 15 minutes?"

Narrator "I laugh and playfully tap my own watch."

Me "Make that 10 and you’ll have yourself a deal."

Randall "I rush from place to place for a living alright, it's a challenge, but I'm a professional. I'll make sure to put on my best performance!"

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

$ quick_menu = True
window show

if _return == opponent:
    
    $ randall_stats += 1

    if randall_stats >= 2:
        show randall_silhouette_lover
        with fade

        pause

        play sound "heartbeat_sfx.wav"

        show randall_silhouette_lover:
            truecenter
            zoom 1.0
            ease 0.5 zoom 1.2
            ease 0.5 zoom 1.0  
    else:
    play music "dialogue_song.mp3" loop 

    Narrator "I can barely stifle my laughter as the attempted clearing seems to cause further unrest."

    if randall_stats >= 2:
        play sound "heartbeat_sfx.wav"

        show randall_silhouette_lover:
            truecenter
            zoom 1.0
            ease 0.5 zoom 1.2
            ease 0.5 zoom 1.0        

    Narrator "Sounds of more things crashing down follow- I'm honestly suprised theres still enough objects left standing to be torn down dramatically in that place."
    
    if randall_stats >= 2:
        play sound "heartbeat_sfx.wav"

        show zayn_silhouette_lover:
            truecenter
            zoom 1.0
            ease 0.5 zoom 1.2
            ease 0.5 zoom 1.0      

    Narrator "More cursing and crustrated grunts follow, though they are stifled by the corridor."

    if randall_stats >= 2:
        play sound "heartbeat_sfx.wav"

        show randall_lover
        with dissolve


    Narrator "I like him."

    hide randall_silhouette_lover
    hide randall_lover
    with fade

    play music "dialogue_song.mp3" loop

else:
    play music "dialogue_song.mp3" loop

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
Narrator "I've just started my break- I have more than enough time... And I do not intent to rush this."

show i_randall normal neutral

Narrator "He stands in place, playfully whipping his head around to follow my movements, circuling him with steady, tentative strides."

Me "Hmmm… You were quite fast, I'll give you that. You just about managed to make it in time."

Narrator "He raises his eyebrows with a gleaming look of pride."

Me "The impending quick-change was also quite impressive for the time."
Me "I should, however, reduct from your score for the sheer amount of cursing in you're technique..."

Narrator "Randall scrunches up his face in protest at my words, exaggerating his displeasure in a playful manner."

Me "All in all, an adiquate performance, if executed a bit... clumbsily"

show i_randall normal blushing 

Narrator "Hiting at the misshap in the corridor leads to him developing a slightly blush on his face."

Me "However… You get bonus points for being cute, so I guess, full marks from me."

Narrator "Randall grins warmly at me, and although he still bears the strains of the day on his face, he looks almost alive again, his entire face bearing the way he feels about me- "

randall "Lucky, that my critic seems to be in good spirits then! Lucky for me, at least."
randall "Anyway, uhm... I'm glad you like- things enough to give me bonus points."
randall "I'd also give you- Eh- bonus points if I had the chance."

Narrator "He wears his heart on his sleeve."
Narrator "I stop walking in circles and lean against the pizza parlour's wall, one foot propped up against it, my back finding comfort on the rigid, cool surface."

Me "I'm glad to have found you again, Randall."

Narrator "His eyes search mine longingly, as if hes trying to assess if he can truly trust my words."
Narrator "There's a searching in him. The moment he seems to have found what he was lookign for, he sighs in relief."

randall "Me too."
randall "The moment you were out of my sight I noticed that I didn't know where I could find you again or if you even wanted to?"

Narrator "He shakes his head nervously, kicking a loose pebble onto the street."
Narrator "It skipps a few times before coming to a halt."
Narrator "If I squint just a little, I could swear that pebble has the shape of a heart."

randall "I- I don't know, I found it very hard to read you. At the same time you couldn't seem to get away quickly enough but on the other..."

Narrator "He stops himself."

randall "I couldn't quite figure you out."

randall "I like you, Layla and I'd love to get to know you more."
randall "I understand if you're not up for that but I just..."
randall "I needed you to know, you know?"

Narrator "He averts my gaze shy and vulnerable, absent-mindedly, playing with the rim of his left sleeve."

randall "I'm not often this foward, but- uhm- I just felt like I'd regret not telling you."

Narrator "Randall summons his strenghth and looks up at me, searching desperately for my response"

randall "Anyway..." 
randall "I'm glad you're here."

Narrator "Closing my eyes for a moment, I ponder how to respond."
Narrator "He's right of course, about me running away earlier. It hadn't just been because I was late, but also ause I was trying to not indulge on any belief that this could be... good."
Narrator "I like him. I liked him from the moment I saw him."
Narrator "But I was scared. Didn't know what to trust, really... Still not quite sure now."
Narrator "Since then everything has just grown more complicated. I don't quite know what to do-"
Narrator "I don't want him to be hurt. Or Cynthia, or Zayn-"
Narrator "This is so confusing but... I need to figure this out."
Narrator "No matter if their feelings are just smoke and mirrors, there is the chance that this is all real and-"
Narrator "My fears cannot get in my way this time. I need to figure out what I want."
Narrator "And what I want right now is to just-"
Narrator "Breathe. Feel safe. Let the world feel like sense."
Narrator "I open my eyes again, blinking, the neon lights sharp in my vision."
Narrator "A warm smile befalls me as I find Randall in my sight once more."
Narrator "No matter what will become of us-"
Narrator "These are the things he makes me feel."

Me "I'm also glad you're here."
Me "But you're right, I did rush away from you earlier today."
Me "I'm sorry it's just been... A very confusing day. Currently, I find myself in a bit of a tough spot romantically and I- I-"
Me "I'm not quite sure what to do."
Me "You're incredibly charming, Randall."
Me "But now I'm torn between a few people I have met recently and it's all been to much, and I need to sleep on it all a night to figure out what I want, I think."
Me "I would like to get to know you Randall, I would, I just- I'm just so overwhelmed by it all, and I'm so sorry, I hate that I cannot tell you what you want to hear..."

Narrator "The floor fills my vision as I look to it ashamed, afraid as well that this might have scared him away."
Narrator "But that is as close as I can get to telling him the truth at this moment in time."
Narrator "Randall deserves the truth."

show i_randall normal neutral

Narrator "A strong, callused hand cups my chin and pulls it up gently."
Narrator "Afraid his expression might be filled with hurt, anger or dissapointment, I almost squint out of instinct, trying to avoid that fate."
Narrator "But his gentle eyes greet me without malace, without pain."
Narrator "A soft, sweet face welcomes me, the hand lingering for just a moment before he strokes my chin gently, his hand returning to his side."
Narrator "I'm baffeled by the decisiveness of his words, the determination and confidence with which he speaks."

randall "What I want to hear, is anything you say."
randall "Sure, hearing you say you'd like me and that I'd have the smallest chance would be a pleasent addition."

show i_randall normal blushing

randall "So, even in that way, you've just given me everythign I needed."
randall "Please don't stress yourself."

show i_randall normal laughing

randall "We only met today after all, not even spoken for long in total."

show i_randall normal neutral

randall "Life is complicated- Love life espechially!"
randall "There's no pressure from my side- If you want to go on a date sometime, I'd be over the moon. If it works out differently, that's alright aswell."

show i_randall normal blushing

Narrator "The monentum of his comfortable overt-ness seems to be dwindeling a bit now."
Narrator "He falls back slowly into his old patterns of slighty awkwardness and embarrasment, his fingers folding into eachother nervously."

randall "All I know, is that you feel... good." 
randall "Yea, that's awkwardly put, but you get what I mean."

show i_randall normal laughing

Narrator "A snort escapes me, the tension of the intensity and awkwardness of the last few minutes bringing me to my breaking point."
Narrator "After throughing him an apologetic look I lay my head on the wall, exhausted from this rollercoaster of emotions."

Me "I think I do know what you mean!"

show i_randall normal blushing

Me "Thank you, by the way. That was very calming to hear."

Narrator "For a moment we just stand in peace. Letting the last moments sink in, just enyjoying eachothers company."
Narrator "Randall squints his eyes at me."
Narrator "That careful, delicate look wanders over me again."
Narrator "I love when he does that- It simply mirror sthe way I feel about him."
Narrator "Amonst the wilderness of the day he is just… like a sigh of relief."
Narrator "Suddenly, he grins to himself, and his face falls to a neutral expression- The way it does not out of apathy or disinterest, but when he’s pursuing a focus."
Narrator "He moves up slowly toward me, leaning on the wall next to me, shoulder to shoulder, staring up at the sky."

show i_randall normal neutral

randall "Can I draw you some time?"

Narrator "I look up at him. His glasses reflect the light of the road, and behind him, I see the glimmer of the night sky."
Narrator "It’s a very starry night. Clearer than I think I’ve ever seen it in this city."
Narrator "His eyes find mine."

Me "You draw?"

randall "I try."

Me "And you want to draw me?"

Narrator "I can’t look away. I feel the warmth of his body radiating calmly next to mine."

show i_randall normal blushing

randall "Yes."

Narrator "I want him to inch closer, to move forward-"
Narrator "His face is so close to mine. All he would need to do to kiss me is lean down just a little, one short journey."
Narrator "I wish he would."
Narrator "I'm close to just staning on my toes, closing the distance between our lips, putting my hand on the side of his face, our breaths merging into one-" 
Narrator "But I stop myself."
Narrator "I couldn't look at him anymore that way. Espechially as he is now."
Narrator "He seems perfectly content to just… look at me."
Narrator "The same thoughts of our closeness, the possibility within that must be on his mind, I'm sure of it." 
Narrator "But the tension of the possibility seems to already be enough to render him fully in bliss."
Narrator "He drinks in every moment, every feature of my face, every fibre of my being like it’s the very force that keeps him alive."
Narrator "It might just be."
Narrator "I want it to be."

show i_randall normal neutral

Narrator "And that’s when a bus drives by us, and by the panic and realization in Randall's eyes, I assume, it’s a bus he needs."
Narrator "Painfully he rips himself from my side, looking at me with a look, which can what can only be described as- apologetic horror?"

randall "OH MY GOD!"
randall "I’m so sorry, I have to run, like, I have to go right this second, right now!"

Narrator "He looks toward me, then the bus, then his phone, then me again, a creature of dispair and pure adrenaline."
Narrator "Shaking my head at his startledness I gesture toward the now parking bus, widening my eyes to try and convey his next course of action to him as efficiantly as I can."

Me "YES I UNDERSTAND, DON't WORRY JUST- RUN!"
Me "... NOW RANDALL!"

Narrator "He hesitates, his expression is filled with panicked regret as he decides to grab his bearings and start running."
Narrator "Pointing at the parlor behind me as he books it to the bus, he looks back at me and shouts."

randall "I WORK- THERE!"


Narrator "I can see the drivers disapproving scowl in the review mirror."
Narrator "When Randall points, doesn't actually point at the Pizza place but the bakery on the other side of the street, but he means well."

Me "I KNOW!"
Me "GO!"

show i_randall normal laughing

Narrator "He nods, shaking his head and laughing at himself"
Narrator "Finally, he reaches the busstop."

show i_randall normal blushing 

Narrator "Randall stumbles into the bus, almost falling over when the driver begins driving, just before he manages to get to a seat."
Narrator "Thankfully, he cathes himself just in time."
Narrator "He grins widely, still handing on awkwardly to a random metal bannister as he sees me waving him goodbye."
Narrator "I’m still waving him as the buss drives off-"
Narrator "-revealing behind it a person, poised casually against the busstop sign, arms crossed, eyes immedeately finding mine-"

show i_randall normal blushing at left

show i_cupid mischievous:
    xalign 0.7 yalign 1.0
with moveinright

Narrator "-rounded out by an ALL too familiar, mischievious grin..."

jump scene_over_randall_closing