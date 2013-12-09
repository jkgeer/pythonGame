import functions.py
print "Welcome to Chapter 2: The Forest of Love!" 
print " "
print "You have successfully escaped from your cell! But you are being chased by the palace guards. You run for your life and end up crashing into a handsome lad."
print " "
player_input(prompt="You give him a terrible gash across his thigh.  He is tearing up from the pain.  Will you heal cut with magical beer mug or give him an angry look?", a=
pain_response = raw_input("You give him a terrible gash across his thigh.  He is tearing up from the pain.  Will you " + "\"heal cut with magical beer mug\"" + ' or '+ "\"give him an angry look\""+'?')
if 'heal cut with magical beer mug' in pain_response:
	print " "
	print "He says thank you and asks why you, the bar maid, is running through the forest. You reply and say that you are running from the palace guards because you defied the king.  He then provides refuge for you in return for you healing him.  As you begin conversing to better know your savior, he tells you of the beast that has been tormenting his village.  He believes that you can do something about the beast since you have magic!  He looks at you with a desperate look."
	print " " 
	beast_response = raw_input("Will you " + "\"choose to ignore story\"" + ' or '+ "\"do something about the beast\""+'?')
	if 'choose to ignore story' in beast_response:
		print " "
		print "You ignore his desperate look and change the topic with an embarassed look.  He gives you an understanding look and proceeds to give you blankets and bids you good night. The next morning, you wake before your savior does and you leave his village."
		print "import scribe_level3.py"   
	if 'do something about the beast' in beast_response:
		print " "
		print "You proceed to tell him you will do what you can to protect his village.  He exclaims with appreciation and gives you a hug.  He embarassingly thanks you and leads you to the blacksmith to help you fight the beast.  You greet the blacksmith.  The blacksmith grunts, looks you over, and laughs.  He underestimates you and proceeds to say that a lady cannot defeat the village beast.  Your savior persuades the blacksmith that because you have magic, you can defeat the beast."
		print " "		
		blacksmith_response = raw_input("He reluctantly asks you what you would prefer, " + "\"suit of armor\"" + " or " + "\"spiked hammer\""+"?")
		if 'suit of armor' in blacksmith_response:
			print " "			
			print "The blacksmith laughs, creates a suit of armor for you, and you can barely walk.  The blacksmith laughs as you fall to the ground and continues to laugh at your failure.  He bids you good luck and you slowly leave the blacksmith.  You travel to the cave where the beast is located."
			print " "			
			cave_response = raw_input("Do you" + "\"enter the cave bravely\"" +" or "+ "\"hesitate\"" +"?")
			if 'enter  the cave bravely' in cave_response:
				print " "				
				print "You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.  The fireball hits your armor and you get flung backwards.  You get up as fast as you can in the heavy suit of armor.  You ball up your armored fist." 
				print " "				
				swing_response = raw_input("Do you "+'\'swing left\''+' or '+'\'swing right\''+'?')
				if 'swing left' in swing_response:
					print " "					
					swing2_response = raw_input("Yikes, you missed the beast.  Looks like you have to swing again.")
					if 'swing left' in swing2_response:
						print " "
						print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
						print " "
						chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:	
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
					if 'swing right' in swing2_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!'  
						print " "
						chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
			if 'hesitate' in cave_response:
				print " "
				print "While you hesitate, the beast comes out of the cave and claws your armor.  You have a gash across your chest from the blow.  Your armor is in shards of metal beside you. You take a shard of metal and use it as a weapon."
				weapon_response=raw_input("Do you use the shard of metal as a" + '\' sword\'' + ' or a ' + '\'throwing weapon\''+'?')
				if 'sword' in weapon_response:
					print " "
					print "You use the metal shard as a sword.  As you swing left and right, the beast comes closer and closer.  You use the sword to deflect the fire the beast is blowing your way.  With your last ounce of strength, you thrust the metal shard into the beast.  You have killed the beast!"
					print " "
					print "Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!"  
					print " "
					chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
					if 'yes' in chapter3_response:
						import scribe_level3
					if 'no' in chapter3_response:
						print " "
						print 'You have ended the game!'
				if 'throwing weapon' in weapon_response:
					print " "
					print "You use the metal shard as a throwing weapon. Since you have so many metal shards, you throw furiously at the beast.  The beast is dodging all of your shards!  As you come down to your last metal shard, you throw with all of your might.  The shard hits the beast's eye, and the trauma kills the beast!"
					print " "
					print "Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!"  
					print " "
					chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
					if 'yes' in chapter3_response:
						import scribe_level3
					if 'no' in chapter3_response:
						print " "
						print 'You have ended the game!'
		if 'spiked hammer' in blacksmith_response:
			print " "
			print 'The blacksmith smiles, creates a spiked hammer of magestic proportions, and gives it to you.  He calls you brave and bids you good luck.  You leave the blacksmith and travel to the cave where the beast is located.'
			print " "
			cave1_response = raw_input("Do you" + "\"enter the cave\"" +" or "+ "\"hesitate\""+"?")
			if 'enter the cave' in cave1_response:
				print " "
				print 'You walk into the dark cave.  You hear growling and all of a sudden, a fireball rushes your way.   You quickly dodge out of the way.  In your action of dodging, you lost your spiked hammer in the dark!  You frantically search for it in the dark but you cannot find it. You decide to use your magical beer mug and you quickly pull it out.  It is too dark to see where the beast is.' 
				print " "
				wave_response=raw_input('Will you wave your beer mug'+'\'left\'' +' or '+'\'right\''+'?')
				if 'right' in wave_response:
					print " " 
					wave2_response=raw_input('Yikes, you missed the beast.  Looks like you have to wave again.')
					if 'right' in wave2_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or '+ '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
					if 'left' in wave_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'  
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
				if 'left' in wave_response:
						print " "
						print 'Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village  and everyone is happy for your marriage!'  
						print " "
						chapter3_response=raw_input('Would you like to continue to chapter 3,' + '\' yes\'' + ' or ' + '\'no\''+'?')
						if 'yes' in chapter3_response:
							import scribe_level3
						if 'no' in chapter3_response:
							print " "
							print 'You have ended the game! Congratulations hero!'
			if 'hesitate' in cave_response:
				print " "
				print "While you hesitate, the beast comes out of the cave and claws you across your chest.  You frantically grab your spiked hammer and swing it furiously at the beast, however, the beast is not fazed and becomes even stronger as it adapts to your blows.  You decide to use your hammer and the magic from your beer mug."
				weapon_response=raw_input("Do you use the magical hammer as a" + '\' offensive weapon\'' + ' or a ' + '\'defensive weapon\''+'?')
				if 'offensive weapon' in weapon_response:
					print " "
					print "You use the magical hammer as a offensive weapon.  As you swing left and right, the beast comes closer and closer.  You use the hammer to hit the beast. You fight back and forth.  With your last blow to the beast, you swing with all your strength and kill the beast!"
					print " "
					print "Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!"  
					print " "
					chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
					if 'yes' in chapter3_response:
						import scribe_level3
					if 'no' in chapter3_response:
						print " "
						print 'You have ended the game!'		
				if 'defensive weapon' in weapon_response:
					print " "
					print "You use the magical hammer as a shield. You manage to deflect each fire blow from the beast.  As the beast runs out of breath from his firebreathing, you aim the shield directly at the beast.  As the beast breathes fire your way, the fire is deflected right back towards him and the beast is killed!"
					print " "
					print "Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage even the blacksmith!"  
					print " "
					chapter3_response=raw_input("Would you like to continue to chapter 3," + '\' yes\'' + ' or ' + '\'no\''+'?')
					if 'yes' in chapter3_response:
						import scribe_level3
					if 'no' in chapter3_response:
						print " "
						print 'You have ended the game!'
else:
	print "He says " +"\"HMPH\""+" and brushes himself off, wipes away the tears of pain, and walks away angrily."
	print " "
	print "Because you chose to be a terrible person and let a handsome lad walk away without apologizing, you get caught by the palace guards and get returned to the palace!"
	print " "
	chapter3final_response=raw_input('Would you like to continue to the next chapter?')
	if 'yes' in chapter3final_response:
		import scribe_level3
	if 'no' in chapter3final_response:
		print " "
		print 'You have ended the game!'
