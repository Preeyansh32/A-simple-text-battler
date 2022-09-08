
def moves():
    print("""Move 1
This move attacks the enemy""")
    print("""Move 2
This move reduces the opoonents attack""")
    print("""Move 3
This move reduces the opponents defence""")
    print("""Move 4
This move heals you""")
    route()
def route():
    print("Press 1 to return")
    x = int(input())
    if x == 1:
        come_back()
    else:
        route()
def battle():
    player_attack = 100
    player_defence = 100
    user_health = 100
    enemy_health = 100
    enemy_attack = 100
    enemy_defence = 100
    while user_health > 0: 
     print("Which move do you perform (enter the number from 1 to 4)?")
     x = int(input())
     import random
     g = random.randint(0,40)
     if x == 1 and g < 30:
        if player_attack >= 70:
         if enemy_defence >= 80:
             enemy_health -= 10
             print("The enemy took 10 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 60:
             enemy_health -= 20
             print("The enemy took 20 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 40:
             enemy_health -= 30
             print("The enemy took 30 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 20:
             enemy_health -= 40
             print("The enemy took 40 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
        elif player_attack >= 40:
         if enemy_defence >= 80:
             enemy_health -= 5
             print("The enemy took 5 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 60:
             enemy_health -= 15
             print("The enemy took 15 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 40:
             enemy_health -= 25
             print("The enemy took 25 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 20:
             enemy_health -= 35
             print("The enemy took 35 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
        elif player_attack > 00:
         if enemy_defence >= 80:
             enemy_health -= 3
             print("The enemy took 3 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 60:
             enemy_health -= 10
             print("The enemy took 10 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 40:
             enemy_health -= 20
             print("The enemy took 20 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
         elif enemy_defence >= 20:
             enemy_health -= 30
             print("The enemy took 30 damage!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
     elif x == 2 and g < 30:
         enemy_attack -= 10
         print("The enemie's attack was lowered by 10!")
         print("Your health is " + str(user_health))
         print("The enemie's health is " + str(enemy_health))
     elif x == 3 and g < 30:
         enemy_defence -= 10
         print("The enemie's defence was lowered by 10!")
         print("Your health is " + str(user_health))
         print("The enemie's health is " + str(enemy_health))
     elif x == 4:
         if user_health == 100:
             print("Your health is already full!")
         else:
             user_health += 10
             print("You regained 10 hp!")
             print("Your health is " + str(user_health))
             print("The enemie's health is " + str(enemy_health))
     else:
         print("You missed!")
     print("The enemy is performing his move!")
     import random
     x = random.randint(0,110)
     z = enemy_attack / 10
     if enemy_health < 50:
         print("The enemy is now angry")
         enemy_attack += 20
         enemy_defence += 20
     if x < 40:
           if player_defence >= 80:
            user_health -= z
            a = 100 - user_health
            print("You took " + str(a) + " damage!")
            print("Your health is " + str(user_health))
            print("The enemie's health is " + str(enemy_health))
           elif player_defence >= 60:
            user_health -= z * 2
            a = 100 - user_health
            print("You took " + str(a) + " damage!")
            print("Your health is " + str(user_health))
            print("The enemie's health is " + str(enemy_health))
           elif player_defence >= 40:
            user_health -= z * 3
            a = 100 - user_health
            print("You took " + str(a) + " damage!")
            print("Your health is " + str(user_health))
            print("The enemie's health is " + str(enemy_health))
           elif player_defence >= 20:
            user_health -= z * 4
            a = 100 - user_health
            print("You took " + str(a) + " damage!")
            print("Your health is " + str(user_health))
            print("The enemie's health is " + str(enemy_health))
     elif x < 60:
        player_attack -= 10
        print("Your attack was lowered by 10!")
        print("Your health is " + str(user_health))
        print("The enemie's health is " + str(enemy_health))
     elif x < 80:
        player_defence -= 10
        print("Your defence was lowered by 10!")
        print("Your health is " + str(user_health))
        print("The enemie's health is " + str(enemy_health))
     elif x < 110:
        enemy_health += 10 
        print("The enemy regained 10 health!")
        print("Your health is " + str(user_health))
        print("The enemie's health is " + str(enemy_health))
     else:
        print("Move missed")
        print("Your health is " + str(user_health))
        print("The enemie's health is " + str(enemy_health))
     if enemy_health == 0:
         print("You Won!!")   
         route()
     elif user_health == 0:
         print("You Lost! :(  ")
def exit():
    print("Goodbye!")
def intro():
    print("Hello and welcome to this game!")
    print("""What do you want to do?
Press the corresponding number to perform the acttion
Moves(1) Battle(2) Exit(3)""")
    x = int(input())
    if x == 1:
        moves()
    elif x == 2:
        battle()
    elif x == 3:
        exit()
    else:
        print("Please enter the corresponding number only")
def come_back():
    print("""What do you want to do?
Press the corresponding number to perform the acttion
Moves(1) Battle(2) Exit(3)""")
    x = int(input())
    if x == 1:
        moves()
    elif x == 2:
        battle()
    elif x == 3:
        exit()
    else:
        print("Please enter the corresponding number only")
intro()
        


    
