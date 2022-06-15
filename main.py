import discord
from discord.ext import commands
import datetime

USERS = ['Zino243', 'Paco']
bot = commands.Bot(command_prefix='>', description="This is a helper bot")


def comprobarusers(name):
    for i in USERS:
        if i == name:
            return True

def enriquecido(title, name,coordX, coordY):
    embed = discord.Embed(title = title, description="Añadir zonas!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name = "Zona de: ", value=name )
    embed.add_field(name = "Coordenada X: ", value=coordX)
    embed.add_field(name = "Coordenada Y: ", value=coordY)
    return embed

@bot.command()
async def sum(ctx,name:str, numX: int , numY: int):
    await ctx.send("tu resultado es nombre: {}, coordX: {} y coordY: {}".format(name, numX, numY))
        
@bot.command()
async def users(ctx ,name:str, numX,  numY):
    title = f"{ctx.guild.name}"
    print(USERS)
    comprobado = comprobarusers(name)
    if comprobado:
        await ctx.send("tu usuario es {}".format(name))
        try:
            int(numX)
            int(numY)
            await ctx.send(embed=enriquecido(title, name, numX, numY))
        except ValueError:
            await ctx.send("alguna entrada de coordenadas da error, repita el mensaje")
    else:
        await ctx.send("tu usuario es incorrecto o falta algo")
    
@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Streaming(name="Paco", url="http://www.twitch.tv/accountname")) #enseña si está en directo
    print('El bot está listo pa')

bot.run('')
