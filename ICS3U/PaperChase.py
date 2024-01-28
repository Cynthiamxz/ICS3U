# Text Adventure Game: Paper Chase
# 2022/01/20
# by Cynthia

#based on the coc game scenario Paper Chase


from random import randint


#defining functions:
def roll(dice):
    """Two sets of dice

    Depending on the parameter: 1d100 will introduce a random number between 1 and 100, while 3d6 returns the sum of 3 random numbers between 1-6.
    """
    if dice == "1d100":
        return randint(1, 100)
    elif dice == "3d6":
        dice_roll = randint(1, 6) + randint(1, 6) + randint(1, 6)
        return dice_roll

def investigator():
    """set the value of the player's skills

    Give a random value from 15 to 90 to each of the keys. Returns the dictionary when finished
    """
    skills = {"strength": 0, "constitution": 0, "size": 0, "dexterity": 0, "appearance": 0, "education": 0, "intelligence(idea)": 0, "power": 0}
    for skill in skills:
        skills[skill] = roll("3d6") * 5
    return skills

def skill_check(skill):
    """the function checks if an action is successful

    draw a random integer between 1-100 and compare it with the player's corresponding stat. An action is successful when int < skill point.
    Then it returns the result.
    """
    d100 = roll("1d100")
    print(f".{skill} = {d100}")
    if d100 <= character_sheet.get(skill):
        return True
    elif d100 > character_sheet.get(skill):
        return False




#introduction to the game
print("""You have been contacted by Thomas Kimball of Michigan. 
It seems that his house has been burglarized, ans some of his uncle's favourite books have been stolen.
The mystery is a little unusual, as the uncle inexplicably disappeared without trace a year ago.
You are being asked to investigate the theft of books and to see whether you can shed any light on the disappearance of 
Uncle Douglas Kimball. 
He describes his uncle to you as "balding with white hair, average height, and wearing round spectacles" 
""")
print("""A quick start rule to this game: you will play the role of an private investigator to carry out the missions mentioned 
above. Type in simplified sentences to describe your move; and try to gather as many clues as you can —— they will lead 
you to the end of the story. A dice roll of a number smaller than your stat is a successful roll. 
Good Luck.
""")



#set variables
round = 0 #records the number of actions that the player took
location = 2 #starts at Kimball's house
cemetery_talk = False #haven't talked to the groundskeeper
diary_search = False  #haven't found the diary in Kimball's study
meet_Douglas = False  #turns yes after the player meets Douglas.
tunnel_door = False #tried to open the mausoleum's door?



#creating character sheet
a = investigator()
b = investigator()
c = investigator()

print(f"""a - {a}
b - {b}
c - {c}""") #diplay the possible choices to the player

while True: #Player can choose one of the 3 characters created
    abc = input("Choose one character sheet above to start the game with. ")
    if abc.lower() == "a":
        character_sheet = a
        break
    elif abc.lower() == "b":
        character_sheet = b
        break
    elif abc.lower() == "c":
        character_sheet = c
        break
    else:
        print("invalid answer. ")

print(f"Your investigator's statistics are: {character_sheet}." ) #diaply the final choice



#Start the game
print("""
Start the Game:
You have arrived at Kimball's house yesterday night, and was invited to stay in one of the spare rooms while investigating 
the case. You decide to start your investigation now.""")


while True:
    round += 1
    action = input("\nWhat is your next move? ") #ask for the player's action
    action = action.lower() #re-organize the input into verb, noun


#if the player wasted too much time (rounds)
    if round >= 20:
        print("""[Ending 1] Days has passed since you took this case, but your effort did not pay dividends. Thomas Kimball is disappointed. 
You kept an eye on such a bizarre case even after you left the town. However, the case remains unsolved even after many 
years, and you never met Douglas Kimball.""")


#call out the help menu
    if action == "help": #help menu
        print(" - try to simplify your sentence and use name of places/items that is mentioned in the text")
        print(" - only one action each round")
        print(" - some actions that might take include: go somewhere, talk with an npc, examine a place/item, etc.")


#if the action is to go somewhere:
    elif "go" in action:
        if "west" in action and location <= 1: #go to a direction
            location = 2
        elif "east" in action and location >= 2:
            location = 1

        #go to a specific place: 0-tunnel under cemetery, 1-cemetery, 2-kimball's house, 3-the study
        elif "cemetery" in action:
            location = 1
        elif ("kimball's house" or "study") in action:
            location = 2
        elif ("down" or "tunnel") in action and location == 1: #go down the tunnel in side the mausoleum
            location = 0 #so will not give info about the cemetery again
            meet_Douglas = True
        elif "study" in action:
            location = 3

        else: #unrecognized place/direction
            print("There is nothing over there.")
            continue


