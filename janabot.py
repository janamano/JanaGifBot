import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

gif_url = 'https://tenor.com/view/jana-gif-3018823685277907379'
gif_count = dict()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'I am awake! Logged in as {bot.user}')


@bot.event
async def on_message(message):
    # Prevent the bot from responding to its own messages
    if message.author == bot.user:
        return

    # print(message)
    # print(message.content)
    # print(message.attachments)
    # print(message.author)

    # Check if the message contains any attachments
    #     for attachment in message.attachments:
    #         # Check if the attachment is a GIF and the URL matches the specific one
    #         if attachment.url.endswith('.gif') and attachment.url == gif_url:
    if message.content == gif_url:
        await message.add_reaction('❤️')
        user_id = str(message.author.id)
        if user_id in gif_count:
            gif_count[user_id]  += 1
        else:
            gif_count[user_id]  = 1
        await message.channel.send(f"<@{message.author.id}>, you have used this gif {gif_count[user_id]} times! UwU RAWR XD") 

    # Process commands if any
    await bot.process_commands(message)

bot.run('MTI4NDIyNzQwNDk3NzY3MjIxMg.GYmGk4.5Kg2crJHedILaAupPsn6f3YHm4z3Tw0vONaO20')


# @bot.event