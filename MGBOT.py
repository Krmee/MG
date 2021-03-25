import discord
import random
from discord.ext import commands

client=commands.Bot(command_prefix="!")

@client.event
async def on_ready():
     await client.change_presence(status=discord.Status.idle, activity=discord.Game('Mandarina Gang'))
     print("Bot is up!")

#komande 
@client.command()
async def clear(ctx, amount=1000):
   await ctx.channel.purge(limit=amount)

@client.command()
async def sajt(ctx):
  await ctx.send("file:///C:/Users/Stefan/Desktop/sajt.html")

@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
  await member.kick(reason=reason)

@client.command()
async def ban(ctx, member:discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f'Banovan {member.mention}')

@client.command()
async def unban(ctx, *, member):
  banned_users=await ctx.guild.bans()
  member_name, member_discriminator=member.split('#')

  for ban_entry in banned_users:
    user=ban_entry.user

    if (user.name, user.discriminator) == (member_name, member_discriminator):
      await ctx.guild.unban(user)
      await ctx.send(f'Unbanovan {user.mention}')
      return

@client.command(aliases=['pitanje', 'test'])
async def _8ball(ctx, *, questions):
         responses = ['Ne',
                 'Krme je prase',
                 'Krme je pametniji od zole',
                 'Zola je J1nnov debil.',
                 'Jeste, zola nema mozga',
                 'Pusti sad Zolu jebo te on',
                 'Ucim se polako sa ovim botom',
                 'Necu vise zolu da diram obecavam',
                 'Da ti odgovorim nesto?',
                 'Krme malo ima 4 noge']
         await ctx.send(f'Pitanje: {questions}\nOdgovor: {random.choice(responses)}')

 




client.run("ODAxOTM3NDU2NjQyNjU0Mjcw.YAn8dA.T4S5vTUsKM3OuQ3bFxMFWa2y4YA")