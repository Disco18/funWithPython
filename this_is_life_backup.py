import sys
import time
    
# Start game scene
#----------------------------------
#The lists are the words the player can type in the input fields so the computer can workout with path they are taking.
noList = ["No","NO","n","N","na","NA","no","Na","Nope"," ","nope",""]
yesList = ["YES","Yes","yes","y","Y","ye","Ye","YE","Yep","YEP"]
instructionsList = ["instructions", "Instructions", "aim", "Aim", "INSTRUCTIONS"]
startList = ["Start", "start", "go", "START", "sTART"]
question_group = ["guess","Guess","GUESS","Code","code","CODE"]
code = str(5858)
smart_test = str(17.35 + 1.20)
sys.stdout.write("\nAll artwork is from https://www.asciiart.eu/\n")
#Where the ascii art work is copied from.
sys.stdout.write("""
 /$$      /$$           /$$                                             /$$ /$$
| $$  /$ | $$          | $$                                            | $$| $$
| $$ /$$$| $$  /$$$$$$ | $$  /$$$$$$$  /$$$$$$  /$$$$$$/$$$$   /$$$$$$ | $$| $$
| $$/$$ $$ $$ /$$__  $$| $$ /$$_____/ /$$__  $$| $$_  $$_  $$ /$$__  $$| $$| $$
| $$$$_  $$$$| $$$$$$$$| $$| $$      | $$  \ $$| $$ \ $$ \ $$| $$$$$$$$|__/|__/
| $$$/ \  $$$| $$_____/| $$| $$      | $$  | $$| $$ | $$ | $$| $$_____/        
| $$/   \  $$|  $$$$$$$| $$|  $$$$$$$|  $$$$$$/| $$ | $$ | $$|  $$$$$$$ /$$ /$$
|__/     \__/ \_______/|__/ \_______/ \______/ |__/ |__/ |__/ \_______/|__/|__/
""")
sys.stdout.write("\nTo 'This is Life', This is your story, please read all lines carefully as it will impact your story and how far you will make it! PS: It is recommended you use light mode to see the art correctly.")
#In this statement we are allowing the player to choose if they would like instructions or want to just pass and start the game.
instructions = input("\nIf you're looking for the instructions on how to play the game or what the aim of the game is please type 'Instructions' and hit the enter key or to continue please hit the enter key.\n")
if instructions in instructionsList:
    sys.stdout.write("Your job is to get through the story as far as you can making the choices you want. However, if you kill the program you have failed!\nIf you go down the wrong path you have the potential to die resulting in a fail. Note you can not go back without restarting. Good luck and survive as long as you can!")

answer = input("\nTo start the game please type 'start', Good Luck!\n")
if answer in noList:
    exit()


#Meeting scene with player
#----------------------------------
sys.stdout.write("Someone is walking towards you...")
time.sleep(3)
#Time.sleep delays the next line of code by (4) seconds simulating the walking
sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.    ,       /   
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug

