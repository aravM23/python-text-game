# Author: Arav
#January 25th,2023
#The road home
#This game is about being stranded and getting lost, leading to several tasks which assist in guiding you home.
import random #imports the function we will use for tasks
# first I defined all my variables
currentdist = 0 #the current distance
totaldistance = 500 #the total distance
health = 100 #health gained
applestrength = 3 #strength gained by apples
usergame = 0 #usergame options 
botgame = 0 #bot actoins in the game
user = 0 #user choices
applequant = 0 #quantity of collceted apples
hometown = input("\nWhat is your hometown") #hometown to guide your way
choices = 0 #choices made
merchant = 0 #merchant seller
rock = 1 #rock 
paper = 2 #paper
scissor = 3 #scissor
endquest = 0 #end of game question, if user wans to quit or not

#defined some repeated functions of repeated code

def distance(): #tells user distnce travelled
  global currentdist
  global totaldistance
  print("you have travelled", currentdist, "miles and have",totaldistance-currentdist," miles to go")

def healthlulli():#depicts health
  global health
  print("your health is currently at", health)
  if health<=0:
    print("you died")

def kaliterilulli():#apple quantity changing based on choices
  if user == 1:
    global applequant
    global health 
    applequant = applequant - 1
    health = health + applestrength
  else:
    print("Sounds good lets move on to the next task")

def terilullichoti(): #current distance gain
  global currentdist 
  global applequant 
  currentdist = currentdist + 80
  applequant = applequant + 1

def rockpaperscissor(): #rockpaperscissor game
 global rock 
 global paper 
 global scissor
 global usergame
 global botgame
 global health
 global currentdist
 global applequant
 usergame = int(input("Enter a number from 1-3, 1 being rock, 2 being paper, and 3 being scissor"))
 botgame = random.randrange(4)
 if (usergame - botgame)== 1:
   print("you won")
   currentdist = currentdist + 100
   applequant = applequant + 1
 elif (botgame-usergame)==1:
   print("you lose")
   health = health - 15  
 elif usergame==botgame:
   print("its a tie")
   print("you do not recieve any reward, but neither do you lose anything")
 elif(usergame-botgame)== 2:
   print("you lose")
   health = health - 15
 elif(botgame-usergame)==2:
   print("you win")
   currentdist = currentdist + 100
   applequant = applequant + 1
 else:
   print("Never try to beat a game by entering invalid values")
   health = health - 15
   healthlulli()

  #Lets start of with a while statement which runs through our program of when currentdistance is not equal less than total distance, as, if it is equal, thet means user defeated game we also keep track of health which when below 0 the game ends, additonally endquest keeps track of if the user wants to quit or not

while ((currentdist < totaldistance) and (health > 0)) or (endquest!=2):
  print("Here you are stranded on an unknown road, your heart races as you scan the scene around you, where you see a sign which states, 500 miles to ",hometown," 500 miles could take days to walk, so concurrently, you start scanning the setting around to find how you can make it home, throughout scanning you will encounter a series of tasks, which at succesful completion will award you a way to sweep through the miles, but failure to complete these tasks comes at a consequence, as you show off your skill, you also recieve apples which can be consumed for health to  guide you along the way, so let's meet you on the other side ")

# here is the first task in the path using randrange where you are going up against a bot
  
  print("\nYou encounter a car zooming through the streets,as you stick your thumb up to get a hitch hike, however the individual in the car states,'I want to make things fun for myself, how about a staring contest for a hitch' your abruptly agree..")
  usergame = int(input("Enter a number between 1-10\n"))
  botgame = random.randrange(11) 
  if (usergame>=11) or (usergame<=0):#not the options given, invalid
    print("\nplay properly")
    health = health - 15
    healthlulli()
  elif usergame>botgame:
    print("\nCongratulation, since you won the stranger agrees to take you 80 miles ahead where he is heading")
    terilullichoti()
    user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
    kaliterilulli() 
    healthlulli()
  else:
    print("\ntough luck, you have to walk for now")
    health = health - 15
    healthlulli()
    distance()
    

