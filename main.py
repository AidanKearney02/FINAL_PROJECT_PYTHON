
import json
import random
import time

import discord
import requests

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
TOKEN = "MTE4Mzg0ODY3NTk2MTc0NTQ1OA.GRW9Ot.keFwipfHCVakjDp6JeHGCH5MbpLuhlI9NzkZQw"
list_of_memes=[]
def memes_generator():

  url = "https://reddit3.p.rapidapi.com/v1/reddit/subreddit"

  querystring = {"url":"https://www.reddit.com/r/memes","filter":"new"}

  headers = {
    "X-RapidAPI-Key": "517f95d594mshc3455967d437879p1d11f4jsnb7a447328156",
    "X-RapidAPI-Host": "reddit3.p.rapidapi.com"
  }

  response = requests.get(url, headers=headers, params=querystring)

  api_return=json.loads(response.text)
  body=api_return['body']

  for post in body:
    if post["is_video"] is True:
      list_of_memes.append(post['media']['reddit_video']['scrubber_media_url'])
    else:
      list_of_memes.append(post['url'])


grettings = ["hi", "hello", "hey", "helloo", "hellooo", "g morining", "gmorning"]
def choose_randomly(list):
  return random.choice(list)

@bot.event
async def on_message(message):
  if message.content.upper()=='HEY MEME BOT':
    user=message.author
    await message.channel.send(choose_randomly(grettings) + user.mention)
  if 'send memes' in message.content.lower():
    old_list = list_of_memes.copy()
    memes_generator()
    for meme in list_of_memes:
      if meme not in old_list:
        await message.channel.send(meme)
        time.sleep(5)

bot.run(TOKEN)