""")

sys.stdout.write("Hey there my name is Bug, what is yours?\n")
#Reads the players input as their name.
players_name = sys.stdin.readline()
time.sleep(2)
sys.stdout.write("Mmm it's great to finally meet you " + players_name)
time.sleep(2)
sys.stdout.write("I have a smart test for you, do you know what 17.35 plus 1.20 equals?\n")
#the below if statement returns different responses depending on the user being able to calulate the correct answer.
count = input("")
if count > smart_test:
    sys.stdout.write("You're not very smart are you..\n")
    time.sleep(1)
    sys.stdout.write(smart_test + " is the correct answer\n")
elif count < smart_test:
    sys.stdout.write("You're not very smart are you..\n")
    time.sleep(1)
    sys.stdout.write(smart_test + " is the correct answer\n")
else:
    sys.stdout.write("Wow! You are really smart\n")
    time.sleep(1)
    sys.stdout.write("I didn't think anyone would get " + smart_test)

#The input and if statement below is asking the player their age and responding if they are old enough to help or not.
first_response = input("\nSay do you think you could help me with a problem please? (yes/no)\n")
if first_response in yesList:
    sys.stdout.write("Awh thank you so much, ive been struggling to find someone to help! \nFirst we will need to get to know you better..\n")
    sys.stdout.write("How old did you say you were?\n")
    players_age = sys.stdin.readline()
    if players_age >= (str(18)) and players_age <= (str(41)):
        sys.stdout.write("Mhmm " + players_age + "That should be old enough!\n")
        time.sleep(2)
        sys.stdout.write("Please follow me, I'll take us to my house\n")
        time.sleep(2)
        sys.stdout.write("You begin walking with Bug...\n")
        time.sleep(3)
        sys.stdout.write("... ... .....\n")
        time.sleep(4)
        sys.stdout.write("... ... ... still walking ...\n")
        time.sleep(3)
        sys.stdout.write("... ... .....\n")
        time.sleep(3)
        sys.stdout.write("Ah here we are! Sorry about the long walk, there's my house over there! *Bug points ahead*\n")
        time.sleep(3)
        sys.stdout.write("""\

             (
                )
            (            ./\.
         |^^^^^^^^^|   ./LLLL\.
         |`.'`.`'`'| ./LLLLLLLL\.
         |.'`'.'`.'|/LLLL/^^\LLLL\.
         |.`.''``./LLLL/^ () ^\LLLL\.
         |.'`.`./LLLL/^  =   = ^\LLLL\.
         |.`../LLLL/^  _.----._  ^\LLLL\.
         |'./LLLL/^ =.' ______ `.  ^\LLLL\.
         |/LLLL/^   /|--.----.--|\ = ^\LLLL\.
       ./LLLL/^  = |=|__|____|__|=|    ^\LLLL\.
     ./LLLL/^=     |*|~~|~~~~|~~|*|   =  ^\LLLL\.
   ./LLLL/^        |=|--|----|--|=|        ^\LLLL\.
 ./LLLL/^      =   `-|__|____|__|-' =        ^\LLLL\.
/LLLL/^   =         `------------'        =    ^\LLLL\
~~|.~       =        =      =          =         ~.|~~
  ||     =      =      = ____     =         =     ||
  ||  =               .-'    '-.        =         ||
  ||     _..._ =    .'  .-58-.  '.  =   _..._  =  ||
  || = .'_____`.   /___:______:___\   .'_____`.   ||
  || .-|---.---|-.   ||  _  _  ||   .-|---.---|-. ||
  || |=|   |   |=|   || | || | ||   |=|   |   |=| ||
  || |=|___|___|=|=  || | || | ||=  |=|___|___|=| ||
  || |=|~~~|~~~|=|   || | || | ||   |=|~~~|~~~|=| ||
  || |*|   |   |*|   || | || | ||  =|*|   |   |*| ||
  || |=|---|---|=| = || | || | ||   |=|---|---|=| ||
  || |=|   |   |=|   || | || | ||   |=|   |   |=| ||
  || `-|___|___|-'   ||o|_||_| ||   `-|___|___|-' ||
  ||  '---------`  = ||  _  _  || =  `---------'  ||
  || =   =           || | || | ||      =     =    ||
  ||  %@&   &@  =    || |_||_| ||  =   @&@   %@ = ||
  || %@&@% @%@&@    _||________||_   &@%&@ %&@&@  ||
  ||,,\\V//\\V//, _|___|------|___|_ ,\\V//\\V//,,||
  |--------------|____/--------\____|--------------|
 /- _  -  _   - _ -  _ - - _ - _ _ - _  _-  - _ - _ \
/____________________________________________________\
""")
        time.sleep(2)
        sys.stdout.write("\nSo what do you think? haha, not bad if I say so myself\n")
        time.sleep(2)
        sys.stdout.write("Please come inside...\n")
        time.sleep(2)
        sys.stdout.write("You both begin to walk towards the door, *You see Bug reach into his pocket* when he turns to you\n")
        time.sleep(3)
        sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.    ,       /   
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
""")
        sys.stdout.write("Well this is awarkward.. I seem to have left my keys inside and the only other way in, is this keypad but I can't remember my passcode...\n")
        time.sleep(2)

