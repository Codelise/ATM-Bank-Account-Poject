print("Hello there and welcome to the Codelise game!")
print("Have a wonderful play!")

while True:
    begin = input("""Do you want to play? 
press Y to continue Q to quit """).upper()
    if begin == "Q":
       print("Quitting...")
    elif begin == "Y":       
         print("Loading...")
         break

print("You're lost in the mountains. Suddenly, there was a man approaching you")

player_name = input("""Hello there fellow adventurer!
May I ask what is your name? """)

while True:
    if player_name == player_name:
     print("It's nice to meet you ", player_name, "\nHave fun out there!")
    else:
        print("Enter your name")
    break

def warrior():
    print("You chose to be a warrior.")
    pass

def wizard():
    print("You chose to be a wizard.")
    pass

def assassin():
    print("You chose to be assassin.")
    pass

def marksman():
    print("You chose to be a marksman.")
    pass

role = input("Choose your role (Warrior|Wizard|Assassin|Marksman) ").lower()

if role == "warrior":
   warrior()
   pass
elif role == "wizard":
   wizard()
   pass
elif role == "assassin":
   assassin()
   pass
elif role == "marksman":
   marksman()
   pass
else:
   print("You must chose a role in order to play this game.")


destination = input("""You walk in the woods.
There were two directions, one for SALVATION and one for DEATH  
which would you choose? """).upper()




