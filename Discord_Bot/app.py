import requests
import discord
import time

client = discord.Client()

async def send_message(message):
    channel = client.get_channel()#add channel ID here
    await channel.sent(message)

client.run('') #add Discord bot ID here