#Start to making the player help break the code for the house
#----------------------------------
        second_response = input("Do you think you would be able to figure it out for me (yes/no)\n")
        if second_response in yesList:
            sys.stdout.write("Thank you so much, I knew I could count on you!\n")
            time.sleep(2)
            sys.stdout.write("You walk up to the keypad and take a look to see what you are dealing with..\n")
            time.sleep(4)
            sys.stdout.write("""

  ,&*.................*@,    ,&*.................*&*    ,&*.................*&, 
 **                     ,/  */                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **          &&#        ,/  **       .@&(%&/       ,/  **       *&#,&&,       ,/
 **        /  @#        ,/  **           /&(       ,/  **          &@#        ,/
 **          .&(        ,/  **         &&(         ,/  **            @@       ,/
 **          .&#        ,/  **       (&@@@@&       ,/  **       .&&@@&        ,/
 **                     ,/  **                     ,/  **                     ,/
 .(                     /,  ,(                     /*  ,(                     /*
   ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*  
                                                                                
  .&(*****************(&.    .&(*****************(&,    .&(*****************(&, 
 **                     ,/  */                     */  */                     */
 **                     ,/  **                     ,/  **                     ,/
 **          &&&        ,/  **        #&@@@,       ,/  **        ,&@&@&       ,/
 **        /&,@&        ,/  **       .&&@@(        ,/  **       .&&,#(        ,/
 **       &&((&&(       ,/  **           .&#       ,/  **       .&@. .&&      ,/
 **           @&        ,/  **        #@@@(        ,/  **        (&%*%&/      ,/
 **                     ,/  **                     ,/  **                     ,/
 ,(                     /*  ,(                     **  ,(                     **
   (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#  
                                                                                
  /%.                 .#/    /%.                 .#(    *%.                 .#( 
 **                     ,/  **                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **       (&&%&&/       ,/  **       ,&# (&,       ,/  **       *&#.&@        ,/
 **          &%         ,/  **        /@@@(        ,/  **       /&* /&&       ,/
 **         &&          ,/  **       #&. .&%       ,/  **         ...&%       ,/
 **        .%*          ,/  **        #@@@%        ,/  **        (@@&,        ,/
 **                     ,/  **                     ,/  **                     ,/
 .%                     #,  ,#                     (,  .%                     (,
   .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.  
                                                                                
  ,%,.................,&*    ,%,.................,%*    ,&*.................,%* 
 **                     ,/  **                     */  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **     *&&#   #&@*     ,/  **       .@&,%@,       ,/  **            *&&.     ,/
 **        %&@&%        ,/  **       #&* ,&%       ,/  **           &&#       ,/
 **       #&@/@&#       ,/  **       #&* ,&#       ,/  **     ,&%.(&@         ,/
 **     ,@&     %&,     ,/  **        #&&&%        ,/  **       *@&/          ,/
 **                     ,/  **                     ,/  **                     ,/
 .#                     (,  ,#                     /*  .#                     (,
   *%&&&&&&&&&&&&&&&&&%*      *%&&&&&&&&&&&&&&%&&%*      *%&&%&&&&&&&&&&&&&&%*
   
""")
            time.sleep(2)
            sys.stdout.write("*mhmm what to do, what to do...* (You think to yourself)")
            time.sleep(2)
            sys.stdout.write("\nI mean, I could just guess the code until I get it right (guess/code)")
            time.sleep(2)
            sys.stdout.write("\nBug who is standing behind you can see that you are sort of confused at where to start so he tells you that he remembers making it something easy that he thought he could as remember as he sees it alot..")
