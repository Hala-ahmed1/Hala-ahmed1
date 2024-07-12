import time

# import random module
import random


play_again = True
# nameing the inputs with diffrent name so when player
# makes invalid inputs the game askes to reenter the choice
#so when user renter the choice it fills the right user
#and the game doesnt crash
user_input = ""
user_input1= ""
user_input2= ""
user_input3= ""
user_input4= ""
user_input5= ""
user_input6= ""
user_input7= ""
user_input8= ""
score = 100
# set up the list of food you might find
food = ["blue berry", "tomato", "apple", "banana", "orange"]
# Function to subtract from the score


def score_sub(g):
    global score
    score -= g
    print("Score:", score)


# Function to add to the score
def score_add(h):
    global score
    score += h
    print("Score:", score)
    
    
# Function to handle the game logic
def game_logic():
    global score
    
    
#a loop to restart the game or to end
def again():
    while True:
        user_input = input("Do you want to play again? (yes/no): ")
        if user_input == "yes":
            return True
        elif user_input == "no":
            print("THE END")
            return False
        else:
            print("Invalid input. Please try again.")
    
def friend():
    print("you started to look around for your friend..")
    time.sleep(2)
    print("you decided to follow your friend's steps...")
    time.sleep(2)
    print("you went to the left path..")
    time.sleep(2)
    print("you lit a small torch")
    time.sleep(2)
    print("while walking, you almost fell in a hole")
    time.sleep(2)
    print("you managed to dodge it.. and when you looked inside you..")
    time.sleep(2)
    print("you found your friend asking for help")
    time.sleep(2)
    print("you decided to...")
    time.sleep(2)
    user_input1 = input("Enter 1 to save friend, Enter 2 to leave friend")
    if user_input1 == "2":
        score_add(10)
        print("you left your friend in the hole..")
        time.sleep(2)
        print("your friend will die from hunger")
    elif user_input1 == "1":
        score_sub(10)
        print("you saved your friend")
        time.sleep(2)
        print("when you stand up your friend attack you.. so you..")
        user_input2 = input("1 to attack, 2 to run, 3 do nothin")
        if user_input2 == "3":
            score_sub(40)
            print("you did nothing and your friend threw you into the hole..")
            time.sleep(2)
            print("you asked your friend for help but...")
            time.sleep(2)
            print("your friend left you in the hole")
            print("and you died a few weeks after..")
            print("bad ending")
            play_again = again()
        elif user_input2 == "2":
              score_sub(10)
              print("you ran away from your friend and went back to the cave")
              cave()
        elif user_input2 == "1":
                 score_add(10)
                 print("you attacked your friend")
                 print("and threw your friend back in the hole")
                 time.sleep(2)
                 print("you desided to go back to the cave..")
                 cave()
        else:
                while user_input2 not in ["1", "2","3"]:
                    print("Invalid input. Please try again.")
                    user_input2 = input("1 to attack, 2 to run, 3 do nothin")
    else:
                while user_input1 not in ["1", "2"]:
                    user_input1 = input("1 save friend,2 leave friend")


def cave():
    print("you went back to the cave it was dark..")
    time.sleep(2)
    print("you went to sit on your usual spot")
    time.sleep(2)
    print("you lit a small fire to warm up and fell asleep..")
    time.sleep(2)
    print("later you woke up and..")
    time.sleep(2)


def beginning():
    print("you returned to the place you and your friend split..")
    time.sleep(2)
    print("your friend is not there...")
    time.sleep(2)
    print("you regret splitting...")


def voices():
    user_input8 = input("1 go to the voice, 2 to stay hidden forever")
    if user_input8 == "1" :
        score_add(10)
        print("you went to the voices and you were finally saved..")
        time.sleep(2)
        print("you reashed good ending1")
        time.sleep(2)
        print("you went back to your family and friends")
        time.sleep(2)
        print("you will never kniw what really happened to your friend..")
        print("THE END")
        play_again = False
        play_again = again()
    elif user_input8 == "2" :
        score_add(20)
        print("you desided to stay in the cave")
        print("and never leave until you find your friend...")
        time.sleep(2)
        friend()
        cave()
        print("you stayed in the cave forever")
        time.sleep(2)
        print("good ending")
        print("THE END")
        play_again = False
        play_again = again()


def look():
    user_input7 = input("Enter cave go to cave,Enter beginning to find friend")
    if user_input7 == "cave":
        score_sub(20)
        cave()
    elif user_input7 == "beginning" :
        score_add(20)
        beginning()
        friend()
        cave()
        print("you heard some noise...it was people voices..")
        time.sleep(2)
        print("you decided to...")
        voices()


