from openai import OpenAI
from google import genai

import discord
from dotenv import load_dotenv

import os

load_dotenv()
apikey = os.getenv("API-KEY")
apikeygoogle = os.getenv("GOOGLE-API-KEY")
apikeyopen_ai = os.getenv("OPEN-KEY")


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client_google = genai.Client(api_key=apikeygoogle)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if client.user != message.author:
        if client.user in message.mentions:

            channel = message.channel

            # response = client_google.models.generate_content(
            #     model="gemini-2.5-flash", contents=message.content
            # )
            # print(response.text)

            client_open_ai = OpenAI(api_key=apikeyopen_ai)

            response = client_open_ai.responses.create(
                model="gpt-5.1",
                input=message.content
            )

            print(response.output_text)


            await channel.send(response.output_text)


client.run(apikey)
