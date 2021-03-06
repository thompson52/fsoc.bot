# fsociety by thomas1o#8211

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import os

bot = commands.Bot(command_prefix='')
bot.remove_command('help')

print (discord.__version__)

@bot.event
async def on_ready():
    print ("initializing fscoiety v.1.0")
    print ("I am running " + bot.user.name)
    print ("With the ID: " + bot.user.id)

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("192.251.68.253")
    print ("user has pinged")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color=0x00ff00)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role)
    embed.add_field(name="Joined", value=user.joined_at)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="ACCESS GRANTED", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_role("Administrator")
async def kick(ctx, user: discord.Member):
    await bot.say(":The user, {} has been kicked".format(user.name))
    await bot.kick(user)

@bot.command(pass_context=True)
async def botinfo(ctx):
    embed = discord.Embed(title="Made with:", description="Python 3.7", color=0x00ff00)
    embed.set_footer(text="$--------$")
    embed.set_author(name="fsociety v.1.0 by thomas1o")
    embed.add_field(name="Powered by:", value="Heroku", inline=True)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed.set_author(name="All Commands")
    embed.add_field(name=ping , value='Sends you an Ip' ,  inline=false)
    embed.add_field(name=info , value='Displays detailed info of your chosen Target' , inline=false)
    embed.add_field(name=serverinfo , value='Displays detailed info on the server' , inline=false)
    embed.add_field(name=botinfo , value='Displays detailed info on this Bot' , inline=false)
    await bot.send_message(author, embed=embed)

bot.run(os.getenv('TOKEN'))
