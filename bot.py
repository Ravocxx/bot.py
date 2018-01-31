import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

client = discord.Client()
client = Bot(description="Sys#5888", command_prefix="*", pm_help = False)

@client.event
async def on_ready():
    print('Bot Online - Óla Mundo')
    print(client.user.name)
    print(client.user.id)
    print('Todos Os Compontes Foram Carregados Com Sucesso, Agora verifique se o Bot Esta ligado Visitando seu Servidor')
    return await client.change_presence(game=discord.Game(name='League Of Crystal')) #This is buggy, let us know if it doesn't work.
    await client.say(":warning: This bot was created by **Nostradamus‘‘**, it seems that you have not modified it yet. Go edit the file and try it out!")
	
@client.event
async def on_message(message):
    if message.content.upper().startswith('!PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))
    if message.content.upper().startswith('!SAY'):
        if message.author.id == "<300664115762823168>": #Replace <User ID> with the ID of the user you want to be able to execute this command!
            args = message.content.split(" ")
            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You do not have permission")
    if message.content.upper().startswith('!AMIADMIN'):
        if "<role id>" in [role.id for role in message.author.roles]: #Replace <Role ID> with the ID of the role you want to be able to execute this command
            await client.send_message(message.channel, "You are an admin")
        else:
            await client.send_message(message.channel, "You are not an admin")


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('$guess'):
        await client.send_message(message.channel, 'Guess a number between 1 to 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await client.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = 'Sorry, you took too long. It was {}.'
            await client.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await client.send_message(message.channel, 'You are right!')
        else:
            await client.send_message(message.channel, 'Sorry. It is actually {}.'.format(answer))


@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))


@client.event
async def on_ready():
    print('Connected!')
    print('Username: ' + client.user.name)
    print('ID: ' + client.user.id)

@client.event
async def on_message(message):
    if message.content.startswith('!editme'):
        msg = await client.send_message(message.author, '10')
        await asyncio.sleep(3)
        await client.edit_message(msg, '40')

@client.event
async def on_message_edit(before, after):
    fmt = '**{0.author}** edited their message:\n{1.content}'
    await client.send_message(after.channel, fmt.format(after, before))


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!Info'):
        msg = 'Python Version 3.0V, Criador, Nostradamus {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
	
client.run('NDA3MzIyMzEwMjExNjY1OTIw.DU_1HA.Q8Ua5ncYOnyXCoUnjGXCAcYobzc')
