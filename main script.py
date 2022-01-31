import discord
from discord import channel
from discord.ext import commands
import requests
import random
""" import nasapy
import pandas
 """


intents = discord.Intents.default()
intents.members = True
intents.reactions = True
intents.messages = True
print("intents.members = {}\nintents.reactions = {}\nintents.messages = {}".format(intents.members, intents.reactions, intents.messages))

client = commands.Bot(command_prefix = '.')
print('client variable set')
print(client.intents)

HighlightsChannelID = 823641460892893225
OverallColorScheme= 0x7289da
LogChannel = 828304682203217921

#---Role Variables---#
roleMessageChannelID = 844872369453269013
roleMessageID = 847445685418983466
roleProducer = 841001899100209193
roleArtist = 841001937691344917
roleFriend = 841001970369953812

#print ready when bot says its awake
@client.event 
async def on_ready():
    print('bot is ready.')


#-----------------Random Things-------------------

@client.command() # generate avum name
async def avum(ctx):
    part1 = ["Ay", "Ey", "A ", "Ai", "A", "Aye", "Bae", "Bae ", "Nay", "I'm "]
    x = random.choice(part1)
    part2 = ["v", "p", "b", "ph", "r", "br", "c", "ch", ""]
    y = random.choice(part2)
    part3 = ["a", "i", "o", "e", "u", "yu", "oo"]
    z = random.choice(part3)
    part4 = ["m", "n", ""]
    a = random.choice(part4)
    your_name_is = "Your name today is: "
    base_name = x + y + z + a
    nick_message = your_name_is + base_name
    await ctx.send(nick_message)

@client.command()  # generate random names
async def name(ctx):
    #consonant variable
    vowel1 = random.choice('aeiou')
    if vowel1 == 'e' or 'o':
        vowel1 = vowel1
    else:
        vowel1 = vowel1
    vowel2 = random.choice('aeiou')
    if vowel2 == 'e' or 'o':
        vowel2 = vowel2
    else:
        vowel2 = vowel2
    vowel1 = vowel1
    vowel2 = vowel2
    upper_letter = ('ABCDFGHJKLMNPRSTVW')
    #upper case variable
    upper = random.choice(upper_letter)  #upper case variable
    consonant1 = random.choice('bcdfghjklmnpqrstvw')
    consonant2 = random.choice('bcdfghjklmnpqrstvw')
    your_name_is = "Your name today is: "
    base_name = upper + vowel1 + consonant1 + vowel2 + consonant2
    nick_message = your_name_is + base_name
    await ctx.send(nick_message)

@client.command() # say hi when command + hello used
async def hello(ctx):
    await ctx.send("hey how's it going.")

@client.command() # say BAH when command + goat used
async def goat(ctx):
    await ctx.send("BAH \n ")

@client.command() # say take that when command + headbutt used
async def headbutt(ctx):
    await ctx.send("Take that!!")

@client.command() #Dice game
async def roll(ctx):
    user = ctx.author.avatar_url
    user_display = ctx.author.display_name
    print(user)
    NumberOfRolls = 1
    counter = 0
    BotRoll = NumberOfRolls == 1
    while BotRoll and counter < 1:
        counter += 1
        user_roll = random.uniform(1, 6)
        user_roll = int(user_roll)
        bot_roll = random.uniform(1, 6)
        bot_roll = int(bot_roll)
        if user_roll > bot_roll:
            message = "You rolled: {}\nI rolled: {}\nYou win.".format(user_roll, bot_roll)
            outcome = "won"
        if user_roll == bot_roll:
            message = "You rolled: {}\nI rolled: {}\nIt's a draw.".format(user_roll, bot_roll)
            outcome = "got a draw"
        if user_roll < bot_roll:
            message = "You rolled: {}\nI rolled: {}\nI win.".format(user_roll, bot_roll)
            outcome = "lost"
    embed = discord.Embed(title= ('{} rolled the dice and {}.'.format(user_display, outcome)), description= message, color=OverallColorScheme)
    embed.set_thumbnail(url= user)
    await ctx.send(content = None, embed=embed)

