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

    if len(args) == 2 and args[1].upper() in ["F", "S", "Y"]:
        try:
            course = cc.create_course(args[0], args[1])
            embed = discord.Embed(title=f"Added '{course.code}' to '{ctx.guild}'",
                                  description=f"'{course.name}' has successfully been added to <#{ctx.channel.id}>.",
                                  color=0x00ff00)
            jdb.save_to_json(ctx.channel.id, course.code)

            await ctx.send(embed=embed)
        except ValueError:
            embed = discord.Embed(title="Error",
                                  description=f"Section '{args[1].upper()}' does not exist for '{args[0].upper()}'.",
                                  color=0xff0000)
            await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="Invalid section type.", color=0xff0000)
        embed.add_field(name="Valid usage", value="`!add <CODE> <SECTION>`", inline=False)
        embed.add_field(name="Valid sections", value="`F`, `S`, `Y`", inline=False)
        await ctx.send(embed=embed)


@client.command()
async def remove(ctx: Context, *args):
    """Remove a course from the server."""
    if len(args) == 1:
        course = cc.create_course(args[0], "S")
        jdb.remove_from_json(ctx.channel.id, course.code)
        embed = discord.Embed(title=f"Removed '{course.code}' from '{ctx.guild}'",
                              description=f"'{course.name}' has successfully been removed from <#{ctx.channel.id}>.",
                              color=0x00ff00)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title="Error", description="Invalid usage.", color=0xff0000)
        embed.add_field(name="Valid usage", value="`!remove <CODE>`", inline=False)
        await ctx.send(embed=embed)


@client.command()
async def view(ctx, *args):
    """Shows the course's lec/pra/tut sections."""
    if len(args) != 2 or args[1].upper() not in ["LEC", "PRA", "TUT"]:
        embed = discord.Embed(title="Error", description="Invalid section type.", color=0xff0000)
        embed.add_field(name="Valid usage", value="`!view <CODE> <SECTION> <TYPE>`", inline=False)
        embed.add_field(name="Valid sections", value="`F`, `S`, `Y`", inline=False)
        embed.add_field(name="Valid types", value="`LEC`, `PRA`, `TUT`", inline=False)
        await ctx.send(embed=embed)

    try:
        course = cc.create_course(args[0], args[1])
    except ValueError:
        embed = discord.Embed(title="Error",
                              description=f"Section '{args[1].upper()}' does not exist for '{args[0].upper()}'.",
                              color=0xff0000)
        await ctx.send(embed=embed)
    except IndexError:
        embed = discord.Embed(title="Error", description="Invalid usage.", color=0xff0000)
        embed.add_field(name="Valid usage", value="`!view <CODE> <SECTION> <TYPE>`", inline=False)
        embed.add_field(name="Valid sections", value="`F`, `S`, `Y`", inline=False)
        embed.add_field(name="Valid types", value="`LEC`, `PRA`, `TUT`", inline=False)
        await ctx.send(embed=embed)

    embed = discord.Embed(title=course.code, description=course.name, color=0x00ff00)

    if args[2].upper() == "LEC":
        lecs = ""
        times = ""
        instructors = ""
        for lec in course.lec:
            for time in lec.times:
                times += time + ", "
            for instructor in lec.instructors:
                if instructor not in instructors:
                    instructors += instructor + ", "
            if ',' == instructors[-2]:
                instructors = instructors[:-2]
            if ',' == times[-2]:
                times = times[:-2]
            lecs += f"**{lec.code}** - {times}\n{instructors}\n"
            times = ""
            instructors = ""
        embed.add_field(name="Lectures", value=lecs, inline=False)
        await ctx.send(embed=embed)

    elif args[2].upper() == "PRA":
        pras = ""
        times = ""
        for pra in course.pra:
            if len(pras) < 900:
                for time in pra.times:
                    times += time + ", "
                if "," == times[-2]:
                    times = times[:-2]
                pras += f"**{pra.code}** - {times}\n"
                times = ""
        if len(pras) > 900:
            pras += "...\n"
        embed.add_field(name="Practicals", value=pras, inline=False)
        await ctx.send(embed=embed)

    elif args[2].upper() == "TUT":
        tuts = ""
        times = ""
        for tut in course.tut:
            if len(tuts) < 900:
                for time in tut.times:
                    times += time + ", "
                if ',' == times[-2]:
                    times = times[:-2]
                tuts += f"**{tut.code}** - {times}\n"
                times = ""
        if len(tuts) > 900:
            tuts += "...\n"
        embed.add_field(name="Tutorials", value=tuts, inline=False)
        await ctx.send(embed=embed)


@client.command()
async def view_all(ctx):
    """Shows all courses in the server."""
    courses = jdb.get_from_json(ctx.channel.id)
    embed = discord.Embed(title="Courses", description=f"All courses in <#{ctx.channel.id}>.", color=0x00ff00)
    for course in courses:
        course = cc.create_course(course, "S")
        embed.add_field(name=course.code, value=course.name, inline=False)
    await ctx.send(embed=embed)

# Login to the bot
client.run(TOKEN)