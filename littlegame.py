print "You enter a dark room with two doors. Do you go through door #1 ,door #2 or door #3?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")
    if bear == "1":
        print "The near eats your face off. Good for you!" 
    elif bear == "2":
        print "The bear eats your legs off. Again good for you!"
    else:
        print "Well, doing %s is probably better. Bear runs away." %bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. YOU WIN!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

elif door == "3":
    print """
    You are in the shadows. You most certainly believe that you are lost,
    but there is nothing that you can do. One day all of this garbage 
    goes straight to hell and you have to go down with it. One day you can't 
    even remember; that's the day that you will die, for real and this time;
    forever."""
    print "1. Kill yourself."
    print "2. Go on!"
    
    youdecide = raw_input("> ")
    
    if youdecide == "1":
        print "Good choice. See you in hell!"
    elif youdecide == "2":
        print "Bruh, you better thing again."
    else: 
        print "COWARD!"
    


else: 
    print "You stumble around and fall on a knife and die. Good job"
    