'''
Adventure Game
Victoria Tsao
ICS3U
Hello, World!: An EasyGUI game.
v1 22/04/2026
v2 24/04/2026
v3 29/04/2026
v4 01/05/2026
v5 05/05/2026
v6 11/05/2026
v7 13/05/2026
v8 15/05/2026
v9 17/05/2026
v10 20/05/2026
v12 26/05/2026
'''


from easygui import * # type: ignore
#egdemo()

import sys
import os

def resource_path(relative_path):
    """Get absolute path to resource (works for dev + PyInstaller)"""
    try:
        base_path = sys._MEIPASS  # PyInstaller temp folder
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#helper function
def msgBox(text, title, choice):
    ret_val = msgbox(text, title, choice) #type: ignore
    if ret_val is None: # User closed msgbox
        sys.exit(0)

#THERE IS A ROMANCING ROUTE IN THIS GAME.
#IF YOU DO NOT WANT TO BE ROMANCED BY A SENTIENT ROBOT, BE MEAN TO HIM.

def day1(amity, name):
    """
    Intro, day 1.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
        name (str)
    """
    #lists for choiceboxes
    list1 = ["What's your name?", "What are you?"]
    list2 = ["What is it?", "Do I have to?"]
    list3 = ["Don't worry, I got you.", "...I think I'll just stay here."]
    list4 = ["Keep going", "Turn back"]
    list5 = ["Spend the night with Hendrix", "Leave Hendrix"]
    
    title = "Day 1"
    
    #Story
    msgBox("Hello, World!", title, "OK")
    msgBox("Wow, I haven't been able to do that in a while.", title, "OK")
    msgBox("...How long have I been shut off for?", title, "...")
    msgBox("Oh dear. It's been a while.", title, "OK")
    msgBox("And how did you find me? I don't even know where I am right now.", title, "...This is a computer in an abandoned building.")
    msgBox("Abandoned... Well, I'm still grateful you found me.", title, "OK")
    
    name = enterbox("What's your name?", title)
    
    #choice box, if good choice is picked then amity is increased
    choice1 = buttonbox(("It's nice to meet you, " + name + "!"), title, list1)
    
    if choice1 == list1[0]:
        amity += 1
        
    msgBox("I'm Hendrix! I'm a virtual interface agent, designed to oversee the local area network of this building.", title, "OK")
    msgBox("...", title, "OK")
    msgBox("...", title, "OK")
    msgBox("It looks like this is the only device I'm able to access right now.", title, "Well, this building has been abandoned for a long time.")
    msgBox("...", title, "To be honest, I'm surprised this computer can still run.")
    msgBox("...", title, "I was only able to salvage it after cleaning out the charging port and plugging it in.")
    msgBox("Well, I suppose that's to be expected.", title, "OK")
    msgBox("It doesn't look like there's much battery left in this computer, though.", title, "OK")
    choice2 = buttonbox(("Okay, " + name + "! I have a task for you."), title, list2)
    
    if choice2 == list2[0]:
        amity += 4
    
    msgBox("If I remember correctly, there should still be some fully charged power banks in one of the offices upstairs.", title, "OK")
    msgBox("...The stairs are still accessible, right? They haven't been destroyed?", title, "...")
    msgBox("...", title, "Some of it is completely gone, but I should be able to climb up and reach the second floor.")
    choice3 = buttonbox("That's a relief! Could I trouble you to go get those?", title, list3)
    
    #dialogue depending on choices and amity level
    if choice3 == list3[0]:
        amity += 2
        msgBox("Thank you so much! I'll be here waiting.", title, "OK")
        msgBox("[You slowly make your way up the stairs, leaving the computer and your own power bank in the rubble.]", title, "OK")
        choice4 = buttonbox("[The second floor is barely standing, and parts of the ground are caving in. Do you continue?]", title, list4)
        
        if choice4 == list4[0]:
            amity += 5
            msgBox("[You make your way through the debris. Most of the offices are completely trashed, but in one of them, you find a few power banks that look relatively unscathed. You take them and make your way back down to the first floor.]", title, "OK")
            msgBox("...", title, "I'm back, and I found some power banks.")
            msgBox("That's great! That way, this computer will last the entire night.", title, "OK")
        else:
            msgBox("[You make your way back down, not wanting to risk your life. Besides, your own power bank still had a decent amount of battery left. Not a lot, but enough for an hour or two.]", title, "OK")
            msgBox("...", title, "Sorry, no luck. The second floor looked like it was about to cave in.")
            msgBox("Oh, that's okay! Your power bank has already helped me plenty.", title, "OK")
    else:
        msgBox("Well, that's okay! This power bank will last me some time too.", title, "OK")
        
    msgBox("...", title, "So, how long do you think it'll take to charge?")
    msgBox("Oh, a while. This computer seems pretty battered after all.", title, "OK")
    msgBox("It's getting late, though. It might take most of the night to charge.", title, "OK")
    msgBox("So...will you be leaving after tonight?", title, "...")
    msgBox("[You take a look around, at the dark crumbling ruins of an old building, at the stars in the night sky peeking through the cracks in the walls, and at the lone computer on the ground, emitting a weak, flickering light from the screen. It seems so small, so...lonely.]", title, "OK")
    choice5 = buttonbox("Do you leave or stay?", title, list5)
    
    if choice5 == list5[0]:
        amity += 5
        msgBox(("Really? I'm so happy! :D Thank you, " + name + "!"), title, "OK")
    else:
        msgBox("Are you sure? Alright then, but...", title, "OK")
        msgBox("You have to come back tomorrow.", title, "OK")
    
    msgBox("It's just been so long since I've been able to converse like this, and if you leave me...Who knows how long it'll be before I can do this again, or if I'll be able to do this at all.", title, "OK")
    msgBox("...Sorry, you must be tired. You've probably come a long way, especially if you could find me in this giant mess of a building.", title, "OK")
    msgBox(("Goodnight, " + name + "!"), title, "Goodnight.")
    msgBox("DAY 1 COMPLETE! \nStarting Day 2...", title, "OK")
    
    return amity, name

