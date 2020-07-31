from discord.ext import commands, tasks

bot = commands.Bot(command_prefix='!!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)  # 토큰으로 로그인 된 bot 객체에서 discord.User 클래스를 가져온 뒤 name 프로퍼티를 출력
    print(bot.user.id)  # 위와 같은 클래스에서 id 프로퍼티 출력
    print('------')


@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


async def _join(self, ctx: commands.Context):
    """Joins a voice channel."""

    destination = ctx.author.voice.channel
    if ctx.voice_state.voice:
        await ctx.voice_state.voice.move_to(destination)
        return

    ctx.voice_state.voice = await destination.connect()


bot.run("NTI2ODA1MzM0ODc5MTA5MTQz.XCEPsw.6-3e3RpKGEDa28orfgdfVNxPOM0")
