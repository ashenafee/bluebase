import discord
from discord.ext import commands

client = commands.Bot(command_prefix='?')

client.command()


async def embed(ctx):
    embed = discord.Embed(title="Course", url="https://artsci.calendar.utoronto.ca/search-courses",
                          description="You can access the UofT courses from the link above",
                          color=discord.Color.blurple())

    await ctx.send(embed=embed)

    embed.set_author(name=ctx.author.display_name, icon_url=ctx.author.avatar_url)

    embed.set_thumbnail(url="https://ontariosuniversities.ca/impact/award-winners/autism-scholars-award-2018/"
                            "uoft-logo-1")