def food_water():
    user_input6 = input("Enter 1 to get food,  Enter 2 to get water")
    if user_input6 == "2":
        score_sub(10)
        print("you found a river and you had a bottel in your back bag..")
        time.sleep(3)
        print("you leaned down to fill the bottel..")
        time.sleep(4)
        print("you fell in the water and you can't swim..")
        time.sleep(2)
        print("you kept struggeling in the water")
        time.sleep(5)
        print(" you drowned...")
        play_again = again()
    elif user_input6 == "1":
        score_add(20)
        print("you went to get food")
        time.sleep(2)
        print("you found an")
        print(random.choice(food))
        print("tree")
        time.sleep(2)
        print("you grapped some and putted them in your bag")
        time.sleep(2)
        print("then you desided to go to...")
        time.sleep(2)
        look()


def bear():
    user_input5=input("1 to run,2 to hide behind tree,3 hide inside a cave")
    if user_input5 == "1":
        score_sub(5)
        print("You ran to the opposite direction..")
        time.sleep(2)
        print("Your friend grabbed you and the bear couldn't find you..")
        print("When you were about to thank your friend")
        print("you felt a sharp pain in your back.. ")
        print("It was a knife that your friend stabbed into your back...")
        print("Your friend betrayed you...")
        play_again = again()
    elif user_input5 == "2":
        score_sub(10)
        print("You hid behind a tree..")
        time.sleep(3)
        print("You looked to your left to find the bear..")
        time.sleep(3)
        print("The bear ate you and you died...")
        play_again = again()
    elif user_input5 == "3":
        score_add(20)
        print("You ran and hid inside a cave")
        time.sleep(3)
        print("It was so dark.. but you were safe from the bear")
        time.sleep(3)
        print("you saw a spot and desided to sit at and then lighted the fire")
        time.sleep(3)
        print("you fell asleep..")
        time.sleep(3)
        print("you woke up later and desided to go get...")
        food_water()


def seperation_story():
    user_input3 = input("Enter 1 to split up, Enter 2 to stay together: ")
    if user_input3 == "1":
         score_add(10)
         print("You and your friend chose to split up, so you choose the...")
         user_input4 = input("Enter 1 to go left, Enter 2 to go right: ")
         if user_input4 == "1":
              score_sub(10)
              print("You choose the left path and walked through it.")
              time.sleep(2)
              print("While walking...")
              print("you fell into a hole and screamed for help")
              print("but no one heard you...")
              print("You stayed in the hole for a few weeks")
              print("and then... died from lack of food and water.")
              play_again = again()
         elif user_input4 == "2":
             score_add(5)
             print("You walked through the right path")
             time.sleep(3)
             print("While walking, you heard a bear's voice")
             bear()
    elif user_input3 == "2":
        score_sub(10)
        print("You and your friend decided to stay together")
        print("and went through the same path.")
        time.sleep(2)
        print("While you both were walking...")
        print("you felt a sharp pain in your back...")
        time.sleep(4)
        print("It was due to a sharp knife..")
        print("that your friend stabbed into your back...")
        time.sleep(4)
        print("Your friend betrayed you....")
        play_again = again()


