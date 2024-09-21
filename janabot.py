import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True
intents.members = True

gif_url = 'https://tenor.com/view/jana-gif-3018823685277907379'
gif_count = dict()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'I am awake! Logged in as {bot.user}')
    channel = bot.get_channel(1283517374057681087)

    file = open('count.txt', 'r')
    message = "I am awake now!\nHere is what I remember from last time, sorry if it's not accurate UwU 🥺👉👈\n"
    for line in file:
        member_count = line.split(',')
        message += member_count[0] + " -> " + member_count[1]
        gif_count[member_count[0]]  = int(member_count[1].strip())

    
    channel.send(message)
    file.close()



trans_count = 0

@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    global trans_count

    # Check if the message contains any attachments
    #     for attachment in message.attachments:
    #         # Check if the attachment is a GIF and the URL matches the specific one
    #         if attachment.url.endswith('.gif') and attachment.url == gif_url:
    if message.content == gif_url:

        trans_count += 1
        await message.add_reaction('❤️')
        user_id = str(message.author.name)
        if user_id in gif_count:
            gif_count[user_id]  += 1
        else:
            gif_count[user_id]  = 1
        
        if (not user_exist_in_file(user_id)):
            append_file(user_id, gif_count[user_id])
        
        await message.channel.send(f"<@{message.author.id}>, you have used this gif {gif_count[user_id]} times! UwU RAWR XD") 

        if trans_count == 10:
            trans_count = 0
            update_file()
    
    # Process commands if any
    await bot.process_commands(message)


def user_exist_in_file(name):
    with open('count.txt', 'r') as file:
        names = [line.split(',')[0] for line in file.readlines()]
    return name in names

def append_file(user_id, count):
    with open('count.txt', 'a') as file:
        file.write(user_id + ',' + str(count) + '\n')

def update_file():
    with open('count.txt', 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        curr = lines[i].split(',')[0]
        lines[i] = curr + ',' + str(gif_count[curr]) + '\n'

    with open('count.txt', 'w') as file:
        file.writelines(lines)

with open('cred.txt', 'r') as file:
        lines = file.readlines()
bot.run(lines[0].strip())


# @bot.event