#Determines the location of the player
        if location == 0:
            print("""You went down the tunnel. Time has past as you wander around a maze of earthen passages that seem to crisscross the 
cemetery. You grow exhausted in crawling around this underground labyrinth and searching, in vain, for even a suggestion 
for suspicious movements or items. When you decide to leave this tunnel empty handed, you unexpectedly meet a "man" app-
arently on his way up to the surface.""")
        elif location == 1:
            print("""You arrived at the cemetery near Kimball's house. The cemetery is reasonably well tended, although the vegetation is quite 
abundant, with lots of tall bushes and ancient trees dotting the spaces between the gravestones and tombs. It is clear
that the cemetery has been here for many years. There is a gardener who is digging out weeds.""")
        elif location == 2: #Kimball's house
            print("""You are at Kimball's house. Inside the house, Thomas Kimball has moved into all of the rooms except
for the study, which is still cluttered and piled with his uncle's books. """)
        elif location == 3:
            print("You entered Kimball's study.")
        else:
            print("Oops, something went wrong. Please restart the game")
            break #quiting the game


#when the player tries to communicate with a npc
    elif ("talk" or "ask") in action:
        if ("gardener" or "caretaker") in action and cemetery_talk == False : #talk to the caretaker of graveyard
            cemetery_talk = True #player cannot talk with this npc twice
            conversation = skill_check("appearance") #npc only talks to the investigator if he/she looks good
            if conversation == True:
                print("""When the gardener hears your approach, he turns and waves a hello. You learned from him that his name is Melodias Jefferson, 
and he has worked here as the caretaker of the cemetery for over 20 years.
When you ask him about Douglas Kimball, he recalls seeing Douglas regularly in the cemetery and spend time chatting with 
Melodias about all manner of topics, from the weather to politics. He also points out to you Kimball's favorite tombstone,
where he used to always sit on while reading his books.""")
            elif conversation == False:
                print("You try to talk with the gardener,but he seems to be busy with his works and walks away.")

        else:
            print("command not recognized, please try something else.")


