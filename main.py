import discord
from discord.ext import commands
import datetime
from matrizcsv import matrizdebusqueda as mtbq
from buscadorcsv import finder as fd
from buscadorcsv import adder as addr

USERS = ['Zino243', 'Amrak22','Awadechicagamer']
bot = commands.Bot(command_prefix='>', description="This is a helper bot")


def comprobarusers(name):
    for i in USERS:
        if i == name:
            return True

# Ejemplo de texto enriquecido #
def enriquecido(title, name,coordX, coordY):
    embed = discord.Embed(title = title, description="Añadir zonas!", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name = "Zona de: ", value=name )
    embed.add_field(name = "Coordenada X: ", value=coordX)
    embed.add_field(name = "Coordenada Y: ", value=coordY)
    return embed

#def generador de eventos activos
def eventos_activos(title):
    embed = discord.Embed(title = title, description="Evenots activos", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name = "Evento mas cercano: ", value="Matar a la Dragona" )
    embed.add_field(name = "Día: ", value="Miércoles 22 de Junio")
    embed.add_field(name = "Hora: ", value="23:00")
    return embed

# guardar coords #
@bot.command()
async def añadir(ctx ,name:str, numX,  numY):
    title = f"{ctx.guild.name}"
    print(USERS)
    comprobado = comprobarusers(name)
    if comprobado:
        await ctx.send("tu usuario es {}".format(name))
        try:
            int(numX)
            int(numY)
            addr.adder(name, numX, numY)
            await ctx.send(embed=enriquecido(title, name, numX, numY))
        except ValueError:
            await ctx.send("alguna entrada de coordenadas da error, repita el mensaje")
    else:
        await ctx.send("tu usuario es incorrecto o falta algo")


#comprobar coords
@bot.command()
async def comprobar(ctx,coordX:int,coordY:int):
    t = mtbq.busqueda(coordX, coordY)
    n = fd.name(coordX, coordY)

    if t:
        await ctx.send("las coordenadas estan elegidas por {}".format(n))
    else:
        await ctx.send("puedes construir aqui!")

#eventos:
@bot.command()
async def eventos(ctx, value: str):
    title = f"{ctx.guild.name}"
    if value == "activos":
        await ctx.send(embed=eventos_activos(title))
    elif value == "" or " " or False:
        await ctx.send("comando mal escrito o no existe")



#esto me dice si el bot se activa por shell
@bot.event
async def on_ready():
    #await bot.change_presence(activity=discord.Streaming(name="Paco", url="http://www.twitch.tv/accountname")) #enseña si está en directo
    print('El bot está listo pa')

bot.run('')
