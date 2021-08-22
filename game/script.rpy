# The script of the game goes in this file.

#characters
define mc = DynamicCharacter("mcName", color="#c35e77", outlinecolor="white") #pink https://www.renpy.org/wiki/renpy/doc/cookbook/Who's_that%3F
define lo = DynamicCharacter("loName", color="#2D4C2B", outlinecolor="black")
$ mcName = "You"
$ lo = "???"

#background images
image classroom = "classroomPlaceholder.jpg"
image outside = "skyPlaceholder.jpeg"
image roof = "roofPlaceholder.jpeg"

#character images
init: #https://lemmasoft.renai.us/forums/viewtopic.php?t=9185
    image hui default:
        "huilook.png"
        zoom .35
    image connie default:
     "connielook.png"
     zoom .35

#sign language images
init:
    image sign now:
        "now.png"
        zoom .5
    image sign anyone: #https://www.reddit.com/r/RenPy/comments/iglq6o/playing_gifs_in_renpy/
        zoom .5
        "any1.png"
        0.5
        "any2.png"
        0.5
        "one.png"
        0.5
        repeat
    image sign sit:
        "sit.png"
        zoom  .5
    image sign here:
        "here.png"
        zoom .5
    image sign yesPlease:
        zoom .5
        "yesplease(1).png"
        0.5
        "yesplease(2).png"
        0.5
        repeat
    image sign noThanks:
        zoom .5
        "nothanks(1).png"
        0.5
        "nothanks(2).png"
        0.5
        "nothanks(3).png"
        0.5
        repeat
    image sign pretty:
        "prettyPlaceholder.jpg"
        zoom .5
    image sign both:
        "bothPlaceholder.png"
        zoom .5

#define styles
# style slButton_left_top is image: #https://www.renpy.org/doc/html/style.html
#     xanchor 600 #https://www.renpy.org/doc/html/style_properties.html
#     yanchor 360
# style slButton_right_top is image:
#     xanchor 860
#     yanchor 360
# style slButton_left_bottom is image:
#     xanchor 600
#     yanchor 710
# style slButton_right_bottom is image:
#     xanchor 860
#     yanchor 710

