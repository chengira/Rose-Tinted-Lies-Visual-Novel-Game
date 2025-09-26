# The script of the game goes in this file.



# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kd = Character("Kai Danko")
define b_Unknown = Character("? ? ?", color = "#d6a99a")
define bella = Character("Bela", color = "#e7a38d")
define bc = Character("Bela Camelia", color = "#e7a38d")
define teach = Character("Teacher", color = "#679277")
image id = "student ID.png"

# The game starts here.

label start:
    stop music

    play sound "<from 0 to 10>audio/Bell Ringing.ogg"
    
    scene bg class 1 alt with fade
    "{bt=3}~~~ 9:00 AM --- Morning ~~~{/bt}"
    
    play music "relax.ogg" volume 0.22 fadein 0.1 loop 

    pause 1.1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg class 1 with fade:
        zoom 1.4
        xalign 0.5

    # These display lines of dialogue.
    teach "All right class, introduce yourselves."

    play sound "<from 0.5 to 3.2>Footsteps.ogg" volume 1.22 fadein 0.03 fadeout 0.8
    show mc neutral
    with dissolve

    "{i}A soft-faced teenager stands in front of the class.{/i}"
    stop sound
    show mc surprised

    kd "{bt=1}H-Hello{/bt} everyone, my name is Kai Danko and I'm from a town in the countryside."

    show mc neutral
    kd "I like to spend my time reading, sketching, and going outdoors."

    show mc regular
    kd "I’m looking forward to getting to know everyone!"
    show mc neutral

    scene bg class 1 alt:
        zoom 1
        xalign 0.5

    teach "Here's your student ID, make sure you don't lose it. I've already got enough paperwork as is..."

    show id with fade:
        zoom 0.75
        xalign 0.5

    "{i}A student ID, the name of the student is Kai Danko... Seems to be the final year of highschool.{/i}"

    hide id
    scene bg class 1 with fade

    show mc neutral:
        xzoom 1
        yalign 1.0
        xalign 0.5
    with dissolve

    kd ". . ."

    scene bg class 1 alt with fade

    play sound "<from 0 to 10>audio/Bell Ringing.ogg"
    "{bt=3}~~~Class ends~~~{/bt}"
    # This ends the game.

    #SCENE 2
label libraryScene1:
    scene library 1 with fade:
        zoom 0.5
    "{bt=2}~~ In the Library ~~{/bt}"
    pause 0.5

    scene library 1 with fade:
        zoom 0.75
        xoffset -860
        yoffset -180

    show f mc back:
        zoom 1.1
        xzoom -1.0
        xalign 0.8
        yalign 1.0
    with dissolve
    b_Unknown "{i}A girl tucked away in a secluded corner, her eyes locked on the pages of a book.{/i}"

    scene library 1 with fade:
        zoom 0.5

    show f mc back:
        zoom 0.8 
        xzoom 1.0
        xalign 0.85
        yalign 1.0
        xpos 0.9
        ease 2.2 xpos 0.65
        pause 0.15
        xzoom -1.0
        ease 2.1 xpos 0.87

    show mc surprised:
        xalign 0.0
        yalign 1.0

    kd "{i}(Kai watches her intently...){/i}"

    show mc neutral

    show dark screen
    with dissolve
menu:
    
    "Take a closer look.":
        jump libraryInteractChoice
    "Leave.":
        jump libraryDontInteract

label libraryInteractChoice:
    scene library 1 with fade:
        zoom 0.5
    show mc surprised
    with dissolve
    kd "Excuse me..."

    hide mc surprised

    show f mc surprised
    play sound "arere.mp3" volume 0.8
    with vpunch
    b_Unknown "! ! !"

    hide f mc surprised

    show mc surprised
    play sound "arere.mp3" volume 0.4
    with hpunch

    kd "! ! !"

    show mc regular
    kd "I'm sorry, did I surprise you?" 

    show mc surprised
    kd "I was just wondering if you could point me in the direction of the science labs?"

    hide mc surprised

    show f mc full alt:
        zoom 0.6
        xalign 0.5
    with dissolve
    b_Unknown "Ah, sure."

    show f mc full

    b_Unknown "Just go around the corner and up the stairs, you should see the sign for the labs."

    hide f mc full

    show mc full:
        zoom 1.3
        xalign 0.555
        yalign 0.05
    with dissolve
    
    kd "Thanks, I appreciate the help."

    show mc full surprised

    kd "I didn't catch your name by the way."

    show mc full 

    kd "I'm Kai Danko, 3rd year."

    hide mc full

    show f mc full alt:
        zoom 0.6
        xalign 0.5

    b_Unknown "Oh sorry, I haven't introduced myself yet."

    show f mc full
    bella "My name is Bela." 
    show f mc full alt
    bc "Bela Camelia, 3rd year as well. Nice to meet you."

    hide f mc full

    show mc full:
        zoom 1.3
        xalign 0.555
        yalign 0.05
    
    kd "Nice to meet you." 
    
    show mc full surprised 
    kd "I'm in a rush to my next class right now, I'll see you around."

    show mc full neutral

    jump leaveLibrary

label libraryDontInteract:
    jump leaveLibrary

label leaveLibrary:
    scene library 1 with fade:
        zoom 0.5

    show dark screen
    with dissolve

    "{bt=2}~~ Leaving the Library ~~{/bt}"

label mcRoom:
    scene room dark 1 with fade:
        zoom 1.3
        xoffset -300
    "{bt=1}Back at home. . . {/bt}"

    scene room with fade:
        zoom 1.3
        xoffset -300

    show mc neutral
    with dissolve

    kd ". . ."
    kd ". . . . ."

    kd "Her name. . ."
    play sound "<from 0.052 to 5>giku.mp3" volume 0.6
    kd "It reminds me. . ."

    kd "It reminds me of my late mother's favourite flower."
    show mc eerie 1
    show dark screen 2
    with dissolve

    stop music
    pause 0.1
    play sound "shock.mp3" volume 0.8
    kd "I wonder what she'll be doing during the weekend, after all, I've already managed to collect her after school habits."
    pause 0.5
    play music "Doll-Dance.ogg" volume 0.22 fadein 0.1 loop 

label demoEnd:
    scene room dark 2 with fade:
        zoom 1.1
    'End of demo. . .'
    stop music

    return
