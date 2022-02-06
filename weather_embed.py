import discord
from discord.ext import commands
import Weather

TOKEN = 'YOUR_TOKEN_HERE'

client = commands.Bot(command_prefix='+')


@client.event
async def on_ready():
    print('WeatherBot is ready to run')


@client.command(pass_context=True)
async def displayembed():
    weather_stats = Weather
    embed = discord.Embed(
        title='Weather',
        description='This is your upcoming forecast at uoftsg campus',
        colour=discord.colour.Colour.blue()
    )
    embed.add_field()
    embed.set_footer(text='this is the footer')
    embed.set_image(url='https://media.globalnews.ca/videostatic/621/967/2016-03-08T17-14-44.133Z--1280x720.jpg')
    embed.set_thumbnail(url='https://media.globalnews.ca/videostatic/621/967/2016-03-08T17-14-44.133Z--1280x720.jpg')
    embed.set_author(name='Bluebot')
    embed.add_field(name='!weather', value='Here is your forecast', inline=True)

    await client.run(embed=embed)

client.run(TOKEN)



