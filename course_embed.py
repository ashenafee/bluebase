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
async def remove(ctx, *args):
    """Remove a course from the server."""

    if jdb.get_from_json(ctx.channel.id) != ValueError:

        course = cc.create_course(args[0], args[1])

        discord.Embed(title=f"Removed '{course.code}' from '{ctx.guild}:{ctx.channel}'",
                      description=f"'{course.name}' has been successfully removed from the server.",
                      color=0x00ff00)

    else:
        print("Nothing to remove! This course does not exist in the server.")


@client.command()
async def view(ctx, *args):
    """Shows the course's lec/pra/tut sections."""
    course = cc.create_course(args[0], args[1])
    embed = discord.Embed(title=course.code, description=course.name, color=0x00ff00)

    if args[2] == "LEC":
        lecs = ""
        for lec in course.lec:
            lecs += str(lec) + "\n"
        embed.add_field(name="Lectures", value=lecs, inline=False)
        await ctx.send(embed=embed)

    elif args[2] == "PRA":
        pras = ""
        for pra in course.pra:
            pras += str(pra) + "\n"
        embed.add_field(name="Practicals", value=pras, inline=False)
        await ctx.send(embed=embed)

    elif args[2] == "TUT":
        tuts = ""
        for tut in course.tut:
            tuts += str(tut) + "\n"
        embed.add_field(name="Tutorials", value=tuts, inline=False)
        await ctx.send(embed=embed)

    else:
        print("Invalid meeting type. Valid meeting types are LEC, PRA, TUT")


@client.command()
async def view_all(ctx: Context):
    """View a course."""
    course = jdb.get_from_json(ctx.channel.id)
    embed = discord.Embed(title=f"Courses for '{ctx.guild}:{ctx.channel}'",
                          color=0x00ff00)
    await ctx.send(embed=embed)
