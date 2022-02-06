import discord
from discord.ext import commands
import parse_weather_data as w_data
from datetime import date

TOKEN = 'TOKEN_HERE'
client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('WeatherBot is ready to run')


@client.command()
async def test(ctx):
    await ctx.send('Ask me what the weather is!')


@client.command()
async def weather(ctx):
    await ctx.send('Today the weather is')
    today_date = date.today()
    weather_stats = w_data.get_weather_data(today_date)
    embed = discord.Embed(
        title='The Weather for ' + str(today_date),
        description=weather_stats,
        colour=discord.colour.Colour.blue()
    )

    embed.set_footer(text='this is the footer')
    embed.set_image(url='https://media.globalnews.ca/videostatic/621/967/2016-03-08T17-14-44.133Z--1280x720.jpg')
    embed.set_thumbnail(url='https://media.globalnews.ca/videostatic/621/967/2016-03-08T17-14-44.133Z--1280x720.jpg')
    embed.set_author(name='Bluebot')
    embed.add_field(name='Weather', value='Here is your forecast', inline=True)
    # await ctx.send(embed=embed)



client.run(TOKEN)