#to examine a place or an item——to give a detailed description of a place / item
    elif ("examine" or "search") in action:
        if "kimball's house" in action and location == 2:
            print("""There is nothing special about his house. However, you remembered that Douglas Kimball has a study in this house. Maybe 
you will be able to find some clue over there.""")
        elif "book" in action and location == 3 and diary_search == False: #give details about the books in study
            diary_search = True #cannot search again
            print("""There are books of all shapes and sizes, and on all subjects, identical only in that they were all well cared for. Among 
those books, you found a journal written by Douglas Kimball.""")
            read_diary = skill_check("education")
            if read_diary == True:  #clues are given when the roll is success
                print("""The last entry cryptically mentions "reaching a decision" and "joining with my friends below." In addition, other earlier 
journal entries seem to hint at a network if tunnels beneath the cemetery, inhabited by mysterious creatures that Douglas 
saw moving about in the cemetery at night.""")
            elif read_diary == False:
                print("""The last entry was written before the day Douglas Kimball has vanished. However, you cannot read Douglas' handwriting, ———
they are too scratchy———it seems that the words are scribbled down by its writer whether in a hurry or in excitement""")

        elif "study" in action and location == 3: #details about Douglas' study
            print("""A few books on the shelves are missing, leaving notable spaces. There is no sign of how the burglar gained access to the 
study; the only way into the room would be its door, where you went in, and a window, which is locked by Thomas.""")
        elif ("window" or "lock") in action and location == 3: #examine the window of the study
            print("You notice that the window locks are loose with age, and a determined effort could easily open them from the outside.")
        elif "cemetery" in action and location == 1:
            find_tracks = skill_check("dexterity")
            if find_tracks == True: #clues are given when success
                print("""You quickly walked around the cemetery and examined the place thoroughly.
You notice around one of the tombstones that there are strange tracks on the ground, which look to have been made by man-
sized bare feet that end in cloven hooves rather than toes.""")
            elif find_tracks == False:
                print("""You searched the cemetery in vain. It seems that there is nothing in the graveyard that worth 
your attention""")
        elif ("kimball's favorite tombstone" or "the tombstone") in action and location == 1: #give evidence around Kimball's favourite tombstone
            #no need to roll
            print("""The old tomb has been worn smooth by age and weather, making it a perfect spot to perch and read a book. It's impossible, 
due to the weathering to work out who is buried beneath the tomb.
You notice strange tracks around the tombstone, which look to have been made by man-sized bare feet that end in cloven 
hooves rather than toes.""")
        else:
            print("invalid command, please try something else.")


    elif "follow" in action: #to follow a trace or someone
        if ("the tracks" or "strange tracks") in action and location == 1:  #follow the strange tracks around tombstone
            print("You followed the tracks through the cemetery. They lead you to the door of a mausoleum")
        else:
            print("command not recognized, please try something else.")

    elif "open" in action: #to open something
        if ("the door" or ("door" and "mausoleum")) in action and location == 1 and tunnel_door == False: #open the mausoleum's door
            open_door = skill_check("strength") #if the player can open the door
            if open_door == True: #opens the door
                print("""When you opened the door, a horrible stench is released from within. You find a "hang dug" tunnel leading down below the 
earth inside the mausoleum.""")
            elif open_door == False:
                print("You pulled the door with all your strength, but it remained solid and motionless however hard you tried.")
        else:
            print("command not recognized, please try something else.")

    elif "leave" in action: #leave is not an effective move, must go to a specific place or direction
        print("Where do you want to go?")

    elif ("take" or "pick up") in action: #players cannot take anything in this game
        print("You cannot take anything that does not belong to you.")

    else:
        print("command not recognized, please try something else.")



 #Met Douglas Kimball? Reaches the end
    if meet_Douglas == True:
        print("""Even in the distance, you can sense the abnormality of this strange figure, along with some faint gibbering sound —— th-
ose resembling a beasts'. You find yourself in a dire predicament, in which you are facing a unknown creature who, dete-
rmined by its footsteps that you heard, is much more familiar with this place than you, making you almost impossible to 
make flight. You feel that the figure has already noticed you. You need to hurry up to make a decision!""")

        if ("talk" or "say" or "hi" or "hello") in action: #talk #ending 2
            print("""The figure stops for a brief moment but then heads slowly to the cemetery, as if it is expecting to be followed by you.
Once inside, it makes its way to Douglas Kimball's favorite tombstone and sits down. When you approaches, the figure speaks 
and says, "Hello." Now you get a closer look at its face: it turns out to be a foul-looking humanoid, naked but covered in 
caked mud and mold, whose face is bestial, with large canine teeth and a rudimentary canine-like snout in place of a human 
nose. However, despite the unhuman features, its face has an uncanny resemblance to Douglas Kimball. You realizes that this
ghoul-like figure is actually the missing Douglas Kimball! """)

            print("""Douglas says that he was just too tired of his mundane existence among humans. The only thing he wanted from life was to 
be left alone, able to read whenever he liked, but other humans kept making demands on him. Living as a ghoul, his life 
is great. He does not need money. He does not have to dress for dinner. He does not have to meet people, except at meal-
times. He can read whenever he wants, day or night. But the other ghouls are shutting down this entrance, so he had one 
last night to try and get more of his books before he and they left for good. There is so much to see and experience in 
the world below that he is planning to write his own book about his experiences.
Before he left, he asks you to not reveal to his nephew, Thomas Kimball, that he is still alive. He then creeps inside the
mausoleum and descend into the tunnel.

[Ending 2] You successfully solved the mystery. Although you could not return the stolen books, no one has ever break into 
Kimball's house to steel books since then. Thomas Kimball thanked you for your help and gladly paid you the reward as he 
promised. You left this town with the most wonderful experience that you encountered, thinking that maybe one day, at another 
place of the world, you will meet this wise and mysterious friend again.""")
            break

        elif ("hit" or "shoot" or "fight" or "gun") in action: #trying to fight #ending 3
            print("""[Ending 3] The figure has an incredible strength that does not belong to ordinary humans. You are knocked down by the figure 
and passed out. When you wake up, you find yourself laying on the bed of a hospital. Although you didn't find his uncle and the, the mysterious theft stopped visiting the Kimball's house. Thomas think that
it is you who solved this problem and readily paid you the remuneration. 

You have tried to find the underground tunnel after leaving the hospital,  but its entrance is blocked by earth and stones, 
and you never see that monster-like figure again. """)
            break

        else:
            print("Not working, try something else.")

print("Thank you for playing.")
