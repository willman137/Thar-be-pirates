import random
import time
def locations(): 
    docks= [1,1]
    harbor = [1,2]
    tavern = [2,1]
    dockyards = [2,2]
    marketSouth = [3,1] 
    marketNorth = [3,2]
    oldTown = [4,1]
    nobleHousing =[4,2]


def gameOver():
    print("Well, this be the end of the tale of" , name, "the", yePath) 
    print("Want to play again matey?")

    playAgain = input()

    if playAgain== "yes" or "Yes" or "Y" or "y" or "yar" or "si":
        tharBePirates()

    if playAgain == "no" or "No" or "n" or "N" or "nope" or "nay" or "avast":
        input()
    else:
        print("say again matey?")

def cityName(name):
    selection = random.randint(1,4)

    if selection == 1:
        name = "Tortuga"
    if selection == 2:
        name = "Resolute Bay"
    if selection == 3:
        name = ""

    return name

def shipName():

    shipChoice = random.randint(1,3) 
    if shipChoice == 1:
        shipName = "The Bootlegger"

    if shipChoice == 2:
        shipName = "SSV Gottam"

    if shipChoice == 3:
        shipName = "Chargin Targe"
    return shipName

    print("now's the time ye should travel to the docks matey, I heard a ship be ready for ye")

    if playerLocation == [1,1] or playerLocation == docks:
        print("Ye be at the docks, with the", shipName, " being in port to the left of ye.")
        print("so now ye say goodbye to the fair city of" , cityName, "and Raise the sails,")
        print("ye get out of the docks and out of the harbor,")                  
        time.sleep(1)
        ending = random.randint(1,3)
        if ending == 1:
                print("and ye set sail for the new world, plunderin' about whether or not to pillage")               

def getDirection():
    print("where would you like to go?")
    dir1 = str(input())
    return dir1

def avast():
        print("""

     ______                                                   __               ___   
    / \\  _     \                                                  / \\ \__       /\\\    \\    
    \\  \\ \L\   \     __  __       ____           ____   \    \ ,_\      \\ \\    \\   
     \\  \\  __   \  / \  \/\   \   /'    __ `\        / ,__  \  \   \ \ /        \\ \\    \\
      \\  \\ \  / \  \ \  \  \_/  | \  \   \L\.  \ _   / \__, `\   \  \ \_         \\ \\ _ \\
       \\  \\_\   \_\ \  \___ /   \  \ __\/. \ _\  \/\____/    \  \__\        \\ /\\_ \\
        \\ /_/\\ /_/   \/__  /      \ /__/\  /__/   \/___/       \ /__/          \\/__/

            """)
        print()

def pirateslogo ():
        print("""

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+                                                                                                                  +
+                                                                                                                  +
+                                                                                                                  +
+                                     PIRATES BE EVERYWHERE!!!                               +
+                                                                                                                  +
+                                                                                                                  +
+                                                                                                                  + 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

    """)
        print()


def tharBePirates():

    while True:
        locations() 
        endGame = 1
        x = 1
        y = 1


        print("AVAST SCUMBAGS! Thar be pirates everywhere ye may be!")
        time.sleep(1)
        print("What be yer name?")

        name = input()
        print("Alright" , name, "let me tell ye a tale of the olden days, wher..")
        time.sleep(1)

        print("AVAST!! There be an important question missing an answer!")
        time.sleep(1)
        print ("What ber yer favorite number matey, of one to four?")

        yeChoice = int(input())


        yePath = "Land Lubber"
        yeStory = "Blank parchment"
        yeSpawn = [0,0]

        p1 = "dummy"
        p2 = "dummy"
        p3 = "dummy"
        n1 = "bad-dummy"
        perkList=[p1,p2,p3,n1]

        if yeChoice == 1:
            yePath= "Street urchin"
            yeStory="A Beggers Rant"

            perkList[0]="Light hands"
            perkList[1]="Beggars charm"
            perkList[2]="Tunnel runner"
            perkList[3]="Scrawny shrimp"


        if yeChoice == 2:
            yePath ="Captian"
            yeStory = "Captians Log: Where be us now?"

            perkList[0]="Captians Charisma"
            perkList[1]="Aura of loyalty"
            perkList[2]="Buckaneer"
            perkList[3]="Down with ye ship"


        if yeChoice == 3:
            yePath = "Noble"
            yeStory = "The Kicker of peasants"

            perkList[0]="Clean Hands?"
            perkList[1]="Sneering Imperialist"
            perkList[2]="Rich"
            perkList[3]="Overly Pampered"


        if yeChoice == 4:
            yePath = "Pirate"
            yeStory= "Pirates tale"

            perkList[0]= "Swashbuckler"
            perkList[1]="Plunder of Treasure"
            perkList[2]="Ya Har Mateys!"
            perkList[3]="Rum Breath"


        if yeChoice==5:
            yePath =="Super Secret Awesome!"
            yeStory == "Secret story"
        
