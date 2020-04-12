import discord
from discord.ext import commands
from discord.utils import get

token = "{insert your token here}"

prefix="?"
client = commands.Bot(command_prefix=prefix)

### This line removes help command problems (MUST HAVE IF YOU HAVE AN OWN HELP COMMAND)
client.remove_command("help")

### Confirmation that bot is running
@client.event
async def on_ready():
    activity = discord.Game(name="ChillinMC.sytes.net")
    await client.change_presence(status=discord.Status.online, activity=activity)
    print("Chillin bot is on")


### Help command
@client.command(pass_context = True)
async def help(ctx):
    embed = discord.Embed(title="Ayuda")
    # embed.set_author(name="Ayuda")
    embed.set_thumbnail(url="http://url.torokoko.cl/chillinicon")
    embed.add_field(name="?help", value="Muestra esta lista de comandos", inline="False")
    embed.add_field(name="?ticket", value="Creas un ticket en caso de tener algun problema en el servidor", inline="False")
    embed.add_field(name="?admins", value="Te muestra todos los administradores del juego", inline="False")
    embed.add_field(name="?author", value="El autor del botsito", inline="False")
    await ctx.send(embed=embed)
    print("Help command just ran")


### Admins command
@client.command(pass_context = True)
async def admins(ctx):
    embed = discord.Embed(title="Administradores")
    embed.set_thumbnail(url="http://url.torokoko.cl/chillinicon")
    embed.add_field(name="Administradores", value="Rokilo, Danisiiwii, Mesticke", inline="False")
    embed.add_field(name="Moderadores", value="torokoko", inline="False")
    await ctx.send(embed=embed)
    print("Admins command just ran")

### ticket command
@client.command(pass_context = True)
async def ticket(ctx):
    await ctx.send("Has creado un ticket con exito, ingresa al canal de tickets para ayudarte, te responderemos lo antes posible :D")
    user = ctx.message.author
    role = discord.utils.get(ctx.guild.roles, name="ticket")

    await user.add_roles(role)

    print("ticket command just ran")


### Author command
@client.command(pass_context = True)
async def author(ctx):
    await ctx.send("El creador de este bot es torokoko#3039, si necesitas ayuda o tienes algun problema no dudes en contactarme")


#### Clear channel messages (by default 100)
@client.command(pass_context = True)
@commands.has_any_role('Developer', 'Owner', 'Admin', 'Moderador', 'Dueño')
async def clear(ctx, amount=100):
    await ctx.channel.purge(limit=amount)


client.run(token)