label start: # The game starts here.
    scene classroom
    "You sigh as you walk into the classroom."
    "You never expected you would be attending a nighttime sign language class, but after the car accident that caused you to lose your hearing, you don’t have much of a choice."
    "You look around for empty seats, and settle on a desk in the back of the room."
    "You’re open to meeting new people, but you won’t go out of your way to make friends here. You just want to learn enough to get on with your life."
    "Out of the corner of your eye, you see..."

    #select LO https://www.renpy.org/doc/html/displaying_images.html
    show hui default at left
    show connie default at right

    menu select_lo: #https://www.renpy.org/wiki/renpy/doc/cookbook/Letting_players_choose_their_own_name
        "a girl":
            jump girl
        "a boy":
            jump boy
    label boy:
        scene classroom
        $ gender = "boy" #one line python https://www.renpy.org/doc/html/python.html
        $ pronoun0 ="him"
        $ pronoun0cap = "Him"
        $ pronoun1 ="he"
        $ pronoun1cap = "He"
        $ pronoun2 ="his"
        $ pronoun2cap = "His"
        $ loName = "Hui"

        jump after_select_lo

    label girl:
        scene classroom
        $ gender ="girl"
        $ pronoun0 ="her"
        $ pronoun0cap = "Her"
        $ pronoun1 ="she"
        $ pronoun1cap = "She"
        $ pronoun2 ="her"
        $ pronoun2cap = "Her"
        $ loName = "Connie"

        jump after_select_lo

    label after_select_lo:
        init:
            image loPic default:
                ConditionSwitch(
                "gender == 'girl'", "connielook.png" ,
                "gender == 'boy'", "huilook.png") #https://lemmasoft.renai.us/forums/viewtopic.php?t=23402
                zoom .35
        init:
            image loPic smile:
                ConditionSwitch(
                "gender == 'girl'", "conniesmile.png" ,
                "gender == 'boy'", "huismile.png") #https://lemmasoft.renai.us/forums/viewtopic.php?t=23402
                zoom .35
        init:
            image loPic talk:
                ConditionSwitch(
                "gender == 'girl'", "connietalk.png" ,
                "gender == 'boy'", "huitalk.png") #https://lemmasoft.renai.us/forums/viewtopic.php?t=23402
                zoom .35

    show loPic default at center with dissolve
    "You see a %(gender)s come stand behind the desk beside you. You turn to face %(pronoun0)s."
    show loPic smile
    "%(pronoun1cap)s smiles radiantly down at you, and %(pronoun1)s moves %(pronoun2)s hands in a series of patterns."
    "You pause for a second, confused, before pursing your eyebrows and tilting your head."
    show loPic default
    "Understanding flashes across %(pronoun2)s face, and %(pronoun1)s reaches into %(pronoun2)s bag and grabs %(pronoun2)s phone, opening the notes app."
    "You peer at the screen."
    show loPic talk
    lo "Is this seat taken?"
    show loPic smile
    "You shake your head. The %(gender)s smiles and plonks down at the desk beside you."
    "%(pronoun1cap)s turns back to %(pronoun2)s phone."
    show loPic talk
    lo "I'm [loName!s]. You?" #https://www.renpy.org/doc/html/text.html
    "[pronoun1cap!s] hands you [pronoun2!s] phone."

    $ mcName = renpy.input("Enter your name") #https://www.renpy.org/wiki/renpy/doc/cookbook/Letting_players_choose_their_own_name
    $ mcName.strip()
    if mcName == "":
        $mcName = "Jay"
    lo "Nice to meet you, [mcName!s]!"
    "[loName!s] puts out [pronoun2!s] hand to shake. You take it and a smile ghosts across your lips."
    hide loPic with dissolve
    "(Maybe it won't be so bad here after all.)"
    "Suddenly, a thought crosses your mind."
    show loPic default with dissolve
    "You fish out your phone as well, and exchange numbers with [loName!s]."
    "You open a new text conversation."
    mc "What were those signs you used?"
    show loPic talk
    lo "I was asking if anyone was sitting here."

    show loPic talk at left
    show sign now at truecenter #https://www.renpy.org/doc/html/transforms.html#creator-defined-transforms
    lo "Now"
    show sign anyone at truecenter
    lo "anyone"
    show sign sit at truecenter
    lo "sit"
    show sign here at truecenter
    lo "here."
    hide sign

    lo "There's no 'ing' words in sign language, so you indicate tense by adding 'now' to the beginning of your sentence."
    lo "You wanna try?"

    label slAnswer1: #would be better not to hardcode this but no time asdlfkjasdls
        show loPic default
        $ score = ""
        #would randomize if had more time
        show sign sit at truecenter
        $ answer = renpy.input("Enter the word")
        if answer == "sit":
            $ score = score + "1"
        show sign anyone
        $ answer = renpy.input("Enter the word")
        if answer == "anyone":
            $ score = score + "1"
        show sign here
        $ answer = renpy.input("Enter the word")
        if answer == "here":
            $ score = score + "1"
        show sign now
        $ answer = renpy.input("Enter the word")
        if answer == "now":
            $ score = score + "1"

    if score == "1111":
        show loPic smile
        lo "See, you've got it!"
    else:
        show loPic talk
        lo "Not quite. Try again!"
        jump slAnswer1

    with None #https://www.renpy.org/doc/html/displaying_images.html#with-statement
    hide loPic
    hide sign
    with fade
    "The instructor walks into the class, and you stop leaning in the aisle and return to your desk."
    "You pay close attention during the class, but there’s too much new information all at once."
    "All you manage to remember is two signs."
    show sign yesPlease at truecenter with dissolve
    "Yes please,"
    show sign noThanks at truecenter with dissolve
    "and no thanks."
    hide sign with dissolve
    "The instructor finishes the class and you let out a huge sigh, dropping your head into your arms on your desk."
    "You were wrong. It’s just as bad as you thought it would be."
    "You let out a loud groan."
    mc "This is hopeless."
    show loPic default at center
    "You feel a tap on your shoulder, and [loName!s] is there, pointing at [pronoun2!s] phone."
    lo "Want some snacks?"

    menu snacks:
        "{image=sign yesPlease}":
            jump yes_snacks
        "{image=sign noThanks}":
            jump no_snacks

    label yes_snacks:
        show loPic smile
        lo "Here you go!"
        "[loName!s] hands you some chips."
        jump after_snacks

    label no_snacks:
        show loPic talk
        lo "Aw, ok."
        "[loName!s] looks a bit disappointed."
        jump after_snacks

    label after_snacks:
        show loPic default
        "[loName!s] takes [pronoun2!s] chair and drags it over to your desk."
        "[pronoun1cap!s] drapes [pronoun2!s] legs over the sides, resting [pronoun2!s] chin on the back of the chair to peer up at you."
    show loPic talk
    lo "What's bugging you?"
    show loPic default
    mc "It's just..."
    "You sigh."
    mc "Sign language is really hard."
    mc "I'm not any good at remembering all the different hand signs, and it's so different from any language I've learned before."
    show loPic smile
    "[loName!s] smiles kindly."
    show loPic default
    "[pronoun1cap!s] places a reassuring hand on your arm."
    show loPic talk
    lo "Don’t be too hard on yourself, [mcName!s]."
    lo "It’s only your first day, you’ll definitely improve with time."
    lo "Soon you’ll be good enough to have full conversations with just your hands - and I don’t mean by typing on a phone like we are now."
    lo "How bout this?"
    lo "I’ll help you."
    lo "I’ll walk with you to the station, and we can meet before class on the roof every day."
    show loPic smile
    lo "We can review what you learned from the class, and what you learned from me."
    "You perk up a bit, and can’t help but smile back at [loName!s]."
    mc "You know… I think I’d really like that."
    lo "Awesome, let’s go then!"
    "[loName!s] takes your hand and pulls you out of the room excitedly."

    scene outside with fade
    "The two of you exit the school, and you’re left holding hands, staring up at the starry night sky."
    show loPic talk with dissolve
    "[loName!s] tugs your sleeve and signs with one hand."
    "Your eyes light up as you remember the sign from the class."
    with None
    show loPic smile at left
    show sign pretty at truecenter
    with dissolve
    lo "Pretty."
    with None
    hide sign pretty
    show loPic default at center
    with dissolve
    "You smirk a bit, and pull your phone out of your pocket to respond."
    mc "Me, or the sky?"
    show loPic smile
    "[loName!s] smiles sweetly and looks into your eyes."
    "[pronoun1cap!s] lets go of your hand, and signs,"
    with None
    show loPic smile at left
    show sign both at truecenter
    with dissolve
    "Both."
    with None
    hide loPic
    hide sign
    with dissolve
    "You started it, but you can’t help but blush."
    "You quickly turn to your phone to hide your reddening cheeks."
    label slAnswer2:
        hide loPic with dissolve
        mc "I remembered those signs!{nw}" #https://www.renpy.org/doc/html/text.html#text-displayables
        mc "I remembered those signs!{fast} Pretty,"
        menu:
            "{image=sign both}":
                $ answer = "0"
            "{image=sign pretty}":
                $answer = "1"
        "and both!"
        menu:
            "{image=sign both}":
                $ answer = answer + "1"
            "{image=sign pretty}":
                $answer = answer + "0"
        show loPic talk

    if answer=="11":
        lo "You did! See, you'll pick it up in no time."
    else:
        lo "Not quite. But that's ok! Just keep trying your best and you'll get it soon."
        jump slAnswer2
    show loPic default
    "Maybe [loName!s] is right. You feel reassured knowing that [pronoun1!s] has your back."

    "Seemingly all too soon, you’ve reached the station."
    show loPic talk
    lo "Well, it seems this is where we part ways."
    "You snicker a bit, and roll your eyes exaggeratedly."
    mc "So dramatic."
    show loPic smile
    lo "I’ll see you on the roof before next class though, right?"
    "You smile, and nod."
    hide loPic with fade
    "As [loName!s]'s train pulls in, you put your phone back in your pocket, and wave goodnight."

    scene roof with fade
    "The next night comes, and you climb the stairs to the roof."
    show loPic default with dissolve
    "[loName!s] is there waiting for you."
    "[pronoun1cap!s] waves you over and pats the ground next to [pronoun0!s]."
    "[pronoun1cap!s] pulls out [pronoun2!s] phone."
    show loPic talk
    lo "Come join me!"
    "You go sit beside [loName!s], on the blanket [pronoun1!s] so graciously prepared for you."
    lo "So, do you remember what you learned last time?"
    mc "I sure do!"

    label slAnswer3:
        lo "Alright, I'll test you then!"
        show loPic default at left

        $ score = 0
        show sign yesPlease at truecenter
        $ answer = renpy.input("Enter the word")
        if answer == "yes please":
            $ score = score + 1
        show sign now
        $ answer = renpy.input("Enter the word")
        if answer == "now":
            $ score = score + 1
        show sign sit at truecenter
        $ answer = renpy.input("Enter the word")
        if answer == "sit":
            $ score = score + 1
        show sign both
        $ answer = renpy.input("Enter the word")
        if answer == "both":
            $ score = score + 1
        show sign anyone
        $ answer = renpy.input("Enter the word")
        if answer == "anyone":
            $ score = score + 1
        show sign pretty
        $ answer = renpy.input("Enter the word")
        if answer == "pretty":
            $ score = score + 1
        show sign here
        $ answer = renpy.input("Enter the word")
        if answer == "here":
            $ score = score + 1
        show sign noThanks
        $ answer = renpy.input("Enter the word")
        if answer == "no thanks":
            $ score = score + 1

    hide sign
    if score == 8:
        show loPic smile at center with dissolve
        lo "Whoo! Awesome job!"
        lo "You remembered all of them!"
    elif score > 5:
        show loPic talk at center with dissolve
        lo "You only missed a few. Don't worry, you've got this!"
        jump slAnswer3
    elif score > 1:
        show loPic talk at center with dissolve
        lo "You missed some of them. You'll get it soon, I believe in you!"
        jump slAnswer3
    else:
        show loPic default at center with dissolve
        lo "Ah. You got all them wrong."
        show loPic talk
        lo "But that's ok! I'll help you practice."
        jump slAnswer3

    show loPic default
    mc "Besides that though… I did some studying on my own, and… I wanted to surprise you."

return #game end

#transform properties: https://www.renpy.org/doc/html/atl.html#transform-properties
#transition: https://www.renpy.org/doc/html/transitions.html
#menu visuals customization: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
#remember user choices: https://www.renpy.org/wiki/renpy/doc/tutorials/Remembering_User_Choices
#clicked actions: https://www.renpy.org/doc/html/screen_actions.html#actions