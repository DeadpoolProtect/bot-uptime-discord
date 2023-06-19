import discord
from discord.ext import commands
from colorama import init, Fore
from discord import utils
import socket
import asyncio



intents = discord.Intents.all()

client = commands.Bot(
    command_prefix='+',  # Le préfix pour les commandes est "+"
    case_insensitive=False,
    description=None,
    intents=intents,
    help_command=None
)

async def check_uptime():
    await client.wait_until_ready()
    status_message = None  
    while not client.is_closed():
        try:
            ip = "ip"
            port = 80
            timeout = 5

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            start_time = asyncio.get_event_loop().time()
            result = sock.connect_ex((ip, port))
            end_time = asyncio.get_event_loop().time()
            sock.close()

            if result == 0:
                ms = round((end_time - start_time) * 1000, 2)
                status = f"En ligne (Ping : {ms} ms)"
            else:
                status = "Hors ligne"

            if status_message:
                await status_message.edit(content=status)
            else:
                channel = client.get_channel(1039248837673496687)  ###met l'id de ton channel
                status_message = await channel.send(status)

        except Exception as e:
            print(f"Une erreur s'est produite : {str(e)}")

        await asyncio.sleep(60)



client.loop.create_task(check_uptime())
client.run("")