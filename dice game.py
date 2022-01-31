import random
import string

NumberOfRolls = 1
counter = 0
BotRoll = NumberOfRolls == 1
set = '' 
while counter < NumberOfRolls:
        roll_dice_float = random.uniform(1, 6)
        number = int(roll_dice_float)
        if counter < NumberOfRolls - 1:
            set += str(number) + ', '
            counter += 1
        else: 
            set += str(number)
            counter += 1
if NumberOfRolls == 1:
    print("You rolled a ", set)

roll_dice_float = random.uniform(1, 6)
bot_num = int(roll_dice_float)
bot_roll_num = str(bot_num)

if BotRoll:
    print("I rolled a ", bot_roll_num)
    if set > bot_roll_num and BotRoll:
        print("You win.")
    elif set == bot_roll_num and BotRoll:
        print("Its a draw.")
    else: 
        print("I win.")
if not BotRoll:
    print("You rolled more than once I'm not playing anymore.")