#this is where the game fills you in on a bit of a prologue
        print("Duly noted")
        time.sleep(1)
        print("Alright, now was eyeh?....Oh yes the tale!")
        time.sleep(1)
        print("the tale where pirates ruled and fought over the seven seas,")
        time.sleep(1)    
        print("pillaged towns and raided fair maidens (they be ships, we be polite to our wenches)")
        time.sleep(1)
        print("but this be no ordinary tale of the seas, oh no,")
        time.sleep(1)
        print("this be one of them choose yer own adventure tales")
        time.sleep(1)
        print("this be the tale where:")

        time.sleep(2)

        pirateslogo ()

        time.sleep(2)


        if yePath == "Captian" or yePath == "Pirate":
            playerLocation = [1,1]

        if yePath == "Street Urchin":
            playerLocation = [2,1]

        if yePath == "Noble":
            playerLocation= [4,2]

        print("So, ye be a" , yePath, "In this fair tale.")
        wall= [ [0,0] , [1,0] , [2,0] , [3,0] , [4,0] , [5,0] , [5,1] , [5,2] , [5,3] , [4,3] , [3,3] , [2,3] , [1,3] , [0,3] , [0,2] , [0,1] ]
        treasure = 0
        while treasure <= 5:
            direc = getDirection()

            if direc == "North" or direc == "north":
                y = y + 1
                playerLocation = [x,y]
                treasure = treasure +1
            if direc == "East" or direc ==  "east":
                x = x + 1
                playerLocation = [x,y] 
                treasure = treasure +1

            if direc == "South" or direc ==   "south":
                y = y - 1
                playerLocation = [x,y] 
                treasure = treasure +1

            if direc == "West" or direc ==  "west":
                x = x - 1
                playerLocation = [x,y] 
                treasure = treasure +1

            if direc == "North" and playerLocation in wall or direc == "north" and playerLocation in wall:
                print("ye can't head that way,so ye turn around and head back to you where ye were before.")
                y = y -1
                playerLocation = [x,y]

            if direc == "South" and playerLocation in wall or direc == "south" and playerLocation in wall:
                print("ye faceplant a wall matey, ye and are where you were before turn about.")
                y = y +1
                playerLocation = [x,y]

            if direc == "East" and playerLocation in wall or direc == "east" and playerLocation in wall:
                print("ye faceplant a wall matey, ye and are where you were before turn about.")
                x = x -1
                playerLocation = [x,y]

            if direc == "West" and playerLocation in wall or direc == "west" and playerLocation in wall:
                print("ye faceplant a wall matey, ye and are where you were before turn about.")
                x = x + 1
                playerLocation = [x,y]


            if direc == "chart" or "map"  or "where?":
                print (str(playerLocation))


            if direc != "North" and direc != "north" and direc != "East" and direc != "east" and direc != "South" and  direc != "south" and  direc != "West" and  direc != "west" and direc != "where am I" and direc != "chart" and  direc !="where?":
                playerLocation = [x,y]
                print("please say again?")
            

            if treasure == 5:
                break

        print("now ye should head back to the docks, seeing as how ye have enough treasure to overfill a pile of chests")
        while playerLocation != [1,1]:
            getDirection()


            if playerLocation == [1,1]:      
                finalTale()                
                endGame == endGame -1
   
            if endGame == 0:
                gameOver()
        else:
            getDirection

tharBePirates()


