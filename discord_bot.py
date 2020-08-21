from discord.ext import commands
import discord
import asyncio

import rundiscord

bot = commands.Bot(command_prefix='!!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)  # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id)  # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')


@bot.command()
async def sine(ctx):
    user = ctx.message.author
    voice_channel = user.voice
    channel = None

    if voice_channel is not None:
        vc = await ctx.author.voice.channel.connect()
        await ctx.send('sine')

        vc.play(discord.FFmpegPCMAudio(sine()), after=lambda e: print('done', e))

        while not vc.is_playing():
            await asyncio.sleep(1)

        await vc.disconnect()
    else:
        await ctx.send('User is not in a channel.')


# @bot.command()
# async def join(ctx):
#     channel = ctx.author.voice.channel
#     await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


@bot.command()
async def ping(ctx):
    ping_ = bot.latency
    ping = round(ping_ * 1000)
    await ctx.send(f"my ping is {ping}ms")


rundiscord.rundiscordbot(bot)