@client.command()
async def nasa(ctx, spec):
    nasa = Nasa()
    if spec == "daily":
        payload = nasa.picture_of_the_day()
        str.payload()
        await ctx.send(payload)

#---------------Moderation and Admin features-------------------

@client.command() #display role recation message
async def roles(ctx):
    role_embed = discord.Embed(
        title="Avum's Garage",
        description=
        "You can use the reactions on this message to pick up any roles you feel represent you. Just click on the specified reaction on this message to be assigned the associated role",
        color=OverallColorScheme)
    role_embed.add_field(
        name="------------------------------------",
        value=
        "🎵 ---- roleProducer \n\n🎨 ---- roleArtist \n\n😊 ---- roleFriend")
    print("First embed executed.\nContent of embed is: ", role_embed)
    #await ctx.send(content='roleMessageID', embed=role_embed)
    channel = client.get_channel(roleMessageChannelID)
    await channel.send(content = 'roleMessageID', embed=role_embed)
    reactionRoleEmbed = role_embed
    await ctx.send(role_embed.to_dict())


#@client.event() # assign roles to user based on reaction
#async def on_raw_reaction_add(payload):



@client.command() # welcome page config
async def config(ctx):
    embed = discord.Embed(
        title="__**Avum's Garage**__",
        description=
        "Scraic chaps.\nSo basically this is a kinda place to hang out and talk music stuff and graphic design.\nThis will continue to be updated as things change and amendments are required.Welcome to the server. \nHere is some information about this server to get you started.\n ",
        color=OverallColorScheme)
    embed.set_thumbnail(
        url=
        "https://i.scdn.co/image/e6632c7f8566c9c0cbc6282a20e80ccfce8f389d")
    embed.add_field(
        name="__                                             __",
        value=
        "\n```Rules```\n\n__**Do**__\n:white_check_mark: Respect different music tastes.\n:white_check_mark: Try your best to keep topics inside the appropriate chat.\n:white_check_mark: Contact @admin if somebody says something which upsets you.\n:white_check_mark: Try to use Predominantly English to communicate.\n\n__**Don't**__\n:no_entry_sign: Post offensive content.\n:no_entry_sign: Post illegal/leaked/paid content.\n:no_entry_sign: Spam.\n:no_entry_sign: Harass people.\n\n```Socials```\n:sound: **[Soundcloud](https://soundcloud.com/avum1)**\n\n:bird: **[Twitter](https://twitter.com/avummusic)**\n\n:camera: **[Instagram](https://www.instagram.com/avummusic/)**\n\n:musical_note: **[Spotify](https://open.spotify.com/artist/28cGoHsdbIVbVdUko7KtYk?si=46mBKRX2T7-zC_-5W3KN1Q)**\n\n\n**Invite your friends using this link**\n\n**https://discord.gg/49Whbj6h3V**")
    embed.set_image(
        url="https://i1.sndcdn.com/visuals-000067269613-Ey6pZX-original.jpg"
    )
    print("First embed executed.\nContent of embed is: ", embed)
    await ctx.send(content=None, embed=embed)
    embed = discord.Embed(
        title="Invite your friends using this link.",
        description="\n **https://discord.gg/49Whbj6h3V**",
        color=OverallColorScheme)
    embed.set_image(
        url="https://i1.sndcdn.com/visuals-000067269613-Ey6pZX-original.jpg"
    )
    print("Second embed executed.\nContent of embed is: ", embed)
    await ctx.send(content=None, embed=embed)

@client.command() #delete x number of messages from channel
async def clear(ctx, amount=10):
    amount = amount + 1
    await ctx.channel.purge(limit=amount)

@client.command()
async def say(ctx, say="say something"):
    await ctx.send(say)

@client.command()
async def info(ctx):
    await ctx.send(message)