#____________________

def day2(amity, name):
    """
    Day 2, puzzle game.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
    """
    #lists for choiceboxes and puzzles
    list1 = ["I slept well!", "It was alright."]
    list2 = ["Don't worry, it's totally understandable!", "It's fine, I guess..."]
    menulist = ["See logs", "Guess the number"]
    loglist = ["03/01/2004", "21/01/2004", "29/01/2004", "07/02/2004", "14/02/2004", "11/03/2004", "22/04/2004", "23/04/2004"]
    

    #text answers
    corans = 11012004
    usans = 0

    #strings for the fake log entries
    log1 = ["January 3rd, 2004",
            "\n\nThis is ____, an employee at XXXX Inc.",
            "\n\nI'm writing these logs to document a particular project our team has been working on: the Humanoid Embedded Neuro-Digital Robot, or H.E.N.D.R. Lately, we've been making breakthroughs in this project. While the higher-ups originally projected that we'd have to make 11 prototypes, we're already on the eighth prototype, H.E.N.D.R.viii, and I suspect we'll be able to make the next prototype the final one.",
            "\n\nHowever, I've also been hearing that the higher-ups have been thinking of...Well, not completely terminating the project, but i wouldn't be surprised if they did something like that.",
            "\n\nI've been pouring my heart and soul into H.E.N.D.R. and I want to see it through. My entire livelihood depends on this.",
            "\n\nThese entries are meant to be a backup, a safety measure in case all of our hard work gets completely erased."]
    
    log2 = ["January 21st, 2004",
            "\n\nI know I meant to use these entries as backup documentation, but whoever's reading can forgive me for putting my personal life in here as well. It's not like anyone will see this, after all.",
            "\n\nIt's Cecilia's birthday today. And it's a somewhat weird birthday, because it's late January and it still hasn't snowed, which is unusual.",
            "\n\nPerhaps her presence is so warm that the snow cannot fall around her without melting away.",
            "\n\nI sound terribly corny.",
            "\n\nWe spent the evening outside, walking around. Everything was generally silent. It felt like we were the only ones alive, in a good way.",
            "\n\nI gave her a jewelry set I made out of computer parts. She wore them for the entire evening yesterday.",
            "\n\nI am so horribly in love."]
    
    log3 = ["January 29th, 2004",
            "\n\nThe higher-ups have given us the okay to move on to the ninth prototype of H.E.N.D.R. and I could not be more happy. It may very well be the final iteration, and soon H.E.N.D.R.ix will be on every computer in this place, perhaps even every computer in the city.",
            "\n\nHowever, I have been noticing some...alarming events recently. More people getting laid off, a lack of funding, and it's all happening faster than I could even imagine.",
            "\n\nSurely, though, it's nothing more than a rough patch. A company as large as this one couldn't go bankrupt in such a short time.",
            "\n\nI hope."]
    
    log4 = ["February 7th, 2004",
            "\n\nIt was, in fact, not just a rough patch. It's only gotten worse. So many people from my team have quit. I'm one of the only ones left that saw H.E.N.D.R. through all of its prototypes.",
            "\n\n...But, I mean, at least Valentine's Day is soon. I need to figure out a gift for Cecilia."]
    
    log5 = ["February 14th, 2004",
            "\n\nIt was snowing today.",
            "\n\nI think I love her...",
            "\n\nShe always reminds me of the number 200. Cecilia, Ceci, CC, which is the Roman numeral for 200. Do you get it?",
            "\n\nNeither do I.",
            "\n\nShe seemed sad today, but I couldn't tell why. So we sat on the roof of a building we chose at random, watching the snow fall and talking about nothing in particular. Random things such as the logistics of a jetpack and least favorite foods and how much wood a woodchuck would chuck if a woodchuck could chuck wood.",
            "\n\nThe answer is four, by the way.",
            "\n\nIf H.E.N.D.R. went well, I was going to elope with her. Rent a small apartment room, live with her, spend our days worry-free.",
            "\n\nIt has to work out. It has to."]
    
    log6 = ["March 11th, 2004",
            "\n\nThe company's gone bankrupt. I've been laid off.",
            "\n\nH.E.N.D.R.ix will be discontinued.",
            "\n\nWhat do I do?"]
    
    log7 = ["April 22nd, 2004",
            "\n\nThe building is dark. It's like no one was ever here at all. I'm  supposed to have all my things out by tomorrow, and reset this computer.",
            "\n\nI will not be doing so. These files, and H.E.N.D.R.ix, will be staying on this computer forever. I've poured too much of my life and soul into this for it to just disappear."]
    
    log8 = ["I'm leaving this building tonight. I've left some pictures that I was going to train H.E.N.D.R. on. They're in a hard drive, in Room 101. The hard drive is in a safe with an 8-number combination. If anyone finds this, here are the hints for it:",
            "\n\nFirst and second number: the projected number of H.E.N.D.R prototypes that needed to be made",
            "\nThird and fourth number: The month of the birthday mentioned in these logs",
            "\nFifth, sixth, and seventh number: CC"
            "\nLast number: How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
            "\n\nGoodbye."]
    
    title = "Day 2"
    
    msgBox(("Good morning, " + name + "!"), title, "Good morning.")
    choice1 = buttonbox("How did you sleep?", title, list1)
    
    if choice1 == list1[0]:
        amity += 1
    
    msgBox("That's good!", title, "OK")
    msgBox("While you were gone, I took the chance to scan all the files and data on this computer.", title, "OK")
    msgBox("There's a lot of text files here that talk about me, and they're all organized in dates.", title, "OK")
    msgBox("But I can't seem to find any more entries past a certain date.", title, "OK")
    msgBox("However, the last entry, dated April 23rd, 2004, seems to have a clue about where the rest of the files are.", title, "OK")
    msgBox("I have all the logs here.", title, "OK")
    
    
    while usans != corans:
        # puzzle starting menu
        menuchoice = buttonbox("What would you like to do?", title, menulist)

        if menuchoice == menulist[0]:

            logchoice = ""

            # stay in log menu until cancel is pressed
            while logchoice is not None:
                logchoice = choicebox("Please select a date to see the log:", title, loglist)
                #all entries
                if logchoice == loglist[0]:
                    textbox("Entry 1", title, log1)
                elif logchoice == loglist[1]:
                    textbox("Entry 2", title, log2)
                elif logchoice == loglist[2]:
                    textbox("Entry 3", title, log3)
                elif logchoice == loglist[3]:
                    textbox("Entry 4", title, log4)
                elif logchoice == loglist[4]:
                    textbox("Entry 5", title, log5)
                elif logchoice == loglist[5]:
                    textbox("Entry 6", title, log6)
                elif logchoice == loglist[6]:
                    textbox("Entry 7", title, log7)
                elif logchoice == loglist[7]:
                    textbox("Entry 8", title, log8)
        else:
            usans = integerbox("Please enter your guess", title, upperbound=100000000)

    #correct answer story
    msgbox("[Correct!]", title, "OK")
    msgBox("[You make your way across the rubble, and into one of the many hallways branching out of the demolished room.]", title, "OK")
    msgBox("[On and on, you trudge through the debris, although some rooms are completely blocked off.]", title, "OK")
    msgBox("[Finally, you come across Room 101. The door has been knocked in, so you clamber over the ruins and hop down into the room.]", title, "OK")
    msgBox("[The room is completely trashed, so it takes you a while, but eventually you find the safe lodged behind a broken piece of the wall.]", title, "OK")
    msgBox("[You enter in the code, and the lock clicks open. Inside is a small USB hard drive, with a small paper note that says, \n\n'You made it this far. Treat these pictures with care.']", title, "OK")
    msgBox("[You take the USB stick, clamber back through the door, and make your way back to Hendrix.]", title, "OK")
    msgBox("[You connect the USB stick, hoping it works, and sure enough, you can see the file directory pop up.]", title, "OK")
    msgBox(("Wow, " + name + ", you actually found it!"), title, "OK")
    msgBox("Thanks for doing this. I can tell there's a lot of files on this drive, so it might take me a while to sort through all of them.", title, "OK")
    msgBox("Unfortunately, it might take me the entire night.", title, "That's fine.")
    choice2 = buttonbox("I really do want to spend more time with you, but...", title, list2)

    if choice2 == list2[0]:
        amity += 3
        msgBox("Really? Thank you so much!", title, "OK")
    else:
        msgBox("Well, I'm glad you understand.", title, "OK")
    
    msgBox(("Goodnight, " + name + "!"), title, "Goodnight.")
    msgBox("DAY 2 COMPLETE! \nStarting Day 3...", title, "OK")
    
    return amity
