import discord
import asyncio

client = discord.Client()
token = "" # Buat token disini
prefix = "#"
command = "leave"
length = len(client.guilds)

@client.event
async def on_ready():
    print("Tulis command ini dimana saja " + prefix + "" + command) # Tulis ini dimana saja didalam chat discord

@client.event
async def on_message(message):
    cmd = str(message.content).split(' ')
    count = 0
    if cmd[0] == prefix + command:
        await message.delete()
        for guild in client.guilds:
            print("Delete channel" + guild.name)
            try:
                await guild.leave()
                count = count +1;
            except:
                pass
            if(count == length):
                print("You left total: " + count)

        
client.run(token, bot=False)
input("Press enter to exit") 