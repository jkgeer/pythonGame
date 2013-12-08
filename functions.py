# INTRODUCTION LEVEL 

def player_input (prompt, choices_list):
    player[choice] = player_input("Will you be a female or male in this game?")
    print "Your Choices Are:"
    
choices_list = ['Female', 'Male'];
if choices_list[0] in choices_list:
    print " Oh, you're a girl! You are a bar maid with an attitude. After recently being homeless on the streets of Karflooglesville, you are now working for the royal family. In particular, your duty is to serve the king his favorite alcoholic beverages. Today, the King has gotten sick of your beer-serving abilities. For some reason, you are off your game and he insists that the beverage is simply too flat, it tastes unbearable, and the smell is too sweet for his senses. \n"
    

if choices_list[1] in choices_list:
    print " Oh, a boy I see. So you are a palace scribe who has been working for the King of Karflooglesville for a number of years now. As a young boy, your parents sent you to work for the palace in order to pay for their overdue taxes. The King has grown fond of you, but as of late, the King has been displeased with the notes you've taken because you haven't written enough about him to satisfy his arrogance.\n"

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input
    
#Disregard everything below, I'm testing above
# INTRODUCTION LEVEL 
def player_input(prompt, choices_list):
    player[choice] = player_input("Do you speak up or comply?", ["Speak up", "Comply"]) 
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

# SCRIBE LEVEL 1 
def player_input(prompt, choices_list):
    player[choice] = player_input("What will you do in this dank and lonely cell?", ["Break out", "Stay dank and lonely"])
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

def player_input(prompt, choices_list):
    player[choice] = player_input("Do you turn your quill to the right or the left first?", ["Right", "Left"]) 
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

def player_input(prompt, choices_list):
    player[choice] = player_input("Which door do you choose to leave from? Door one or door two?", ["Door one", "Door two"]) 
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

#BAR MAID LEVEL 1 
def player_input(prompt, choices_list):
    player[choice] = player_input("What will you do in this dank and lonely cell?", ["Break out", "Stay dank and lonely"]) 
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

def player_input(prompt, choices_list):
    player[choice] = player_input("But how will you break out?", ["Break down door", "Break window"])
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

def player_input(prompt, choices_list):
    player[choice] = player_input("Where will you go?", ["Forest", "Palace"]) #Input asking the user if he/she wants to break out of the cell (and thus play the game) or not 
    input =""

    print prompt 
    print "Your Choices Are:"

for choice in choices_list:
    print choice

while input not in choices_list:
    input = raw_input("What is your choice? \n")
    print input