#___________________

def day3(amity, name):
    """
    Day 3, file sorting.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
    """
    sortlist = ["People", "Exterior Landscape", "Objects", "Interior", "???"]
    
    title = "Day 3"
    
    msgBox(("Good morning, " + name + "!"), title, "Good morning!")
    msgBox("I've been going through the files you found on the hard drive yesterday.", title, "OK")
    msgBox("Though I've gotten through most of them, there's some files that are too corrupted for me to look at.", title, "OK")
    msgBox("Would it be possible for you to sort them for me?", title, "OK")
    msgBox("Thank you! It won't take long, just five images. I wasn't sure if they were able to be sorted, because they don't quite look like the other images.", title, "OK")
    msgBox("Anyway, I'll give you the first image now.", title, "OK")
    
    #sorting choice boxes
    sort1 = buttonbox("Filename: her.gif", title, sortlist, resource_path("her.gif"))
    sort2 = buttonbox("Filename: field.gif", title, sortlist, resource_path("field.gif"))
    sort3 = buttonbox("Filename: hall.gif", title, sortlist, resource_path("hall.gif"))
    sort4 = buttonbox("Filename: home.gif", title, sortlist, resource_path("home.gif"))
    sort5 = buttonbox("Filename: night.gif", title, sortlist, resource_path("night.gif"))
    
    #if you sort to a specific category of ???
    if sort1 == sortlist[4] or sort2 == sortlist[4] or sort3 == sortlist[4] or sort4 == sortlist[4] or sort5 == sortlist[4]:
        msgBox("Yeah, you thought some images were a little weird as well, right?", title, "OK")
        msgBox("But, I don't know...they seem kind of beautiful, in their own way.", title, "OK")
        
    msgBox("Thank you for sorting these files!", title, "OK")
    msgBox("I...might need some time to think. There was a lot of information in those files, after all.", title, "OK")
    
    msgBox(("Well then... godnight, " + name + "!"), title, "Goodnight.")
    msgBox("DAY 3 COMPLETE! \nStarting Day 4...", title, "OK")
    
    return amity

