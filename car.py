import random
import time

attributes = {
    "intelligence": 10,
    "energy":50,
    "weight":15,
    "zoomies":False,
    "divinity":1
}

messeges = {
    1:"""
    List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
    """,
    2:"""
    What would you like to do today?:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    Give Cat Catnip

    """,
    3:"""
    List of Activies:

    Pway with car (vewy coowl [good idyea])
    Fweed car (delicious tweats)
    twaech car (I grow more intellegent every second you wait, I will soon rise from this mortal prison and instigate a reckoning upon your people)
    Put car to sleep (sweepy)
    
    """,
    4:"""
    List of Activies:

    Feed Cat
    Feed Cat
    Feed Cat
    Feed Cat
    Feed Cat 
    Feed Cat
    """,






}

alive = True

name = input("Please name your Cat: ").lower()
name = name.capitalize()
colour = input("What colour is your cat? ").lower()
colour = colour.capitalize()
def status():
    print("Name: ",name)
    print("Colour: ",colour)
    print("Intellegence: ",attributes["intelligence"])
    print("Energy: ", attributes["energy"])
    print("Weight: ", attributes["weight"])
status()

time.sleep(3)

print("""
List of Activies:

    Play with cat
    Feed cat
    Train Cat
    Put cat to sleep
    
Enter [stats] to view cat status
""")

while alive == True:
    cmd = input("\n What would you like to do? ").lower()
    if cmd == "play with cat" or cmd == "play":
        print("You played with ",name," for a while, they seemed to have fun.")
        x = random.randint(1,3) 
        y = random.randint(3,6)
        z = random.randint(1,5)
        d = random.randint(2,3)
        print("Intelligence +",x,"\nEnergy -",y, "\nWeight -",z)
        attributes["intelligence"] + x
        attributes["energy"] - y
        attributes["weight"] - z
        attributes["divinity"] + d
    elif cmd == "feed cat" or cmd == "feed":
        print("You gave",name, "some food, they definatley enjoyed it.")
        x = random.randint(4,8)
        y = random.randint(2,3)
        print("Energy +", x,"\n Weight +",y )
        attributes["energy"] + x
        attributes["weight"] + y
    elif cmd == "train cat" or cmd == "train":
        print("You teach ", name, " some tricks, they appear to thoroughly enjoy it.")
        x = random.randint(3,5)
        y = random.randint(1,4)
        print("Intelligence +",x,"\n Energy -",y)
        attributes["intelligence"] + x
        attributes["energy"] -y
    elif cmd == "put cat to sleep" or cmd == "sleep":
        print("You put ", name," to bed")
        x = random.randint(5,7)
        d = random.randint(2,4)
        print("Energy +",x)
        attributes["energy"] + x
        attributes["divinity"] + d
    elif cmd == "stats" or "status":
        status()
    if attributes["energy"] <= 0:
        print(name, "Has died \n You Lose.")
        alive = False