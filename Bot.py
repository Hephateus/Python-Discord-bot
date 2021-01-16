import discord
from discord.ext import commands

client = commands.bot(command_prefix = "Your bot's Prefix")

@client.event
async def on_ready():
    print("The bot is ready.")
		# if the bot is ready it will send the message below
		
@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")
		
client.run("Your bot's token")
