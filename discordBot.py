import discord
import openai
import os

# import to use .env file.
import dotenv
from dotenv import load_dotenv

# importing commands .
from discord.ext import commands

# allows bot to access the content of the messages
intent = discord.Intents.default()
intent.message_content = True

# loads .env file located on the same level of this script.
load_dotenv()

# get both discord token and open api key from .env file.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

# creating new bot object
bot = commands.Bot(command_prefix=commands.when_mentioned_or("/"), intents=intent)


# message to log when the bot is up and running.
@bot.event
async def on_ready():
    print("I'm ready!")
    print("------------------")
    print("I'm in " + str(len(bot.guilds)) + " servers")

# bot will respond to @ mentions
@bot.event
async def on_message(msg):
    # strips the bots name and leading/trailing white spaces.
    try:
        message_req = msg.content.split(" ", 1)[1].strip()
    except IndexError:
        # insert a generic message to send to openai
        message_req = "I have a question for you"
    if bot.user.mentioned_in(msg) and message_req:
        # calling open ai
        ai_response = openai.Completion.create(
            model="text-davinci-003",
            prompt=message_req,
            temperature=1,
            max_tokens=4000,
        )
        # parse for the response text
        ai_response_msg = ai_response.choices[0].text
        await msg.channel.send(ai_response_msg)


# executes the bot with token located in .env file.
bot.run(DISCORD_TOKEN)
