import datetime
import discord
from discord.ext import commands
import random

# The Command Prefix
COMMAND_PREFIX = ">"

bot = commands.Bot(command_prefix=COMMAND_PREFIX)
logFile = open("data/log.txt", "a")

def log(logMsg):
    print(f"[{datetime.datetime.now()}] {logMsg}")
    logFile.write(f"[{datetime.datetime.now()}] {logMsg}\n")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"Listening for {COMMAND_PREFIX}help | prefix is \"{COMMAND_PREFIX}\" "))
    log("Bot is ready.")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, Welcome to Programmer's Cafe :>")

    log(f"{member.name} joined.")

@bot.event
async def on_message(message):
    content = message.content 
    channel = message.channel 
    user = message.author.name 
    userID = message.author.id


    # if anyone says the stuff included in this list the bot will reply
    badWords = ["fuck", "f*ck"]
    if not user.lower() == "arkydarky":
        for badWord in badWords:
            if badWord in content.lower():
                await channel.send(f"<@{userID}> 😠")

# the 8ball command
@bot.command(aliases=['8ball'])
async def eightball(ctx, *, arg):
    answers = [
    "As I see it, yes.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "It is certain.",
    "It is decidedly so.",
    "Most likely.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Outlook good.",
    "Reply hazy, try again.",
    "Signs point to yes.",
    "Very doubtful.",
    "Without a doubt.",
    "Yes.",
    "Yes – definitely.",
    "You may rely on it."
    ]
    response = f"Question: {arg}\nAnswer: {random.choice(answers)}"
    await ctx.send(response)
    # print and log stuff
    log("8ball command has been used.")

with open('data/token.txt','r') as my_token:
    token = my_token.read()

bot.run(token)
