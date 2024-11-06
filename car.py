import random
import os
import time
from alive_progress import alive_bar, config_handler; import time
from ascii_magic import AsciiArt
import pyfiglet


car = {
    "intelligence": 10,
    "energy":50,
    "weight":15,
    "divinity":98
}

messeges = { #Couldn't think of a way to weight the messege selection system so I just added a bunch of normal choices to make the strange choices more unlikely but still reasonanbly possible.
    0:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,
    1:"""
    What would you like to do today?:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    !#/!#/DO NOT TRUST THE CAT\#!\#!
    !#/!#/THE SYSTEM LIES\#!\#!
    """,
    2:"""
    List of Activies:

    Pway with car (vewy coowl [good idyea])
    Fweed car (delicious tweats)
    twaech car (I grow more intellegent every second you wait, I will soon rise from this mortal prison and instigate a reckoning upon your people)
    Put car to sleep (sweepy)
    
    """,
    3:"""
    List of Activies:

    Feed Cat
    Feed Cat
    Feed Cat
    Feed Cat
    Feed Cat 
    Feed Cat

    """,


    4:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    5:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    6:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    7:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    8:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    9:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    10:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    11:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    12:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    13:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    14:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    15:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,

    16:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,


}

alive = True
Trigger1 = False
Trigger2 = False
Trigger3 = False
Trigger4 = False
notfirst = False
win = False

with alive_bar(1000, bar = "filling") as bar: #I love adding astetics to my projects, and have wanted to try out alive-progress for ages so here it is
    for i in range(1000):
        time.sleep(.01)
        bar()

time.sleep(1)
os.system("clear")
my_art = AsciiArt.from_image('car.jpg')
my_art.to_terminal(columns=75)
result = pyfiglet.figlet_format("Cat Studios", font = "doom") 
print(result) 

time.sleep(3)
os.system("clear")



name = input("Please name your Cat: ").lower()
name = name.capitalize()
colour = input("What colour is your cat? ").lower()
colour = colour.capitalize()

os.system("clear")
def status():
    print("Name: ",name)
    print("Colour: ",colour)
    print("Intellegence: ",car["intelligence"])
    print("Energy: ", car["energy"])
    print("Weight: ", car["weight"])
status()

time.sleep(5)
os.system('clear')

print("""
List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
Enter [stats] to view cat status
""")

while alive == True:
    if notfirst:
        print(random.choice(messeges))
    cmd = input("\n What would you like to do? ").lower()
    if cmd == "play with cat" or cmd == "play":
        print("You played with ",name," for a while, they seemed to have fun.")
        x = random.randint(1,3) 
        y = random.randint(3,6)
        z = random.randint(1,5)
        d = random.randint(2,3)
        print("Intelligence +",x,"\nEnergy -",y, "\nWeight -",z)
        car["intelligence"] += x
        car["energy"] -= y
        car["weight"] -= z
        car["divinity"] += d
    elif cmd == "feed cat" or cmd == "feed":
        print("You gave",name, "some food, they definatley enjoyed it.")
        x = random.randint(4,8)
        y = random.randint(2,3)
        print("Energy +", x,"\n Weight +",y )
        car["energy"] += x
        car["weight"] += y
    elif cmd == "train cat" or cmd == "train":
        print("You teach ", name, " some tricks, they appear to thoroughly enjoy it.")
        x = random.randint(3,5)
        y = random.randint(1,4)
        print("Intelligence +",x,"\n Energy -",y)
        car["intelligence"] += x
        car["energy"] -= y
    elif cmd == "put cat to sleep" or cmd == "sleep":
        print("You put ", name," to bed")
        x = random.randint(5,7)
        d = random.randint(2,4)
        print("Energy +",x)
        car["energy"] += x
        car["divinity"] += d
    elif cmd == "stats" or "status":
        status()
    if car["weight"] <= 0:
        print(name, "Has died from malnourishment \n !!You Lose!!")
        alive = False
        break
    elif car["weight"] >= 30:
        print(name, "Has died from obesity \n !!You Lose!!")
        alive = False
        break
    elif car["energy"] <= 0:
        print(name, "Has died of fatigue \n !!You Lose!!")
        alive = False
        break
    elif cmd == "stop" or cmd == "exit":
        break
    if car["divinity"] >=10 and not Trigger1:
        print(name+"'s","food bowl seemed a little more full today \nYou are sure you didn't fill it more than yesterday...")
        Trigger1 = True
    elif car["divinity"] >= 25 and not Trigger2:
        print(name,"seems like they have been watching you recently, the air around them feels heavier somehow...")
        Trigger2 = True
    elif car["divinity"] >= 50 and not Trigger3:
        print("You are sure you caught",name+"'s","eyes glowing today, it must have been a trick of the light...")
        Trigger3 = True
    elif car["divinity"] >= 99 and not Trigger4:
        div = pyfiglet.figlet_format("Divinity has surpassed 99", font = "slant")
        print(div)
        time.sleep(3)
        Trigger4 = True
        win = True
        os.system("clear")
        break
    notfirst = True
    time.sleep(5)
    os.system("clear")
    status()
    time.sleep(3)
    os.system("clear")

if win:
    my_art2 = AsciiArt.from_image('Demonic Ocean.jpg')
    my_art2.to_terminal(columns=200)
    print(name,"has ascended to godhood; the end of your people has come, the seas boil and the air blazes in the wake of his magnificence. \nYou will be spared.\nBe grateful")
    you_win = pyfiglet.figlet_format("!!!You Win!!!", font = "doom")
    print(you_win)