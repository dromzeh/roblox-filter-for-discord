<p align = center>
    <img src="https://i.imgur.com/2V1ri5t.gif" alt="hi">
</p>
    <h1 align = center>roblox filter for discord</h1>
    <h3 align = center>a discord bot that changes 'banned' words into ########
</h2>

<p align = center>
    <img src = "https://img.shields.io/github/last-commit/dromzeh/roblox-filter-for-discord" alt = "checks">
    <img src = "https://img.shields.io/badge/python-3.8%2B-informational" alt = "python">
    <img src = "https://img.shields.io/badge/discord.py-latest-blueviolet" alt = "dpy">
    <img src = "https://img.shields.io/badge/license-MIT-orange" alt = "MIT">
</p>

## note: i have not been working on this project for a while, if there are any issues at all or no longer works correctly, please open an issue

# requirements

you only need `discord.py` (`pip install discord.py`) to run this & a python version which supports discord.py

# setup guide

- download this repository, edit `cfg/config.json` with your bot token, webhook url + channel id. you can leave the prefix the same as the bot currently has no commands.
- edit `bannedwords.txt` with the list of banned words, (scroll further down in the readme for more help)
- invite the bot to your server, run the bot *(open terminal of choice in bot directory -> py bot.py)*

# getting channel id, creating a bot & making a webhook

- to get the channel id, enable developer mode in discord settings, right click on the channel you're 'filtering' and copy the id.

- to create a bot, go onto the discord developer portal, make an application and make it a bot, then copy the bot token and put it into the file, **don't give this token to anyone** (in a worst case scenario and you do, just regenerate it!)

- to make a webhook, go into `server settings > integrations > new webhook`, the **webhook name does not matter, nor does the profile picture** (this gets automatically changed), set the webhook channel to the channel you are 'censoring', then simply copy the url and enter it into the bot.py

# adding custom filter words

- the built in filter words are just `hello` and `world` until you modify the `bannedwords.txt` (keep this file in the same directory as `bot.py`), enter all the words you want to enter and put a space between each banned word, so your bannedwords.txt might be looking like this:
`hello world 123 456`
- in this example, it means, 'hello' 'world' '123' '456' are all censored words

# other issues

- if the bot isn't deleting your message, make sure the bot has administrator permissions.
- if the webhook isn't working (##### isn't appearing), make sure that it is going to the correct channel, and you entered everything in correctly
- any other errors will output in console, google can help you with those, if you're still struggling, just open an issue on this repo.

# todo

- [ ] : completely rewrite the code
