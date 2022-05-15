# Chapter four, how to play dragon realm

import random

import time

# A function that gives a brief introduction to the scenario in question

# Frostbite?

def displayintro():
    print("""
    It's a cold, dark night, the wind is howling, the eerie moonlight flickers through the tattered remains of what
    once were curtains. Stood sheepishly at the foot of a grand stair case as an ominous chill lingers down each step
    towards you. Gulping, as you scan the once majestic estate that is now left in ruin. You cautiously raise your
    right foot, your eyes dart back and fourth between the two directions of the stair case.
     """)

print()

# A function that gives the player a choice between two directions and returns the input

def choosedirection():
    direction = ""
    while direction != "right" and direction != "left":
        print("Which way do you so wish to explore first? (left and right)")
        direction = input()
    return direction

print()

def checkdirection(chosendirection):
    print("You intrepidly approach the fork in the stairs")
    time.sleep(2)
    input()
    print("Your heart racing as the fear and uncertainty grow to a fever pitch")
    time.sleep(1)
    input()
    print("""
    The door at the summit of the stairs behinds you slams shut without warning, followed by the front door.
    Fearfully jerking your head back, out of the corner of your eye intently watching the once opened and sinisterly
    inviting door.
    """)
    time.sleep(4)
    input()
    print("""
    Taking a moment, trying to stop the growing sense of dread from incapacitating you where you stand.
    Wishing you had eyes in the back of your head as you recenter yourself, warily swivelling your head back forward.
    Tightly clenching the banister as your knuckles go white from the encroaching terrors flooding your mind.
    Alert as you start to tip-toe from step to step, just hoping the bone chilling anxiety is all but a figment of
    your imagination.
    """)
    time.sleep(2)
    input()

    #friendlydirection = random.randint(1,2)

    if chosendirection == "left":
        print("""
        The door before you opens a creak, a red carpet of ice begins creeping towards you.
        Looking up you see something that makes your hair stand on end, the heat from the room almost instantly
        evaporates as your breathing quickens. Your body tenses as you peer through the fog you're exhuming though
        your mouth. What you see is a tall, menacing snowman. Complete with a top hat and a carrot nose. Beady eyes
        and a cheeky grin that makes you just wish you had went the other way.
        """)
    else:
        print("""
        The moonlight shines through a hole in the roof as it is uncovered by clouds, a frightfully telling
        silhouette paints itself on the floor just in front of you. Bats, your eyes widen as you look forward. But
        it's too late, a slender, well dress figure is already towering over you. The sickly scent of iron
        infiltrates your nose. You try to speak, to scream, to run. You feel yourself go light headed, feet going numb
        as the moonlight glimmers off of their pearly white teeth. Ensnared by your emotions as your imagination runs
        amok and you're left helplessly dumbstruck staring up at this mythical beast.
        """)

playagain = "yes"
while playagain == "yes" or playagain == "y":
    displayintro()
    directionnumber = choosedirection()
    checkdirection(directionnumber)

    print("Do you want to play again? (Yes or No)")
    playagain = input()