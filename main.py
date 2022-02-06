import os

import discord
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands.context import Context

import course_creator as cc
import json_database as jdb

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
async def ping(ctx: Context):
    """Output pong to the server."""
    await ctx.send("Pong!")


@client.command()
async def add(ctx: Context, *args):
    """Add a course to the server."""
    course = cc.create_course(args[0], args[1])
    embed = discord.Embed(title=f"Added '{course.code}' to '{ctx.guild}:{ctx.channel}'",
                          description=f"'{course.name}' has successfully been added to the server.",
                          color=0x00ff00)
    jdb.save_to_json(ctx.channel.id, course.code)

    await ctx.send(embed=embed)


@client.command()
async def view_all(ctx: Context):
    """View a course."""
    course = jdb.get_from_json(ctx.channel.id)
    embed = discord.Embed(title=f"Courses for '{ctx.guild}:{ctx.channel}'",
                          description=f"",
                          color=0x00ff00)
    await ctx.send(embed=embed)



# Login to the bot
client.run(TOKEN)