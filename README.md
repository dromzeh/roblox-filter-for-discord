<p align = center>
<img src="https://i.imgur.com/2V1ri5t.gif" alt="hi">
</p>
<h1 align="center">roblox filter for discord</h1>
<h3 align ="center">a literal discord bot that does nothing except changed banned words into ######## ¯\_(ツ)_/¯
</h2>

<p align = center>
<img src="https://img.shields.io/github/last-commit/dromzeh/roblox-filter-for-discord" alt="checks">
<img src="https://img.shields.io/badge/python-3.8%2B-informational" alt="python">
<img src="https://img.shields.io/badge/discord.py-latest-blueviolet" alt="dpy">
</p> 

# requirements
you only need `discord.py` (pip install discord.py in cmd prompt) to run this, and a python version which supports discord.py

# setup guide
- download this repository, edit `bot.py` and edit lines 20-22 with your bot token, webhook url + channel id.
- edit `bannedwords.txt` with the list of banned words, (scroll further down in the readme for more help)
- invite the bot to your server, run the bot *(open command prompt in bot directory -> py bot.py)*

# idk how to get a webhook url, channel id or a bot token!! help pls
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
