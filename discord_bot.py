import asyncio
import discord

client = discord.Client()


class bot:
    def __init__(self):
        self.token = ""

    @client.event
    async def on_ready(self):
        print(f"{client.user} has connected.")

    def run(self):
        client.run(self.token)
