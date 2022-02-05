import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import course_creator as cc

client = commands.Bot(command_prefix='!')
client.remove_command('help')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


@client.event
async def on_connect():
    print("Bluebase has connected to Discord.")


@client.event
async def on_ready():
    print("Bluebase is up and running.")
    await client.change_presence(
        activity=discord.Game(name="Type !help for a list of commands!"))


@client.command()
async def ping(ctx, *args):
    """Output pong to the server."""
    await ctx.send("Pong!")


@client.command()
async def add(ctx, *args):
    """Add a course to the server."""
    course = cc.create_course(args[0], args[1])
    embed = discord.Embed(title=course.code, description=course.name, color=0x00ff00)

    lecs = ""
    for lec in course.lec:
        lecs += str(lec) + "\n"
    embed.add_field(name="Lectures", value=lecs, inline=False)

    await ctx.send(embed=embed)


# Login to the bot
client.run(TOKEN)