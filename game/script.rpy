# The script of the game goes in this file.

define mc = Character("You", color="#c35e77") #pink

label start: # The game starts here.
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg room #** replace with background

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

define mc = Character("You", color="#c35e77") #pink for now
define lo = Character("Connie", color="#5e9ca5") #turquoise for now

    return