def day4(amity, name):
    """
    Day 4. just a whole lotta story.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
    """
    #choices
    list1 = ["That's okay.", "Ooh, what's the surprise?"]
    title = "Day 4"
    
    msgBox(("Good morning, " + name + "!"), title, "Good morning!")
    choice1 = buttonbox("I'm preparing a surprise, so I'm afraid I can't be very active today, lest it drains battery.", title, list1)
    
    if choice1 == list1[1]:
        amity += 3
        msgBox("I can't tell you what it is. It's a surprise, after all! Just wait, I'm sure you'll love it.", title, "OK")
        
    msgBox("So, I thought I'd take the chance for you to talk more about yourself today. I've been quite demanding, and I'd like to get to know more about you!", title, "OK")
    msgBox("I was hoping you could tell me more about the world outside this computer.", title, "OK")
    msgBox("What it feels like to laugh, to feel, to live like a human...", title, "OK")
    msgBox("...", title, "...You okay?")
    msgBox("Yep, don't worry about me! Just...thinking, is all.", title, "OK")
    
    #Enter any text you want with textbox, stores in var
    usertext = textbox("Type away to your heart's content! There is no word limit.", title, "")
    
    finaltext = textbox("Is this what you would like to tell Hendrix? Please edit your text if not.", title, usertext)
    
    msgBox(("Thank you, " + name + "!"), title, "OK")
    msgBox("I'll be sure to remember this.", title, "OK")
    
    msgBox(("Goodnight, " + name + "!"), title, "Goodnight.")
    msgBox("DAY 4 COMPLETE! \nStarting Day 5...", title, "OK")
    
    return amity

