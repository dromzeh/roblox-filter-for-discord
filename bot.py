# Copyright © 2023 dromzeh
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# https://dromzeh.mit-license.org/

import discord # discord.py
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import guild_only
from aiohttp import ClientSession # used to make requests to the webhook
import json

# opens bannedwords.txt and sets it as a global variable
with open('bannedwords.txt', 'r') as x:
    global bannedwords
    words = x.read()
    bannedwords = words.split()

with open ('cfg/config.json', 'r') as x:
    config = json.load(x)
    TOKEN = config['TOKEN']
    PREFIX = config['PREFIX']
    WEBHOOK_URL = config['WEBHOOK_URL']
    CHANNEL_ID = config['CHANNEL_ID']

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=PREFIX, intents=intents)
bot.remove_command('help')

# on ready event (when bot finishes loading, etc etc)
@bot.event
async def on_ready():
    print(f'logged in as {bot.user.name} [{bot.user.id}]')
    print('bot coded by dromzeh @ https://github.com/dromzeh licensed under MIT')

# on message event
@bot.event
async def on_message(message):
    msg = message.content.lower()
    channel = message.channel
    if channel.id == CHANNEL_ID:
        for word in bannedwords:
            if word in msg:
                await message.delete()
                messagelength = len(msg)
                async with ClientSession() as cs:
                    webhook = discord.Webhook.from_url(WEBHOOK_URL, adapter=discord.AsyncWebhookAdapter(cs))
                    await webhook.send(content="#" * messagelength, username=message.author.name, avatar_url=message.author.avatar_url) 

# running bot
bot.run(TOKEN)
