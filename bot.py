import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to the discord server! If you need more info on the bt or the support server please join this: https://discord.gg/6eFXZQR')
    print('Sent message to ' + member.name)
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content == ';info':
        await client.send_message(message.channel,'This bot is multi purpose, it is a chat moderator and fun commands, (leveling may come soon.) It was made by enderman slayerr#6740')
    if message.content.startswith(';coinflip'):
        randomlist = ['heads','tails']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith(';ping'):
        await client.send_message(message.channel,'pong'  %(message.author.id))
    if ('fuck') in message.content:
       await client.delete_message(message)
    if ('shit') in message.content:
       await client.delete_message(message)
    if ('bitch') in message.content:
       await client.delete_message(message)
    if ('nigger') in message.content:
       await client.delete_message(message)
    if ('betch') in message.content:
       await client.delete_message(message)
    if ('cunt') in message.content:
       await client.delete_message(message)
    if ('wanchor') in message.content:
       await client.delete_message(message)
    if ('fucking') in message.content:
       await client.delete_message(message)
    if ('bullshit') in message.content:
       await client.delete_message(message)
    if ('dick') in message.content:
       await client.delete_message(message)
    if ('dickhead') in message.content:
       await client.delete_message(message)
    if ('tits') in message.content:
       await client.delete_message(message)
    if ('vagina') in message.content:
       await client.delete_message(message)
    if message.content.startswith(';joke'):
        randomlist = ['"dad im hungry" "hi hungry im ddad"','where do sheeps go to get their haircut? the baaaa- barbers','how do you prevent catching a summer cold? catch it in winter','what do planets like to read? comet books','i quit my job at a helium factory. dont speak to me in that tone.','what did sushi a say to sushi b? washabi!','whats the best thing about switzerland? i dont know but their flag is a plus.','I invented a new word! plagiarism!']
        await client.send_message(message.channel,(random.choice(randomlist)))
                      















client.run('NTMzMzQxODcyNDI5NTk2Njg3.DxppGQ.zHr5U7fYNwXG5ynUouWG43cHMBw')
