# The script of the game goes in this file.

#characters
define mc = Character("You", color="#c35e77") #pink
define lo = Character("name", color="#c6d7c8") #green

#background images
image classroom = "classroomPlaceholder.jpg"

#character images
image hui default = "maleLOplaceholder.png"
image connie default = "femaleLOplaceholder.png"


label start: # The game starts here.
    label the_beginning:
        "test start"
        menu:
           "Keep going":
                jump the_beginning
           "The end!":
                jump the_end

    label the_end:
        "You did it! You made it to the end!"
        "Congratulations!"

    scene classroom
    "You sigh as you walk into the classroom."
    "You never expected you would be attending a nighttime sign language class, but after the car accident that caused you to lose your hearing, you don’t have much of a choice."
    "You look around for empty seats, and settle on a desk in the back of the room."
    "You’re open to meeting new people, but you won’t go out of your way to make friends here. You just want to learn enough to get on with your life."
    "Out of the corner of your eye, you see..."

    #select LO
    show hui default at left
    show connie default at right

    menu select_lo:
        "a girl":
            jump girl
        "a boy":
            jump boy
    #implement image map if there's time, to click on the actual images of the LOs
    #     screen selectLO_imagemap:
    #         imagemap:
    #             hotspot() #maleLO
    #             hotspot() #femaleLO

    label boy:
        scene classroom
        $ gender = "boy"
        $ pronoun0 ="him"
        $ pronoun1 ="he"
        $ pronoun2 ="his"

        jump after_select_lo

    label girl:
        scene classroom
        $ gender ="girl"
        $ pronoun0 ="her"
        $ pronoun1 ="she"
        $ pronoun2 ="her"

        jump after_select_lo

    label after_select_lo:
        if $ gender == "girl":
            $ isF = 2
        else:
            $ isF = 0
        image lo default = ConditionSwitch(
            "isF > 1", "femaleLOplaceholder.png"
            "isF < 1", "maleLOplaceholder.png"
        )
        show lo default at center

    "you see a %(gender)s come stand behind the desk beside you. You turn to face %(pronoun0)s."
    "%(pronoun1)s smiles radiantly down at you, and %(pronoun1)s moves %(pronoun2)s hands in a series of patterns."
    "You pause for a second, confused, before pursing your eyebrows and tilting your head."

#define mc = Character("You", color="#c35e77") #pink for now
#define lo = Character("Connie", color="#5e9ca5") #turquoise for now

    return #game end