@client.event #when certain reaction added do something
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    channel = client.get_channel(LogChannel)
    logMessage = "**Payload content is:**\n```py\n{}\n```\n**Message content is:**\n```\n{}\n```".format(payload, message.content)

    await channel.send(logMessage)
    await channel.send(message)
    print(message)
    if payload.emoji.name == '👍':  #thumb reaction to send message to highlight channel 
        channel = client.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = client.get_user(payload.user_id)
        reaction = payload.emoji
        message_content = message.content
        print("message content is ", message.content )
        author = message.author
        print('channel content is: {}\nmessage content is: {}\nuser is: {}\nreaction is: {}\nmessage author is: {}'.format(channel, message_content, user, reaction, author))

        embed = discord.Embed(
            title= author.display_name, 
            description= message_content, 
            color=OverallColorScheme)
        message_url = message.jump_url
        embed.add_field(name= "----------", value= ("[jump to message]({})".format(message_url)))
        embed.set_thumbnail(url = author.avatar_url)
        channel = client.get_channel(HighlightsChannelID) #channel = reaction.message.channel #channel to send message
        await channel.send(content = None, embed=embed)

    if payload.emoji.name == '🙏':  #silly reaction thing - maybe make this more useful
        channel = client.get_channel(payload.channel_id)
        await channel.send('Praise the lord! 🙏')
        
    if payload.message_id == roleMessageID:
        reaction = payload.emoji.name
        user = payload.user_id
        if payload.emoji.name == '🎵':
            role = roleProducer
        if payload.emoji.name == '🎨':
            role = roleArtist
        if payload.emoji.name == '😊':
            role = roleArtist
        
        channel = client.get_channel(payload.channel_id)
        await channel.send('reaction is {}\n user is {}\nrole required is {}').format(reaction, user, role)       

""" 
#user score board
@client.command()
async def users(ctx):
    list = ''
    for user in guild:
        list += user +"\n" 
    await ctx.send(list) """
""" 
@client.command()
async def search(ctx, feature):
    await ctx.send(feature) """


#client.run runs the bot.
client.run('ODI2Nzg2NzUyMDE3ODU4NTYy.YGRjKg.xAkhMHgMM-wMfYAfrFONJqcsndM') #this is the bot token.

# backup config embed code
""" @client.command() # welcome page config 
async def config(ctx):
    embed = discord.Embed(
        title="Avum's Garage",
        description=
        "Scraic chaps.\nSo basically this is a kinda place to hang out and talk music stuff and graphic design.\nThis will continue to be updated as things change and amendments are required.Welcome to the server. \nHere is some information about this server to get you started.\n ",
        color=OverallColorScheme)
    embed.set_thumbnail(
        url=
        "https://i.scdn.co/image/e6632c7f8566c9c0cbc6282a20e80ccfce8f389d")
    embed.add_field(
        name="------------------------------------",
        value=
        "```Rules```\n***Do***\n:white_check_mark: Respect different music tastes.\n:white_check_mark: Try your best to keep topics inside the appropriate chat.\n:white_check_mark: Contact @admin if somebody says something which upsets you.\n:white_check_mark: Try to use Predominantly English to communicate.\n\n***Don't***\n:no_entry_sign: Post offensive content.\n:no_entry_sign: Post illegal/leaked/paid content.\n:no_entry_sign: Spam.\n:no_entry_sign: Harass people.\n\n```Socials```\n:sound: **[Soundcloud](https://soundcloud.com/avum1)**\n\n:bird: **[Twitter](https://twitter.com/avummusic)**\n\n:camera: **[Instagram](https://www.instagram.com/avummusic/)**\n\n:musical_note: **[Spotify](https://open.spotify.com/artist/28cGoHsdbIVbVdUko7KtYk?si=46mBKRX2T7-zC_-5W3KN1Q)**")
    embed.set_image(
        url="https://i1.sndcdn.com/visuals-000067269613-Ey6pZX-original.jpg"
    )
    print("First embed executed.\nContent of embed is: ", embed)
    await ctx.send(content=None, embed=embed)
    embed = discord.Embed(
        title="Invite your friends using this link.",
        description="\n **https://discord.gg/49Whbj6h3V**",
        color=OverallColorScheme)
    embed.set_image(
        url="https://i1.sndcdn.com/visuals-000067269613-Ey6pZX-original.jpg"
    )
    print("Second embed executed.\nContent of embed is: ", embed)
    await ctx.send(content=None, embed=embed) """