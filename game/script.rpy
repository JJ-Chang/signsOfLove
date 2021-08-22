﻿# The script of the game goes in this file.

#characters
define mc = DynamicCharacter("mcName", color="#c35e77", outlinecolor="white") #pink https://www.renpy.org/wiki/renpy/doc/cookbook/Who's_that%3F
define lo = DynamicCharacter("loName", color="#c6d7c8", outlinecolor="black")
$ mcName = "You"
$ lo = "???"

#background images
image classroom = "classroomPlaceholder.jpg"

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

    image sign now small:
        "now.png"
        zoom .3
    image sign anyone small: #https://www.reddit.com/r/RenPy/comments/iglq6o/playing_gifs_in_renpy/
        zoom .3
        "any1.png"
        0.5
        "any2.png"
        0.5
        "one.png"
        0.5
        repeat
    image sign sit small:
        "sit.png"
        zoom  .3
    image sign here small:
        "here.png"
        zoom .3

#define styles
style slButton_left_top is image: #https://www.renpy.org/doc/html/style.html
    xanchor 600 #https://www.renpy.org/doc/html/style_properties.html
    yanchor 360
style slButton_right_top is image:
    xanchor 860
    yanchor 360
style slButton_left_bottom is image:
    xanchor 600
    yanchor 710
style slButton_right_bottom is image:
    xanchor 860
    yanchor 710

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
    #lo "{image=now}{alt}now sign{/alt}{image=anyone}{alt}anyone sign{/alt}{image=sit}{alt}sit sign{/alt}{image=here}{alt}here sign{/alt}\nNow anyone sit here" #https://www.renpy.org/doc/html/text.html#text-tag-image

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

#     menu sl1: #https://lemmasoft.renai.us/forums/viewtopic.php?t=36963
#         "{image=nowSmall}": #https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=26705
#             $ selection += "Now"
#         "{image=anyone}":
#             $ selection += "Anyone"
#         "{image=sit}":
#             $ selection += "Sit"
#         "{image=here}":
#             $ selection += "Here"
#     menu sl1:
#         " (sign now small)":
#             $ selection += "Now"
#         " (sign anyone small)":
#             $ selection += "Selection"
#         " (sign sit small)":
#             $ selection += "Sit"
#         " (sign here small)":
#             $ selection += "Here"
#     label slSelect0:
#         call screen slImageMap0
#
#         show sign anyone style slButton_left_top
#         show sign here style slButton_right_top
#         show sign sit style slButton_left_bottom
#         show sign now style slButton_right_bottom
#
#         $ result = _return
#         if result == "now":
#             $ selection += "Now"
#         elif result == "anyone":
#             $ selection += "Anyone"
#         elif result == "sit":
#             $ selection += "Sit"
#         elif result == "here":
#             $ selection += "Here"
    label slAnswer1: #would be better not to hardcode this but no time asdlfkjasdls
#         python: #https://lemmasoft.renai.us/forums/viewtopic.php?t=40012
#             for r in [3, 2, 1, 4]: #https://lemmasoft.renai.us/forums/viewtopic.php?t=21196
#                 if r == 1:
#                     renpy.show("sign now") #should remember truecenter placement
#                 elif r == 2:
#                     renpy.show("sign anyone")
#                 elif r == 3:
#                     renpy.show("sign sit")
#                 elif r == 4:
#                     renpy.show("sign here")
#
#                 answer = renpy.input("Enter the word")
#                 if r == 1:
#                     if answer.lower == "now": #https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
#                         score += "1"
#                     else:
#                         score += "0"
#                 elif r == 2:
#                     if answer.lower == "anyone":
#                         score += "1"
#                     else:
#                         score += "0"
#                 elif r == 3:
#                     if answer.lower == "sit":
#                         score += "1"
#                     else:
#                         score += "0"
#                 elif r == 4:
#                     if answer.lower == "here":
#                         score += "1"
#                     else:
#                         score += "0"
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


return #game end

# screen choice(items): #https://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=31059&start=0
#     window:
#         style "menu_window"
#         xalign 0.5
#         yalign 0.5
#
#         vbox:
#             style "menu_vbox"
#             spacing 2
#
#             for caption, action, chosen in items:
#                 if action:
#                     $ finder = caption[caption.find("(")+1:caption.find(")")]
#                     $ caption = caption.replace(" (%s)" % finder, "")
#                     button:
#                        action action
#                        style "menu_choice_button"
#                        has hbox
#                        if finder:
#                            add "%s" % finder
#                            null width 10    # some space between the image and the text
#                        text caption style "menu_choice"
#                 else:
#                     text caption style "menu_caption"

#transform properties: https://www.renpy.org/doc/html/atl.html#transform-properties
#transition: https://www.renpy.org/doc/html/transitions.html
#menu visuals customization: https://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
#remember user choices: https://www.renpy.org/wiki/renpy/doc/tutorials/Remembering_User_Choices
#clicked actions: https://www.renpy.org/doc/html/screen_actions.html#actions