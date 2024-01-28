label scene_cynthia_closing:

    window hide
    $ quick_menu = False

    scene bar bright
    with fade

    $ renpy.pause()

    $ quick_menu = True
    window show

    Narrator "The next few hours moved by quickly. "
    Narrator "Two people threw up outside of the toilets, a few people found their match for the night or got their hearts broken, but overall, a pretty normal night.  "
    Narrator "Apart from when had a bachelorette party incident wherein the bride of honour was revealed to have had an affair with the bride-to-be’s fiancé, so we had to kick them out before our property got damaged. "
    Narrator "It was a lot of love drama, more than normal and I can’t help but believe I know who’s responsible. "
    Narrator "The weirdest moment so far, however, is now- "
    Narrator "Cause now I’m standing behind the bar and the night has reached its midpoint. "
    Narrator "...She walks in. "

    show i_cynthia neutral

    Narrator "She doesn’t see me at first. "
    Narrator "She comes in, wearing the same things she wore at her coffee break. "
    Narrator "She looks tired, but not too tired for a last drink to process whatever happened at that last meeting of hers. "
    Narrator "Her hair isn’t as perfectly in place as it had been earlier, loose strands find their way into the air and her corset sits a little lop-sided. Her make-up is smudged, and her left earring keeps getting caught on itself. "
    Narrator "She looks even more beautiful than I remember. "
    Narrator "I enjoy watching her and hold my breath, hoping the moment lasts a little longer, till she sees me. "
    Narrator "There’s something so ethereal about her, as she acts purely without the bias of my presence.  "
    Narrator "It’s wonderful to see her politely apologize to guests as she wants to walk past them, as she fixes her hairpins back into place, rolls back down her collar and wipes away fallen mascara under her eyes. "
    Narrator "She’s not serene, that’s not the right word- she still holds herself high, walks with purpose and assesses everything around her critically. "
    Narrator "No, the serenity only sets in when she sees me. "

    show i_cynthia mischievous

    Narrator "And after the first initial expression of surprise, a sly smile creeps into her face. "
    Narrator "I can’t help but smile as well- though it was wonderful to see her act without my bias, the way she looks at me makes me feel- "
    Narrator "No. "
    Narrator "This is getting crazy"
    Narrator "This is too many people, too much, too many feelings and none of them are even real. Amazing. "
    Narrator "Before I have time to make up my mind over if I should now indulge on tonight’s feelings or not, she is in front of the bar. "
    Narrator "She slides onto a stool and props up her face on her hands. "

    show i_cynthia laughing

    cynthia "Fancy seeing you here- I see this is where you had to hurry off to."

    show i_cynthia mischievous

    Narrator "I can’t help myself- I copy her pose and playfully lean my chin on my hands opposite her, way too proud of myself as that inspires a spark in her expression, eyes sharply tracking their target, grin widened. "

    Me "Yes, as you can see Mrs. “It may be 8 pm, but I have another meeting scheduled for today”, I also have important business to attend to..."

    Narrator "She tilts her head, playfully biting her lip and slowing moving her steer from my lifts to my eyes and back again. "

    cynthia "Oh yea? And what could possibly be that important?"

    Narrator "Riding this absolute power trip and feeling way more confident with a bar between her and I, both due to proximity, as well as this being home turf, I lean forward teasingly, slowly, toward her face, inching. "

    show i_cynthia blushing

    Narrator "She stays in place, but I see her grin fall as that rewarding blush reveals itself on her cheeks. I see her let out a shaky breath to calm herself, her attention glued to me, awaiting my next move. "
    Narrator "I lean past her face toward her ear and whisper. "

    Me "Asking you for your order."

    Narrator "I jump up and playfully gesture to the wall behind me, stacked to the top with liquor."

    Me "I’m a Bartender, I’m here to fulfil your desires."

    Narrator "Cynthia props herself back up and crosses her arms, laughing off the tension of the previous moment, even, to my pride, clearing her throat. "

    show i_cynthia laughing

    cynthia "Does the desire have to be… liquor related?"

    Narrator "I nod with a playful sadness and continue waving my hands elaborately in front of the bottles, doing my best salesman impression.  "
    Narrator "Cynthia laughs off her sight disappointment but grins playfully. "

    show i_cynthia mischievous

    cynthia "Too bad- well, then, an expresso martini please… I feel like choosing coffee has been pretty successful today, why stop now-"

    Narrator "She laughs to herself like she’s pondering whether to say something or not. "

    show i_cynthia blushing

    cynthia "So- serve me please, Leyla."

    window hide
    $ quick_menu = False

    call screen pong(opponent = "Cynthia", backdrop = "bar bright", opponent_pic = "cynthia neutral")

    $ quick_menu = True
    window show

    if _return == opponent:
        $ cynthia_stats += 1

        Narrator "I have to laugh at that- it’s very on the nose, but her boldness is both amusing and… Well…"
        Narrator "Ok, yea, it’s hot. "

        show i_cynthia mischievous

        cynthia "Go on then will you, quit staring, I’m thirsty!"

        Narrator "I notice that I might have let my stare linger on her for a bit too long but… It’s very difficult to tear myself away from her. "

        Me "Okok, You’ve got it boss!"


    else:
        Narrator "I chuckle, but more out of politeness and less because I find it funny… "
        Narrator "I think she can sense that it wasn’t genuine because she gets a bit quieter but doesn’t slump together out of insecurity. "
        Narrator "She’s funny that way- she can get shy, but out of vulnerability I feel and less out of an awkwardness with herself… She’s… yea. I don’t know. She intrigues me. "

    
    Me "One expresso martini, coming right up!"

    Narrator "I wink at her and am about to turn around to actually MAKE the drink at this point, when I turn around and see- "

    show zayn neutral:
        xalign 0.3 yalign 1.0
    with moveinleft
        
    show i_cynthia mischievous:
        xalign 0.5 yalign 1.0
        linear 0.5 xalign 0.75

    $ renpy.pause()

    hide zayn neutral
    hide cynthia mischievous

    show i_zayn neutral:
        xalign 0.3 yalign 1.0
    show i_cynthia mischievous:
        xalign 0.75 yalign 1.0

    zayn "Still working, little one?"

    Narrator "I’m holding bottles in my hands. "
    Narrator "The grin that slowly falls from my face was put there in the first place by Cynthia. "

    show i_cynthia neutral:
        xalign 0.75 yalign 1.0

    Narrator "This. This is awkward. "
    Narrator "Cynthia sits up straighter, not insecure by herself but sensing my shift in mood. "
    Narrator "Zayn crosses his arms and projects casualness as he leans back his head and raises his arms to stretch his neck.  "
    Narrator "Which isn’t attractive to me at all, that leaves me completely unaffected. Help. "

    cynthia "..."

    Narrator "Amazing. Now we have an awkward silence. Great.  "
    Narrator "I’m being dramatic, it luckily doesn’t go on for long, it’s just a beat in time, but it’s still bad. I can’t believe I didn’t see him come back; I hope he wasn’t there long… "

    zayn "…Well I’m only asking because I don’t think you’ve taken your break yet so- go and I’ll make the customer her drink."

    show i_cynthia mischievous:
        xalign 0.75 yalign 1.0

    cynthia "Cynthia snorts, prompting Zayn to look at her sharply, and then look back at me with an expression that is the definition of disapproval. "

    Me "Ah yes, I probably should do that then-"

    Narrator "Before I have a chance to further figure out who to say what to, say goodbye or promise to call or not call Cynthia, Zayn jumps to action. "
    Narrator "He calmly but forcefully takes the bottles from of my hands, pushes me out from behind the bar, and steers me in the direction of the door.  "
    Narrator "Within seconds I am a good distance away from Cynthia and Zayn rushes back toward the bar. "
    Narrator "I can’t even begin to process the usual feelings that would be accompanied by feeling him grip me that way, of how close we are as he pushes me away, or what it is to see how seemingly intimidated he is by Cynthia- "

    show i_cynthia laughing:
        xalign 0.75

    Narrator "I’m too distracted by Cynthia stealthily turning around to me as Zayn takes my place at the bar.  "
    Narrator "She mouths “Call me” and winks at me, before quickly turning around and playing patient yet entitled customer again, the moment Zayn looks back up.  "
    Narrator "I need to get out of here. "

    jump scene_randall