play_again = True
while play_again :
    score = 100
    print("system: in this game you have a score")
    print("your current score is 100 your score depends on your choises")
    print("if your score reaches 0 you lose")
    print("You and your friend are lost in the forest.")
    time.sleep(2)
    print("You always hear rumors that your friend is not loyal")
    print("but you weren't sure...")
    time.sleep(3)
    print("You two were walking in the forest trying to find an exit")
    print("but you couldn't.")
    time.sleep(3)
    print("Then you both faced two different paths")
    print("so you both decided to...")
    time.sleep(4)
    user_input3 = input("Enter 1 to split up, Enter 2 to stay together")
    if user_input3 == "1":
         score_add(10)
         print("You and your friend chose to split up, so you choose the...")
         user_input4 = input("Enter 1 to go left, Enter 2 to go right: ")
         if user_input4 == "1":
              score_sub(10)
              print("You choose the left path and walked through it.")
              time.sleep(2)
              print("While walking")
              print("you fell into a hole and screamed for help")
              print("but no one heard you...")
              print("You stayed in the hole for a few weeks")
              print("and then died from lack of food and water.")
         elif user_input4 == "2":
             score_add(5)
             print("You walked through the right path")
             time.sleep(3)
             print("While walking, you heard a bear's voice")
             user_input5 = input("1 run,2 hide behind tree,3 hide in cave")
             if user_input5 == "1":
                  score_sub(5)
                  print("You ran to the opposite direction..")
                  time.sleep(2)
                  print("Your friend grabbed you")
                  print("and the bear couldn't find you..")
                  print("When you were about to thank your friend")
                  print("you felt a sharp pain in your back.. ")
                  print("It was a knife")
                  print("that your friend stabbed into your back...")
                  print("Your friend betrayed you...")
                  play_again = again()
             elif user_input5 == "2":
                  score_sub(10)
                  print("You hid behind a tree..")
                  time.sleep(3)
                  print("You looked to your left to find the bear..")
                  time.sleep(3)
                  print("The bear ate you and you died...")
                  play_again = again()
             elif user_input5 == "3":
                 score_add(20)
                 print("You ran and hid inside a cave")
                 time.sleep(3)
                 print("It was so dark.. but you were safe from the bear")
                 time.sleep(3)
                 print("you saw a spot and desided to sit at")
                 print("and then lighted the fire")
                 time.sleep(3)
                 print("you fell asleep..")
                 time.sleep(3)
                 print("you woke up later and desided to go get...")
                 user_input6 = input("1 to get food, 2 to get water")
                 if user_input6 == "2":
                      score_add(20)
                      print("you found a river")
                      print("and you had a bottel in your back bag..")
                      time.sleep(3)
                      print("you leaned down to fill the bottel..")
                      time.sleep(4)
                      print("you fell in the water and")
                      print("you can't swim..")
                      time.sleep(2)
                      print("you kept struggeling in the water")
                      time.sleep(5)
                      print(" you drowned...")
                      play_again = again()
                 elif user_input6 == "1":
                     score_add(20)
                     print("you went to get food")
                     time.sleep(2)
                     print("you found an")
                     print(random.choice(food))
                     print("tree")
                     time.sleep(2)
                     print("you grapped some and putted them in your bag")
                     time.sleep(2)
                     print("then you desided to go to...")
                     time.sleep(2)
                     print("Enter cave go to cave,Enter beginning find friend")
                     user_input7 = input("cave or beginning?")
                     if user_input7 == "cave":
                         score_sub(20)
                         cave()
                     elif user_input7 == "beginning" :
                         score = score + 20
                         print("score:")
                         print(score)
                         beginning()
                         friend()
                         cave()
                         print("you heard some noise..it was people voices.")
                         time.sleep(2)
                         print("you decided to...")
                         print("Enter 1 to go to the voice")
                         print("Enter 2 to not leave the cave")
                         user_input8 = input(" 1 or 2 ?")
                         if user_input8 == "1" :
                             score_sub(70)
                             print("you went to the voices")
                             print("and you were finally saved..")
                             time.sleep(2)
                             print("you reashed good ending1")
                             time.sleep(2)
                             print("you went back to your family and friends")
                             time.sleep(2)
                             print("you will never know what really happened")
                             print("to your friend..")
                             print("THE END")
                             play_again = False
                             play_again = again()
                         elif user_input8 == "2" :
                             score_add(20)
                             print("you desided to stay in the cave")
                             print("and never leave until..")
                             print("you find your friend...")
                             time.sleep(2)
                             friend()
                             cave()
                             print("you stayed in the cave forever")
                             time.sleep(2)
                             print("good ending")
                             print("THE END")
                             play_again = False
                             play_again = again()
                         else:
                             while user_input8 not in ["1", "2"]:
                                 user_input8 = input("1 voices , 2 hide")
                     else:
                         while user_input7 not in ["beginning", "cave"]:
                             print("Invalid input. Please try again.")
                             user_input7 = input("cave or beginning ?")
                 else:
                     while user_input6 not in ["1", "2"]:
                         print("Invalid input. Please try again.")
                         user_input6 = input("1 to get food,2 to get water")
             else:
                 while user_input5 not in ["1", "2","3"]:
                    print("Invalid input. Please try again.")
                    print("1 run, 2 hide behind tree, 3 hide in cave")
                    user_input5 = input("1 or 2 or 3?")
         else:
              while user_input4 not in ["1", "2"]:
                        print("Invalid input. Please try again.")
                        user_input4 = input("1 left, 2 right")
    elif user_input3 == "2":
        score_sub(40)
        print("You and your friend decided to stay together")
        print("and went through the same path.")
        time.sleep(2)
        print("While you both were walking")
        print("you felt a sharp pain in your back...")
        time.sleep(4)
        print("It was due to a sharp knife")
        print("that your friend stabbed into your back...")
        time.sleep(4)
        print("Your friend betrayed you....")
        play_again = again()
    else:
        while user_input3 not in ["1", "2"]:
            print("Invalid input. Please try again.")
            user_input3 = input("1 split up,2 stay together")
            seperation_story()