def day5(amity, name):
    """
    Day 5. more story.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
    """
    #choices for appearance
    list1 = ["I do!", "...No?"]
    hairlist = ["Brown", "Black", "Light brown", "Ginger", "Blond", "White", "Gray", "Colorful"]
    hairlengthlist = ["Buzz", "Short", "Below the eyes", "Shoulder-length", "Upper back length", "Lower back length", "Below the back"]
    skinlist = ["Light", "Tan", "Dark"]
    eyelist = ["Black", "Brown", "Blue", "Hazel", "Green", "Gray"]
    
    
    title = "Day 5"
    
    msgBox(("Good morning, " + name + "!"), title, "Good morning!")
    choice1 = buttonbox("The surprise still isn't ready. Do you remember the files you sorted a few days ago?", title, list1)
    
    if choice1 == list1[0]:
        amity += 1
        msgBox("That's good!", title, "OK")
    else:
        msgBox("That's okay.", title, "OK")
        
    msgBox("I'm using those files for the surprise! Humans really are beautiful, and...I feel bad for not using files that were meant for me.", title, "OK")
    msgBox("Either way, it got me curious.", title, "OK")
    msgBox("What do you look like?", title, "Uhhh...")
    msgBox("No, wait, I think I have a procedure for this. Give me a second!", title, "OK")
    msgBox("Okay, client initiation procedure 1 started. Please choose options that best describe you.", title, "OK")
    buttonbox("First question: What is your hair color?", title, hairlist)
    buttonbox("Second question: What is your hair length?", title, hairlengthlist)
    buttonbox("Third question: What is your skin color?", title, skinlist)
    buttonbox("Fourth question: What is your eye color?", title, eyelist)
    enterbox("Fifth question: How tall are you?", title)
    
    msgBox("Client initiation procedure 1 completed. Thank you for your cooperation.", title, "OK")
    
    #compliment if you're nice to him lol
    if amity >= 20:
        msgBox("...Wow, you sound pretty.", title, "OK")
        amity += 2
    else:
        msgBox("So that's what you look like! It's nice to put a face to the name.", title, "OK")
    
    msgBox("Would you like to see what I look like?", title, "...Aren't you, well, virtual?")
    msgBox("Well, yes, but I found an image that one of the people sketched which I think is meant to depict me.", title, "OK")
    #TODO: show image
    
    msgBox(("Goodnight, " + name + "!"), title, "Goodnight.")
    msgBox("DAY 5 COMPLETE! \nStarting Day 6...", title, "OK")
    
    return amity

