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
    i=0

    for guild in client.guilds:
        for member in guild.members:
            for role in member.roles:
                if role.name == "ticket":
                    i = i+1

    print(i)
    if i >= 1:
        a = 0

        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "ticket2":
                        a = a + 1

        print(a)
        if a == 0:
            embed = discord.Embed(title="Creado correctamente",
                                  description="Por favor dirigete al canal #ticket creado en la sección de soporte solamente para ti!, mientras alguien te atiende por favor danos una explicación del problema en ese canal",
                                  color=0xff2968)
            embed.set_author(name="Sistema de Tickets", icon_url="http://url.torokoko.cl/chillinicon")
            await ctx.send(embed=embed)

            user = ctx.message.author
            role = discord.utils.get(ctx.guild.roles, name="ticket2")

            await user.add_roles(role)

        else:
            b = 0

            for guild in client.guilds:
                for member in guild.members:
                    for role in member.roles:
                        if role.name == "ticket3":
                            b = b + 1

            if b == 0:
                embed = discord.Embed(title="Creado correctamente",
                                      description="Por favor dirigete al canal #ticket creado en la sección de soporte solamente para ti!, mientras alguien te atiende por favor danos una explicación del problema en ese canal",
                                      color=0xff2968)
                embed.set_author(name="Sistema de Tickets", icon_url="http://url.torokoko.cl/chillinicon")
                await ctx.send(embed=embed)

                user = ctx.message.author
                role = discord.utils.get(ctx.guild.roles, name="ticket3")

                await user.add_roles(role)

            else:
                embed = discord.Embed(title="Capacidad superada",
                                      description="Lo sentimos pero ya tenemos muchos tickets por el momento, por favor intentalo más tarde o comenta tu problema por aquí",
                                      color=0xff2968)
                embed.set_author(name="Sistema de Tickets", icon_url="http://url.torokoko.cl/chillinicon")
                await ctx.send(embed=embed)


    else:
        embed = discord.Embed(title="Creado correctamente",
                              description="Por favor dirigete al canal #ticket creado en la sección de soporte solamente para ti!, mientras alguien te atiende por favor danos una explicación del problema en ese canal",
                              color=0xff2968)
        embed.set_author(name="Sistema de Tickets", icon_url = "http://url.torokoko.cl/chillinicon")
        await ctx.send(embed=embed)

        user = ctx.message.author
        role = discord.utils.get(ctx.guild.roles, name="ticket")

        await user.add_roles(role)

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
