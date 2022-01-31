import random
import time

def attack(user, select_attack):
    PunchDamage = random.randint(5,40)
    KickDamage = random.randint(10,35)
    HeadbuttDamage = random.randint(15,30)
    punch = PunchDamage
    kick = KickDamage
    headbutt = HeadbuttDamage
    attack = select_attack
    if attack == "k":
        attack = kick
    elif attack == "p":
        attack = punch
    elif attack == "h":
        attack = headbutt
    else: 
        print("enter a proper attack")
    attackpoints = attack
    return attackpoints

Player1Health = 100
Player1IsAlive = Player1Health > 0
PlayerName = input("what is your name?\n")
time.sleep(1)
print("-------Attack Selection Menu-------\nType 'k' to kick.\nType 'p' to punch.\nType 'h' to headbutt.")
time.sleep(1)
proceed = input("Enter any key to continue\n")
time.sleep(1)
choose_opponent = input("Enter number to choose your opponent.\n1 --> Philip\n2 --> Sandra\n3 --> Tiana\n4 --> Pierre\n")
if choose_opponent == "1":
        BotName = "Philip"
if choose_opponent == "2":
        BotName = "Sandra"
if choose_opponent == "3":
        BotName = "Tiana"
if choose_opponent == "4":
        BotName = "Pierre"

BotHealth = 100
BotIsAlive = BotHealth > 0
attacks = ("kick", "punch", "headbutt")

while BotIsAlive and Player1IsAlive == True:
        playerattack = input("Choose your attack {}:\n".format(PlayerName))
        playerattackpoints = attack(user= PlayerName, select_attack = playerattack)
        BotHealth = BotHealth - int(playerattackpoints)
        print("{} did {} of damage to {}".format(PlayerName, playerattackpoints, BotName))
        time.sleep(1)
        print("player health is currently: ", Player1Health, "\nbot health is currently: ",BotHealth)
        print("______________________________")      
        time.sleep(1)  
        attacks = ("k", "h", "p")
        bot_attack = random.choice(attacks)
        botattackpoints = attack(user= BotName, select_attack= bot_attack)
        print("{} chose {} and did {} points of damage ".format(BotName,bot_attack,botattackpoints))
        Player1Health = Player1Health - int(botattackpoints)
        time.sleep(1)
        print("player health is currently: ", Player1Health, "\nbot health is currently: ",BotHealth)
        print("______________________________")
if BotHealth <= 0:
        BotIsAlive == False
        print("Game over. {} lost the fight.".format(BotName))
elif Player1Health <= 0:
        Player1IsAlive == False
        print("Game over. {} lost the fight.".format(PlayerName))







