name = raw_input("Welcome to our Medieval Python RPG. To get this adventure started, please tell me your name.\n") #Input for the user to type his or her name
print " So your name is %s." % name #Print function for responding with the user's name

gender = raw_input("Are you going to be a male or female in this game?\n")#Input to ask the user what his or her gender is

if 'Female' in gender: #If the user is a female...
    	print " Oh, you're a girl! You are a bar maid with an attitude. After recently being homeless on the streets of Karflooglesville, you are now working for the royal family. In particular, your duty is to serve the king his favorite alcoholic beverages. Today, the King has gotten sick of your beer-serving abilities. For some reason, you are off your game and he insists that the beverage is simply too flat, it tastes unbearable, and the smell is too sweet for his senses." #As a female, this is the backstory that will print out
    	answer = raw_input("Do you speak up or comply?\n")#Input to ask the user how he/she will answer the king
    	if 'Speak up' in answer: #If the user speaks up and stands up to the king...
		print "In return, you inform the King that his breath is unbearable and you are sent to the dungeon. The 		King goes into a rage and send you to solitary confinement."#After speaking up, this is the 					response that will be printed out
		import barmaid_level1.py #After being sent to the dungeon, Level 1 of the Bar Maid's version of the game 		will be imported 
	if 'Comply' in answer: #If the user complies and does not defy the king...
		print "Really? You will let such a defiant moment pass?" #After complying, this is the response that 			will be printed out
		import intro.py #After complying, the user will be forced to restart the "Intro" portion of the game

	
if 'Male' in gender: #If the user is a male...
        print " Oh, a boy I see. So you are a palace scribe who has been working for the King of Karflooglesville for a number of years now. As a young boy, your parents sent you to work for the palace in order to pay for their overdue taxes. The King has grown fond of you, but as of late, the King has been displeased with the notes you've taken because you haven't written enough about him to satisfy his arrogance.\n" #As a male, this is the backstory that will print out
	answer = raw_input("Do you speak up or comply?\n") #Input to ask the user how he/she will answer the king
	if 'Speak up' in answer: #If the user speaks up and stands up to the king...
		print " The King goes into a rage and send you to solitary confinement." #After speaking up, this the 			response that will be printed out
		import scribe_level1.py #After being sent to the dungeon, Level 1 of the Scribe's version of the game 			will be imported
	if 'Comply' in answer: #If the user complies and does not defy the king...
		print "Really? You will let such a defiant moment pass?" #After complying, this is the response that 			will be printed out
		import intro.py #After complying, the user will be forced to restart the "Intro" portion of the game

	
	
	