#Here is the second task, if the first task was succesfully completed you recieved 80 miles and an apple, the apple could grant you 3 health if chosen to use, however, failure of task completion takes away 15 health
  
  print("\nAfter travelling the miles, you encounter a new opportunity where you are offered to race an individual")
  usergame = int(input("Enter a number between 1-25\n"))
  botgame = random.randrange(26)
  if (usergame>=26) or (usergame<=0):
    print("\nplay properly please")
    health = health - 15
    healthlulli()
  elif botgame>usergame:
    print("\nWow, your victory awards you new shoes to keep you going comfortably for the next few miles")
    terilullichoti()
    user = input("\ndo you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
    kaliterilulli() 
    healthlulli()
  else:
    print("\nOh well, you need to walk along your old boots for now")
    health = health - 15
    healthlulli()
    distance()
    

#As you can see, we start increasing the range used for the random category games to make winning harder and harder as we slowly move on to the riddle part od the game, as you can see, throughout the first few tasks both defined fucntions are doing their role,one for adding distance if you are succesful, while the other is for adding health if you choose the option to use collected golden apple
  
  print("\nAs you build pace towards your destination you notice you have two paths both guiding you to the same place, choose one to go through ")
  
  choices = int(input("Enter a number between 1 and 2\n"))
  if choices == 2: #second choice chosen
    print("\nthere are zombies chasing you choose a number which determines your next move, 1 - behind a car, 2 - behind an electric wire, 3 - fight the zombies, 4 - stay still ")
    usergame = int(input("Enter your choice\n"))
    if (usergame == 1) or (usergame == 2): #correct options to the riddle
      print("\nWow, the zombies zoom right through without noticing, keeping you going comfortably for the next few miles")
      terilullichoti()
      healthlulli()
      user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
      kaliterilulli() 
      healthlulli()
    else: #depicting loss
     print("\nOh well, the zombies came out victorious")
     health = health - 15
     healthlulli()
     distance()
     
  elif choices == 1:#first path chosen
    print("\nthere are invisible ghosts which can come from anywhere, every movement is a threat what do you do, 1 - run behind a car, 2 - stay where you are, 3 - stand still, 4 - start dancing ")
    usergame = int(input("Enter your choice\n"))
    if (usergame == 2) or (usergame == 3):#correct riddle options chosen
      print("\nThat was close, your standing still prevents the ghosts from getting to you, now you can move comfortably")
      terilullichoti()
      user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
      kaliterilulli()  
    else: #lost the riddle
     print("\nOh no, you have been attacked by ghosts")
     health = health - 15
     healthlulli()
     distance()
      
  else: #usually invalid
    print("\nplease enter a valid input next time, due to your inability to play you have been punished")
    health = health - 15
    healthlulli()
    distance()

# the first choice based game required the use of nested statements to determine the choice based system, concurrently our spead out options also increased difficulty rather then just picking random numbers in the first few tasks.
    
  print("\nYou notice a route blocked off by a guard, which saves you around 80 miles, so you decide to fight the guard")
  usergame = int(input("Enter a number between 1-3"))
  botgame = random.randrange(4)
  if (usergame>3) or (usergame<=0): #invalid options
    print("invalid.. not again..")
    health = health - 15
    healthlulli()
  elif usergame>botgame: #correct user choice
    print("\nWoah, thet was a clean punch, the guard is knocked out RUN")
    terilullichoti()
    healthlulli()
    user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
    kaliterilulli()
    healthlulli()
  else: #loss depiction
    print("Ouch thet must have hurt, good thing, it's only a few bruises\n")
    health = health - 15
    healthlulli()
    distance()
    

    # This attack base random game can get very challenging, mainly because there are only three options and it is very unlikely thet your option if higher then the bots (1/3%) chance, this was added so thet the user is convinced to use the next feature of a in game shop merchant

  print("Congratulations on completing your first few tasks, because of your accomplishment, you encounter a merchant who is willing to assist you in your journey in exchange for your apples, here are his offers: 1 apple for 25 miles off, 2 apples for 50 miles off, 3 for 100 miles off, any other selection will be ignored, as the merchant doesn't like being annoying")
  user = int(input("Pick a number to choose your selection\n"))
  if user == 1:#first choice chosen
    totaldistance = totaldistance - 25
    print("nice choice\n")
  elif user == 2: #second choice chosen
    totaldistance = totaldistance - 50
    print("hefty expense\n")
  elif user == 3: #third choice chosen
    totaldistance = totaldistance - 100
    print("big spender\n")
  else: #none of the given options chosen
    print("The merchant storms away\n")

# The ingame shop uses basic if/else statements to utilize your collected apples for a totaldistance reduction to make the game easier, however in order to use this perk you need to be organized and store your apples
    
  print("\nAt the end of the road there is a visible bus path however there is only one seat which is available, however you see another person also walking to the bus, to resolve this problem the driver chooses a particular number between 1-10, whoever's number is closer, yours or the other person's gets to sit on the bus")
  usergame = int(input("Enter a number between 1-3\n"))
  botgame = random.randrange(4)
  choice = 9
  if usergame>=4: #usually invalid
    print("\nlook at options properly")
    health = health - 15
    healthlulli()
  elif (usergame - choice) or (choice - usergame) >= (botgame - choice) or (choice - botgame):#correct options
    print("\nNice guessing skills, thet earned you a spot on the bus")
    terilullichoti()
    healthlulli()
    user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
    kaliterilulli()
    healthlulli()
  else:
    print("\ntouch luck, you are left standing as the bus leaves leaving it's exhaust on you")#incorrect option
    health = health - 15
    healthlulli()
    distance()
    
  
  print("\nThere is just a bit more to go in your final distance you abruptly encounter this woman who seems to be incredibly hungry and is asking for food, the only thing you have with you are your collected apples, currently you have", applequant,"apples do you want to help this woman or not")
  if applequant>=1:#checks if you have enough apples
    usergame = int(input("Enter a number between 1-2, 1 if you want to help and 2 if you wnat to go forward\n"))
    if usergame==1:#choose to help woman
      applequant = applequant - 1
      print("\nsince you chose to help the woman, she awards you with a worn out bike which could speed up your path atleast for a bit")
      terilullichoti()
      healthlulli()
    elif usergame==2:#choose to keep going
      print("\nbe more caring, your actions always come back to you")
      health = health - 15
      kaliterilulli()
      healthlulli()
    elif (usergame>=2)or(usergame<=0):#invalid response
      print("\nYou are not looking at the options")
      health = health - 15
      healthlulli()
  else:#for not enough apples
    print("\nyou should have saved up, irresponsible")
    health = health - 15
    healthlulli()
    distance()
  print("\nYour final task emerges, you notice a nearby taxi center and decide to enter to ask for assistance, as you explain your scenario to the manager, they state thet they could help by providing one free service of a carpool taxi, but in order to attain it, you have to beat the managers son in a game of rock paper scissors, since this is the last task, instead of the usual 80 miles, you get 20 additional miles at victory")
  rockpaperscissor()
  if (usergame - botgame== 1) or (botgame-usergame==2):#correct options chosen, win game
    user = input("do you want to use the apple you recieved for three extra health, press '1', if not click any button\n")
    kaliterilulli() 
    healthlulli()
  elif (botgame-usergame==1) or (usergame-botgame== 2):#wrong options chosen, lose game
    print("\nGood try but this wasn't your day")
    healthlulli()
  print("\nIt is the end of the journey where you travelled",currentdist," miles and are left with",health," health. Although you didn't make it, you still have health left, would yuo like to try and continue with the health you have")
  #prints last parts
  endquest = int(input("\nIf you would like to continue the challenge with this new challenge of lower health, press 1, if you want to end the game press 2"))
  #asks to continue or end
  if endquest>=3:#invalid
    print("\nyou are not playing seriously, when you are ready to pleay properly please run the game sometime later")
    health = health - 100
print("game over")
if (currentdist>=totaldistance) or (currentdist==totaldistance):
  print("Congratulations you beat the game")
    