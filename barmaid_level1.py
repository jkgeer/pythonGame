# -*- coding: utf-8 -*-
character2 = {'Name': 'Bar Maid', 'Gender': 'Female', 'Role': 'Serving alcoholic beverages to the king', 'Location': 'dungeon', 'Level': '1'};

while character2['Level'] == 'barmaid_level1':
	while character2['Location'] == 'Dungeon':
		print "Chapter 1: Breakin' Bad Habits"
		print "As a result of your actions, you’re sent to the dungeon to think about what you've done.\n"
		action = raw_input("What will you do in this dank and lonely cell? Break out or stay dank and lonely?\n")
		if 'Stay dank and lonely' in action:
  			print "If you wish..."
  			import barmaid_level1.py

		if 'Break out' in action:
			print "Excellent!"
		escape = raw_input("...But how will you break out? The way I see it, you have two options. Break down the cell door with your highly reliable beer mug or break the conveniently located window right behind you?\n")
		if 'Break down cell door' in escape:
  			print "Alas, to no avail."
  		
		if 'Break window' in escape:
  			print "Somehow you've managed to break the window quietly enough not to attract any attention from the dungeon guards or your fellow dungeon mates. You escape successfully!\n" 
  		
		location = raw_input("Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the nearby forest, or back to the palace?\n")
		if 'Forest' in location: 
  			print "Onward to the next level!" 
  			import barmaid_level2.py
		if 'Palace' in location:
  			print "What are you doing?! You can't go back there, the King'll have your head for sure!"
  		
  		decision = raw_input("Do you really want to go back?\n")
		if 'Yes' in decision:
  			print "The King spots you sneaking across the grounds while he is on one of his evening strolls. He is merciful and sends you back to the dungeon."
  			import barmaid_level1.py
  		if 'No' in decision:
  			print "Good. I knew you were wiser than that."
    	
    		location = raw_input("Now that you've dusted off shards of glass while remaining unharmed, where will you go? To the nearing forest, or back to the palace?\n")
  		if 'Forest' in location: 
  			import barmaid_level2.py
 
    
  
  
  
  