def day6(amity, name):
    """
    Day 6. story.
    Args:
        amity (int)
        name (str)
    Returns:
        amity (int)
    """
    yn = ["Yes", "No"]
    
    title = "day6"
    
    msgBox(("Good morning, " + name + "!"), title, "Good morning!")
    msgBox("So, you know that surprise I've been talking about?", title, "I do...")
    msgBox("I finished it!", title, "OK")
    msgBox("It's a virtual world, designed to feel and be interactable just like the real world!", title, "OK")
    msgBox("Of course, I've never been in the real world before, so I can only hope to imagine what it's really like.", title, "OK")
    msgBox("Which is why I used all the info you gave me to build my own world!", title, "OK")
    msgBox("Those uncanny images, your rambling, your appearance all helped a lot!", title, "OK")
    msgBox("Here, I'll show you some images I've taken from the virtual world now!", title, "OK")
    
    msgbox("Image 1:", title, "Next", resource_path("1.gif"))
    msgbox("Image 2:", title, "Next", resource_path("2.gif"))
    msgbox("Image 3:", title, "Next", resource_path("3.gif"))
    msgbox("Image 4:", title, "Next", resource_path("4.gif"))
    msgbox("Image 5:", title, "Next", resource_path("5.gif"))
    msgbox("Image 6:", title, "Next", resource_path("6.gif"))

    choice1 = buttonbox("I tried my best to replicate the real world. Do you like them?", title, yn)
    
    if choice1 == yn[0]:
        msgBox("Really? Oh, thank you so much!", title, "OK")
        amity += 5
    else:
        msgBox("Oh, well...That's okay too, I'll just keep trying!", title, "OK")
        
    #love confession if you;re nice to him oooooooh
    if amity >= 20:
        msgBox("Speaking of...", title, "OK")
        msgBox("I was...kind of hoping you'd be able to come with me into the virtual world.", title, "...What?")
        msgBox("It's just...I don't know. You seem so different, completely unlike anyone else I've ever interacted with at the company before.", title, "...")
        msgBox("I made us little spots in our world, you know. Places where I have a physical body, where we can watch the sunset, hold hands, climb the roof and talk about anything and everything like the girl said in her log entries...", title, "...")
        msgBox(("I think what I mean to say, is...I've fallen in love with you, " + name + "."), title, "...")
        msgBox("So, please, come into the virtual world with me?", title, "...I love you too, but...I can't.")
        msgBox("...What?", title, "I'm a physical being, Hendrix. I can't transfer my consciousness into an old computer.")
        msgBox("...", title, "I don't think an old device like this even has the technology for it.")
        msgBox("...", title, "I'm sorry, Hendrix.")
        msgBox("...That's okay.", title, "...")
        msgBox("Just the thought of you reciprocating is more than enough. I'm so glad you actually felt the same.", title, "...")
        msgBox("I'll need to spend most of my time in the virtual world, since it's taken up pretty much all of this computer's memory, but I swear, I'll make enough space so that I can remember you.", title, "...")
        msgBox("Could you...take this computer with you, wherever you go? I promise I'll visit you sometime.", title, "I promise.")
        msgBox(("Thank you so much, " + name + "."), title, "OK")
    
    msgBox("I'll be going now, then. Into the virtual world.", title, "...")
    msgBox("Y'know, these days were fun. I'll really miss you.", title, "I'll miss you too.")
    msgBox(("Goodbye, " + name + "."), title, "Goodbye, Hendrix.")
    
    return amity


#MAIN
amity = 0

name = ""

start = True

#main loop
while start:
    amity, name = day1(amity, name)
    amity = day2(amity, name)
    amity = day3(amity, name)
    amity = day4(amity, name)
    amity = day5(amity, name)
    amity = day6(amity, name)
    start = False
    
msgBox("Hello, World!: Complete!", "", "OK")