#----------------------------------
            #This is were the player guesses the code for the house to continue.
            #The while loop stays active for as long as the player keeps entering the wrong code.
            #If the play enters the correct code "5858" the loop breaks and continues the story for the player.
            fith_response = input("")
            if fith_response in question_group:
                while True:
                    code_guess1 = input("Guess the 4 digit code\n")
                    if code_guess1 < code:
                        sys.stdout.write("\n*Red light beeps*")
                    elif code_guess1 > code:
                        sys.stdout.write("\n*Red light beeps*")
                    else:
                        sys.stdout.write("\n*Green light beeps*")
                        break
                time.sleep(1)
                sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.            /   
 '     "--"'          .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
       """)
                sys.stdout.write("\n Wow!! " + players_name + " You actually did. I can't believe you broke into someones house")
                time.sleep(2)
                sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                #This is were the game ends for the free verison.
#----------------------------------            
        elif second_response in noList:
            third_response = input("Awh.. Can you please help me figure it out I will make it worth your while! (yes/no)\n")
            if third_response in yesList:
                sys.stdout.write("Thank you! I really apperecatie it.\n")
                time.sleep(2)
                sys.stdout.write("You walk up to the keypad and take a look to see what you are dealing with..\n")
                time.sleep(4)
                sys.stdout.write("""
  ,&*.................*@,    ,&*.................*&*    ,&*.................*&, 
 **                     ,/  */                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **          &&#        ,/  **       .@&(%&/       ,/  **       *&#,&&,       ,/
 **        /  @#        ,/  **           /&(       ,/  **          &@#        ,/
 **          .&(        ,/  **         &&(         ,/  **            @@       ,/
 **          .&#        ,/  **       (&@@@@&       ,/  **       .&&@@&        ,/
 **                     ,/  **                     ,/  **                     ,/
 .(                     /,  ,(                     /*  ,(                     /*
   ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*  
                                                                                
  .&(*****************(&.    .&(*****************(&,    .&(*****************(&, 
 **                     ,/  */                     */  */                     */
 **                     ,/  **                     ,/  **                     ,/
 **          &&&        ,/  **        #&@@@,       ,/  **        ,&@&@&       ,/
 **        /&,@&        ,/  **       .&&@@(        ,/  **       .&&,#(        ,/
 **       &&((&&(       ,/  **           .&#       ,/  **       .&@. .&&      ,/
 **           @&        ,/  **        #@@@(        ,/  **        (&%*%&/      ,/
 **                     ,/  **                     ,/  **                     ,/
 ,(                     /*  ,(                     **  ,(                     **
   (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#  
                                                                                
  /%.                 .#/    /%.                 .#(    *%.                 .#( 
 **                     ,/  **                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **       (&&%&&/       ,/  **       ,&# (&,       ,/  **       *&#.&@        ,/
 **          &%         ,/  **        /@@@(        ,/  **       /&* /&&       ,/
 **         &&          ,/  **       #&. .&%       ,/  **         ...&%       ,/
 **        .%*          ,/  **        #@@@%        ,/  **        (@@&,        ,/
 **                     ,/  **                     ,/  **                     ,/
 .%                     #,  ,#                     (,  .%                     (,
   .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.  
                                                                                
  ,%,.................,&*    ,%,.................,%*    ,&*.................,%* 
 **                     ,/  **                     */  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **     *&&#   #&@*     ,/  **       .@&,%@,       ,/  **            *&&.     ,/
 **        %&@&%        ,/  **       #&* ,&%       ,/  **           &&#       ,/
 **       #&@/@&#       ,/  **       #&* ,&#       ,/  **     ,&%.(&@         ,/
 **     ,@&     %&,     ,/  **        #&&&%        ,/  **       *@&/          ,/
 **                     ,/  **                     ,/  **                     ,/
 .#                     (,  ,#                     /*  .#                     (,
   *%&&&&&&&&&&&&&&&&&%*      *%&&&&&&&&&&&&&&%&&%*      *%&&%&&&&&&&&&&&&&&%*
   """)
                sys.stdout.write("\n*Mhmm what to do, what to do...* (You think to yourself)")
                time.sleep(2)
                sys.stdout.write("\nI mean, I could just guess the code until I get it right (guess/code)")
                time.sleep(2)
                sys.stdout.write("\nBug who is standing behind you can see that you are sort of confused at where to start so he tells you that he remembers making it something easy that he thought he could as remember as he sees it alot..")
#----------------------------------
                #This is were the player guesses the code for the house to continue.
                #The while loop stays active for as long as the player keeps entering the wrong code.
                #If the play enters the correct code "5858" the loop breaks and continues the story for the player.
                fourth_response = input("")
                if fourth_response in question_group:
                    while True:
                        code_guess2 = input("Guess the 4 digit code\n")
                        if code_guess2 < code:
                            sys.stdout.write("\n*Red light beeps*")
                        elif code_guess2 > code:
                            sys.stdout.write("\n*Red light beeps*")
                        else:
                            sys.stdout.write("\n*Green light beeps*")
                            break
                    time.sleep(1)
                    sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.            /   
 '     "--"'          .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
       """)
                    sys.stdout.write("\n Wow!! " + players_name + " You actually did. I can't believe you broke into someones house")
                    time.sleep(2)
                    sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                    #This is were the game ends for the free verison.
#----------------------------------
            elif third_response in noList:
                sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \     "   ._.' 
 .   :        ; \   '   \;  
 ;    \      /   :   '   :  
 ;     '-..-'        '   ;  
 :     ,---.    ,    '  /   
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
       """)
                #This input choice will confirm if the player is going to leave the scene and contiune on or stay.
                sixth_response = input("\nI can't believe you are going to do this to me, are you that heartless!? Thanks for nothing! " + players_name + " (yes/no)\n")
                if sixth_response in yesList:
                    sys.stdout.write("\nYou leave Bug standing there and proced to walk along one of the paths leading from the house\n")
                    time.sleep(3)
                    sys.stdout.write("...walking...walking....\n")
                    time.sleep(4)
                    sys.stdout.write("You have been walking for some time now when you start to see the pathway split into multiple directions with a signpost at the end\n")
                    time.sleep(2)
                    sys.stdout.write("You come to the end of the path where the signpost is and begin to examine it\n")
                    time.sleep(2)
                    sys.stdout.write("""
                     .--._..--.
              ___   ( _'-_  -_.'
          _.-'   `-._|  - :- |
      _.-'           `--...__|
   .-'                       '--..___
  / `._          The House            \
   `. `._                             |
     `. `._                           /
       '. `._    :__________....-----'
         `..`---'    |-_  _- |___...----..._
                     |_....--'             `.`.
               _...--'                       `.`.
          _..-'                            _.'.'
       .-'         The Town              _.'.'
       |                               _.'.'
       |                   __....------'-'
       |     __...------''' _|
       '--'''        |-  - _ |
               _.-''''''''''''''''''-._
            _.'                        |\
          .'                         _.' |
          `._      Mysterious         |:.'
            `._         House        _.' |
               `..__                 |  |
                    `---.._.--.    _|  |
                     | _   - | `-.._|_.'
          .--...__   |   -  _|
         .'_      `--.....__ |
        .'_                 `--..__
       .'_                         `.
      .'_          Bridge            `-.
      `--..____                        _`.
               ```--...____          _..--'
                   (\| - _ ```---.._.'
         ..       ;::|   - _ |/)     
  (o)        ;;::.,  |_ -  - |;;;:
 (\'/)   ::;;   (o)  | -_  -_L     ``::;;;.
 .;;'         (\ '/) |  -_ _ G (o)  ..;;
        '''    ;:;;.,|(o)  _-B(\'/)
   """)
                    sys.stdout.write("After looking at the sign you are faced with a few options on where to travel next\n")
                    #When the player gets to the sign we want them to pick a place to go.
                    #The if statement below allows them to do this.
                    #The lists are the words the player can type to go that direction.
                    signListA = ["a", "the house", "The house", "The House", "thehouse", "TheHouse", "A"]
                    signListB = ["b", "B", "town", "the town", "The Town", "TheTown", "thetown"]
                    signListC = ["c", "C", "Mysterious", "mysterious", "Mysterious House", "MysteriousHouse", "mysterioushouse", "mysterious house"]
                    signListD = ["d", "D", "Bridge", "bridge"]
                    seven_response = input("*Mhmm which way do I want to go?* (the house, the town, mysterious, bridge)\n")
                    #In the first if statement it is passing to the the town because we are forcing the player not to go back.
                    if seven_response in signListA:
                        sys.stdout.write("I just came from there, I am not going back to that weirdo..\n")
                        time.sleep(1)
                        sys.stdout.write("For trying to go back you have failed!")
                        time.sleep(4)
                        exit()
#----------------------------------
                    elif seven_response in signListB:
                        sys.stdout.write("I think I'm going to go to town\n")
                        time.sleep(1)
                        sys.stdout.write("*You start walking along the path leading east, heading towards The Town*\n")
                        time.sleep(2)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(3)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(3)
                        sys.stdout.write("*As you come up over a slight hill you can see before you the small town, with only a handful of buildings and people around*\n")
                        time.sleep(2)
                        sys.stdout.write("""
~         ~~          __
       _T      .,,.    ~--~ ^^
 ^^   // \                    ~
      ][O]    ^^      ,-~ ~
   /''-I_I         _II____
__/_  /   \ ______/ ''   /'\_,__
  | II--'''' \,--:--..,_/,.-{ },
; '/__\,.--';|   |[] .-.| O{ _ }
:' |  | []  -|   ''--:.;[,.'\,/
'  |[]|,.--'' '',   ''-,.    |
  ..    ..-''    ;       ''. '
  """)
                        sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                        #This is were the game ends for the free verison.
#----------------------------------
                    elif seven_response in signListC:
                        sys.stdout.write("I think I am going to go to The Mysterious House, whatever that is..\n")
                        time.sleep(1)
                        sys.stdout.write("*You start walking along the path leading north west, heading towards The Mysterious House*\n")
                        time.sleep(2)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(3)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(3)
                        sys.stdout.write("*As you were walking you noticed the forest around you became gloomy and dark with every minute that passed, just before the end of the path you see what appears to be a clearing in the forest*\n")
                        time.sleep(1)
                        sys.stdout.write("*When you get to the clearing you realise you can see a massive house up on a hill*\n")
                        time.sleep(3)
                        sys.stdout.write("""
                                        _____
                    . . . . .      _.-"'     '"-._
                    !-!-!-!-!    .'               '.
                    !_!_!_!_!  .'                   '.
                    |_=-   =| /   .-..                \
                    !_ ,;,-_]/    |__H _    .-\_)`-.   \
                  ,/`,/'_`\,`\,  [____|_]  /.-. .-,_\   ;
                ,/',/'/_|_\`\,`\,|=   |=|      \(       ;
              ,/' |/ ||'''|| \| `\, = | |       `       |
              |   #| ||___|| | #  |=  | |               |
            ,/' #  | [_____] |   #`\, |=|               ;
          ,/',-----'      =  '-----,`\--'---,/\,--,    /
         `""|   .;;;,=      ,;;;,   |#  # ,//  \\,'\, /
            | =//___\\ =   //___\\ =| # ,//',;;,'\\,#\,
            |  ||-. ||     ||   ||  |#,//' //||\\ '\\,`\,
            |  ||..\||     ||   ||  |-|/| ||_||_|| |\|_ _|
            |  ||   ||   = ||   ||  |=  | |.----.|=|___]
            |= ||___|| =   ||___|| =|  =| ||    || | ||
            | [_______]   [_______] |--.| ||____|| | ||
            ;_______=______=_____ __;   |[________]| ||
          ,/'#    #   #      #       #  '----------''\|
        ,/'    #        #       #         #     #   # '\,
      ,/'___#____#__#_____#___#_______#_______#____#___#'\,
      `""[____________________________________________]|""`
         _[_|   .-----.  =-       ___________    ||_]_||
        |  _| .",-"|"-,',   () = |.--..-..--.| = |_  |||
        |_/ |/ /_\_|_/_\ \ /__\  ||__||_||__||   | \_|\\
        (_) || .-------. | |  |  |.--..-..--.|  =| (_) ||
        / \ || |       | | |()|  ||__||_||__||   | / \ ||
        \_/ || '-------' |  )(   |___________|   | \_/ ||
        (_) ||.---------.|  \/   |.---------.|=  | (_) ||
        / \ |||   ___   ||    =  ||         ||   | / \ ||
        \_/ |||  {___}  ||       ||         ||   | \_/ ||
        (_) |||  ((_))  || -=   =||_________|| = |_(_)_//
        / \ |||   '-'   ||   _ .-'-----------'-. | / \__\
        \_/_|||       ()||  [_]-----------------[_]\_/\\\\
       [ __ ]||         || =| |==.==.==.==.==.==| |__]|||||
       j|  ||||         ||  | |  |  |  |  |  |  | |  |====|
       g|__|||;).       ||--|_|=='=='=='=='=='==|_|  ||||||
      _s____/`---`\ ____||_.____._____._____.____.|__|////
     |     |  9.9  |=====' |    |    /  \    \   |    |-'
     '------\ www /---'----'----'---'----'---'---'----'
             `---'
             """)
                        time.sleep(2)
                        sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                        #This is were the game ends for the free verison.
#----------------------------------
                    elif seven_response in signListD:
                        sys.stdout.write("Ehh I guess I will just go to the Bridge..\n")
                        time.sleep(1)
                        sys.stdout.write("*You start walking along the path leading north east, heading towards the Bridge*\n")
                        time.sleep(2)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(2)
                        sys.stdout.write("...walking...walking....\n")
                        time.sleep(2)
                        sys.stdout.write("*It isnt long before you see the stone Bridge in sight*")
                        time.sleep(2)
                        sys.stdout.write("""
   ______________________________________________________
   [[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]-[[]]
   .-.`| `-/-.__/.-'\_.-._,'/`-._'\_.-._`-'_/-._.'|/.-'\-
   \_.-`./`-._'\__.-`-.__.-`--._/--.`-._\`-._\__.-)`-'._/
   `._-'.\_.---._-.\_`-..`\_.---._`-.__.-`'._.--./`-'._,'
   __/`.-/       `.'_`./`.'       '.\__.-`.'    (_.-\_,-.
   `._-/'          |._.-|           |.'`.|       `(_.`-._
   .-',`)          | /`.|           |`-/`|         ;.-'_/
   `\,-/           |\.-'|           |\-'`|          ;\_,-
    -./`._        [[[[[[[[         [[[[[[[[         .',-'
    `.`--.~~-^_~-/.`-._`-.\^~-_~-^/`-.'-,.'\^~-~_^"'`-.'_
    -,.'"-"~^-~_~- - - _- -~^-_.~ - -_ - - -~- . "'"-"-""
    ""-'"-""-"~- _~.^-~-^.-^_.- .^~.-  ~-. ~^_-""-""-"'-"
    jgs
    """)
                        time.sleep(2)
                        sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                        #This is were the game ends for the free verison.

                    else:
                        sys.stdout.write("Well I am not going to stand here forever...")
                        sys.stdout.write("You failed because you took to long")
                    

#----------------------------------                    
    #This else if statement checks if the player has entered a number equal to or greater than 41 resulting in being to old.          
    elif players_age >= (str(41)):
        sys.stdout.write("Sorry " + players_age + "is to old to help!")
        time.sleep(1)
        exit()

    #This else statement tells the player they are not old enough because they entered a age to low of the accepted range (18+) by the program.
    else:
        sys.stdout.write("Sorry " + players_age + "is not old enough to help!")
        time.sleep(1)
        exit()
#----------------------------------
        #Below is the elif statement that belongs to the first convosation between the player and 'Bug'
elif first_response in noList:
    time.sleep(1)
    sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \     "   ._.' 
 .   :        ; \   '   \;  
 ;    \      /   :   '   :  
 ;     '-..-'        '   ;  
 :     ,---.    ,    '  /   
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug

""")
    sys.stdout.write("Well be like that then, I'm out of here...\n")
    time.sleep(2)
    sys.stdout.write("With tears down his cheek, Bug turns and starts to walk away\n")
    #The user is given an option incase they want to take back their first choice.
    time.sleep(2)
    butWait= input("Do you want to change your mind before hes gone completely gone? (yes/no)\n")
    if butWait in yesList:
        sys.stdout.write("You yell out to Bug, to gain his attention and tell him you changed your mind\n")
        time.sleep(3)
        sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.            /   
 '     "--"'          .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug

""")
        sys.stdout.write("That was really mean " +players_name+ "I'm glad you changed your mind though..\n")
        time.sleep(1)
    #This if statement checks to see if the player is correct age to help the character
        sys.stdout.write("Okay I need to make sure you can handle the task, please tell me your age\n")
        play_age = sys.stdin.readline()
        if play_age >= (str(18)) and play_age <= (str(41)):
            sys.stdout.write("Mhmm " + play_age + "That should be old enough!\n")
            time.sleep(2)
            sys.stdout.write("Please follow me, I'll take us to my house\n")
            time.sleep(1)
            sys.stdout.write("You begin walking with Bug...\n")
            time.sleep(3)
            sys.stdout.write("... ... .....\n")
            time.sleep(4)
            sys.stdout.write("... ... ... still walking ...\n")
            time.sleep(3)
            sys.stdout.write("Ah here we are! That's my house over there! *Bug points ahead*\n")
            time.sleep(3)
            sys.stdout.write("""
            (
                )
            (            ./\.
         |^^^^^^^^^|   ./LLLL\.
         |`.'`.`'`'| ./LLLLLLLL\.
         |.'`'.'`.'|/LLLL/^^\LLLL\.
         |.`.''``./LLLL/^ () ^\LLLL\.
         |.'`.`./LLLL/^  =   = ^\LLLL\.
         |.`../LLLL/^  _.----._  ^\LLLL\.
         |'./LLLL/^ =.' ______ `.  ^\LLLL\.
         |/LLLL/^   /|--.----.--|\ = ^\LLLL\.
       ./LLLL/^  = |=|__|____|__|=|    ^\LLLL\.
     ./LLLL/^=     |*|~~|~~~~|~~|*|   =  ^\LLLL\.
   ./LLLL/^        |=|--|----|--|=|        ^\LLLL\.
 ./LLLL/^      =   `-|__|____|__|-' =        ^\LLLL\.
/LLLL/^   =         `------------'        =    ^\LLLL\
~~|.~       =        =      =          =         ~.|~~
  ||     =      =      = ____     =         =     ||
  ||  =               .-'    '-.        =         ||
  ||     _..._ =    .'  .-58-.  '.  =   _..._  =  ||
  || = .'_____`.   /___:______:___\   .'_____`.   ||
  || .-|---.---|-.   ||  _  _  ||   .-|---.---|-. ||
  || |=|   |   |=|   || | || | ||   |=|   |   |=| ||
  || |=|___|___|=|=  || | || | ||=  |=|___|___|=| ||
  || |=|~~~|~~~|=|   || | || | ||   |=|~~~|~~~|=| ||
  || |*|   |   |*|   || | || | ||  =|*|   |   |*| ||
  || |=|---|---|=| = || | || | ||   |=|---|---|=| ||
  || |=|   |   |=|   || | || | ||   |=|   |   |=| ||
  || `-|___|___|-'   ||o|_||_| ||   `-|___|___|-' ||
  ||  '---------`  = ||  _  _  || =  `---------'  ||
  || =   =           || | || | ||      =     =    ||
  ||  %@&   &@  =    || |_||_| ||  =   @&@   %@ = ||
  || %@&@% @%@&@    _||________||_   &@%&@ %&@&@  ||
  ||,,\\V//\\V//, _|___|------|___|_ ,\\V//\\V//,,||
  |--------------|____/--------\____|--------------|
 /- _  -  _   - _ -  _ - - _ - _ _ - _  _-  - _ - _ \
/____________________________________________________\

            """)
            time.sleep(2)
            sys.stdout.write("\nSo what do you think? haha, not bad if I say so myself\n")
            time.sleep(3)
            sys.stdout.write("Please come inside...\n")
            time.sleep(2)
            sys.stdout.write("You both begin to walk towards the door, *You see Bug reach into his pocket* when he turns to you\n")
            time.sleep(3)
            sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.    ,       /   
 '    '  -. "--"      .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
       """)
            sys.stdout.write("\nWell this is awarkward.. I seem to have left my keys inside but the only other way in is my electrionic keypad, but I bloody can't remember my passcode...\n")
            time.sleep(3)
            sys.stdout.write("I hate to ask but do you think you could figure it out for me? I will make it worth while!\n")
            time.sleep(3)
            sys.stdout.write("*Without any hesation you nod at bug*\n")
            time.sleep(3)
            sys.stdout.write("Thank you so much, I knew I could count on you!\n")
            time.sleep(3)
            sys.stdout.write("*Well it is the least I could do after making him feel bad before, (you think to yourself)*\n")
            time.sleep(3)
            sys.stdout.write("You walk up to the keypad and take a look to see what you are dealing with..\n")
            time.sleep(4)
            sys.stdout.write("""

  ,&*.................*@,    ,&*.................*&*    ,&*.................*&, 
 **                     ,/  */                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **          &&#        ,/  **       .@&(%&/       ,/  **       *&#,&&,       ,/
 **        /  @#        ,/  **           /&(       ,/  **          &@#        ,/
 **          .&(        ,/  **         &&(         ,/  **            @@       ,/
 **          .&#        ,/  **       (&@@@@&       ,/  **       .&&@@&        ,/
 **                     ,/  **                     ,/  **                     ,/
 .(                     /,  ,(                     /*  ,(                     /*
   ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*      ,&@@@@@@@@@@@@@@@@@@*  
                                                                                
  .&(*****************(&.    .&(*****************(&,    .&(*****************(&, 
 **                     ,/  */                     */  */                     */
 **                     ,/  **                     ,/  **                     ,/
 **          &&&        ,/  **        #&@@@,       ,/  **        ,&@&@&       ,/
 **        /&,@&        ,/  **       .&&@@(        ,/  **       .&&,#(        ,/
 **       &&((&&(       ,/  **           .&#       ,/  **       .&@. .&&      ,/
 **           @&        ,/  **        #@@@(        ,/  **        (&%*%&/      ,/
 **                     ,/  **                     ,/  **                     ,/
 ,(                     /*  ,(                     **  ,(                     **
   (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#      (@&&&&&&&&&&&&&&&&&@#  
                                                                                
  /%.                 .#/    /%.                 .#(    *%.                 .#( 
 **                     ,/  **                     ,/  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **       (&&%&&/       ,/  **       ,&# (&,       ,/  **       *&#.&@        ,/
 **          &%         ,/  **        /@@@(        ,/  **       /&* /&&       ,/
 **         &&          ,/  **       #&. .&%       ,/  **         ...&%       ,/
 **        .%*          ,/  **        #@@@%        ,/  **        (@@&,        ,/
 **                     ,/  **                     ,/  **                     ,/
 .%                     #,  ,#                     (,  .%                     (,
   .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.      .#%%%%%%%%%%%%%%%%%#.  
                                                                                
  ,%,.................,&*    ,%,.................,%*    ,&*.................,%* 
 **                     ,/  **                     */  **                     ,/
 **                     ,/  **                     ,/  **                     ,/
 **     *&&#   #&@*     ,/  **       .@&,%@,       ,/  **            *&&.     ,/
 **        %&@&%        ,/  **       #&* ,&%       ,/  **           &&#       ,/
 **       #&@/@&#       ,/  **       #&* ,&#       ,/  **     ,&%.(&@         ,/
 **     ,@&     %&,     ,/  **        #&&&%        ,/  **       *@&/          ,/
 **                     ,/  **                     ,/  **                     ,/
 .#                     (,  ,#                     /*  .#                     (,
   *%&&&&&&&&&&&&&&&&&%*      *%&&&&&&&&&&&&&&%&&%*      *%&&%&&&&&&&&&&&&&&%*
   """)
            time.sleep(3)
            sys.stdout.write("\n*mhmm what to do, what to do... (You think to yourself)*")
            time.sleep(3)
            sys.stdout.write("\n*I guess I could just try guessing the code or maybe there's some clue laying around here.* (guess/code)")
            time.sleep(3)
            sys.stdout.write("\nBug who is standing behind you can see that you are sort of confused at where to start so he tells you.. 'I know it's a 4 digit code and I faintly recall it starting with a 5'.\n")
#----------------------------------
            #This is were the player guesses the code for the house to continue.
            #The while loop stays active for as long as the player keeps entering the wrong code.
            #If the play enters the correct code "5858" the loop breaks and continues the story for the player.
            eight_response = input("")
            if eight_response in question_group:
                while True:
                    code_guess3 = input("Guess the 4 digit code\n")
                    if code_guess3 < code:
                        sys.stdout.write("\n*Red light beeps*")
                    elif code_guess3 > code:
                        sys.stdout.write("\n*Red light beeps*")
                    else:
                        sys.stdout.write("\n*Green light beeps*")
                        break
                time.sleep(1)
                sys.stdout.write("""
             ____           
        .--""___ ""-,       
      .' .-"" __:-' ;       
     /__:.--""      :       
     \              _`-'\   
      \_..--""    ""     :  
      /      ______..,   ;  
   _gd$$$$$$$$$$$$$$$P===;  
,g$$$$$$P^^^^T$$$$$P'    ;  
T^": ,-.       "'"  \    :  
    ;;  d.   .-"'"d. \ ,-:  
   : '.:$$'-"    :$$  '.-,; 
   ;   :^"    "-._T'  ') :: 
  /   /      \         ._.' 
 .   :        ; \       \;  
 ;    \      /   :       :  
 ;     '-..-'            ;  
 :     ,---.            /   
 '     "--"'          .'    
  `.              _.-"      
    "-.       _.-"          
       "-._.-"     Bug
       """)
                sys.stdout.write("\n Wow!! " + players_name + " You actually did it. I can't believe you figured that out!")
                time.sleep(3)
                sys.stdout.write("\n Now come on in " + players_name + "I want to give you a gift for helping me out.")
                time.sleep(3)
                sys.stdout.write("\n CONGRATULATIONS!! You have reached the end of your game demo. If you would like to continue please purchase the game from 'www.maybe_this_will_be_real_one_day.com.au'")
                #This is were the game ends for the free verison.
#----------------------------------   
        else:
            sys.stdout.write("Sorry you are not old enough to help this story!\n")
            time.sleep(1)
            exit()
    elif butWait in noList:
        sys.stdout.write("You failed!")
        time.sleep(1)
        exit()
else:
    sys.stdout.write("Hello are you listening?")
    time.sleep(1) 
    exit()
