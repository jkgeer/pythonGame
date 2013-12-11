Contributing to the Karflooglesville Quest for Adventure {#welcome}
=====================

How to contribute?
---------

A basic and easy way for you to keep uniformity with the standard our code has set would just be to look at the raw code itself.
Assuming you don't have access to do that, just know that our levels are each individual files that will pull upon each other to advance or
sometimes regress a user's adventure. To that end, just make sure if you're advancing or progressing levels, you try to 
keep a similar level name ot ours.

In addition, this program makes use of 'for/while' loops to cut down on repetitive code and account for users input a wrong choice. An example of this is
as follows:

  "player_input(prompt="Do you swing your fist left or right?", choice1='Left', choice2='Right') #Prompt for user input        
   fistchoices=['right', 'left']
   response=raw_input('What is your choice?')
        
   while (response).lower() not in fistchoices:#User chooses Right or inputs incorrectly
      print" "
      print "Incorrect input.  Try again."
   if (response).lower() in fistchoices[0]: #User chooses Left
      print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
      import barmaid_level3.py #Move to next level
   if (response).lower() in fistchoices[1]: #User chooses Left
      print "Congratulations, you have killed the beast! Your savior comes and gives you a kiss for saving his village.  He says he is forever in your debt. You two fall in love, and get happily married!  You are deemed a hero in the eyes of the village and everyone is happy for your marriage, even the blacksmith!"
      import barmaid_level3.py"
      
Finally, we use data dictionaries to account for our possible choices, so please start each level with the following:

"def player_input(prompt, choice1, choice2):
        print "Prompt: ", prompt;
        print "Choice 1: ", choice1;
        print "Choice 2: ", choice2;"
