import discord
import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
Discord_Token=os.getenv("Discord_key")
G_Token=os.getenv("G_key")
Open_Token=os.getenv("OpenAI")


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if client.user != message.author:
        if client.user in message.mentions:

            # The client gets the API key from the environment variable `GEMINI_API_KEY`.
            client_google = genai.Client(api_key=G_Token)

            response = client_google.models.generate_content(
                model="gemini-2.5-flash", contents=message.content
            )
            print(response.text)
            await message.channel.send(response.text)

client.run(Discord_Token)