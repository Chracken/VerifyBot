import discord
import mysql.connector
import math
import asyncio
import aiohttp
import json
import datetime
from discord.ext import commands
import traceback
from urllib.parse import quote
import validators
from discord.ext.commands.cooldowns import BucketType
from time import gmtime, strftime


with open('credentials.json') as credentials:
  jsdata = json.load(credentials)

PREFIX = jsdata['PREFIX']
SITE = jsdata['SITE']
ROLEID = jsdata['ROLEID']
SERVERID = jsdata['SERVERID']
mysql_ip = jsdata['mysql_ip']
mysql_username = jsdata['mysql_username']
mysql_password = jsdata['mysql_password']
signedtext = jsdata['signedtext']

bannedtext = jsdata['bannedtext']
unbannedtext = jsdata['unbannedtext']
notindatabase = jsdata['notindatabase']
correctformattext = jsdata['correctformattext']
codevalid1 = jsdata['codevalid1']
codevalid2 = jsdata['codevalid2']
wrongcode = jsdata['wrongcode']
bannedmessageonjoin = jsdata['bannedmessageonjoin']

class cmds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(pass_context=True)
    async def verify(self, ctx, arg=None):
        if isinstance(ctx.message.channel, discord.abc.PrivateChannel):
            if arg is None:
                return await ctx.channel.send(correctformattext + " `" + PREFIX + "verify <code>`")
            database = mysql.connector.connect(
              host=mysql_ip,
              user=mysql_username,
              password=mysql_password,
              database='verifybot'
            )
            cursor = database.cursor(buffered=True)
            CheckIfItExists = ("SELECT status,passcode FROM security WHERE userid = " + str(ctx.message.author.id))
            cursor.execute(CheckIfItExists)
            row_count = cursor.rowcount
            if row_count == 1:
                listedvalues = cursor.fetchall()
                for row in listedvalues:
                    status = row[0]
                    passcode = row[1]
                    if status != 'BLOCKED':
                        if (passcode == arg):
                            try:
                                await ctx.channel.send(codevalid1 + " `" + arg + "` " + codevalid2)
                                server = discord.utils.get(self.bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                member = server.get_member(ctx.message.author.id)
                                await member.remove_roles(role)
                            except:
                                pass
                        else:
                            await ctx.channel.send(wrongcode)
                    else:
                        await ctx.channel.send(bannedmessageonjoin)
            database.commit()
            cursor.close()
            database.close()

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member : discord.Member, reason = ""):
        signed = signedtext
        try:
            await member.ban(reason = reason + signed)
            await ctx.send(f'{bannedtext} {member}')
            database = mysql.connector.connect(
              host=mysql_ip,
              user=mysql_username,
              password=mysql_password,
              database='verifybot'
            )
            try:
                cursor = database.cursor(buffered=True)
                banuser = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(member.id))
                cursor.execute(banuser)
                database.commit()
                cursor.close()
                database.close()
            except:
                pass
        except:
            pass

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(ban_members = True)
    async def unban(self, ctx, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split("#")
            for ban_entry in banned_users:
                user = ban_entry.user

                if (user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'{unbannedtext} `{user}`')
                    database = mysql.connector.connect(
                      host=mysql_ip,
                      user=mysql_username,
                      password=mysql_password,
                      database='verifybot'
                    )
                    try:
                        cursor = database.cursor(buffered=True)
                        unbanuser = ("DELETE FROM security WHERE userid = " + str(user.id))
                        cursor.execute(unbanuser)
                        database.commit()
                        cursor.close()
                        database.close()
                    except:
                        pass
                    return
        except:
            await ctx.send(f'{correctformattext} `{PREFIX}unban name#0000`')
            return
            
    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(ban_members = True)
    async def unbandb(self, ctx, ids):
        if ids.isnumeric() and len(ids) == 18:
            try:
                database = mysql.connector.connect(
                  host=mysql_ip,
                  user=mysql_username,
                  password=mysql_password,
                  database='verifybot'
                )
                cursor = database.cursor(buffered=True)
                CheckIfItExists = ("SELECT status FROM security WHERE userid = " + str(ids))
                cursor.execute(CheckIfItExists)
                row_count = cursor.rowcount
                if row_count == 1:
                    unbanuser2 = ("DELETE FROM security WHERE userid = " + str(ids))
                    cursor.execute(unbanuser2)
                    database.commit()
                    cursor.close()
                    database.close()
                    membertounban = await self.bot.fetch_user(ids)
                    try:
                        await ctx.guild.unban(membertounban)
                    except:
                        pass
                    await ctx.send(f'{unbannedtext} ID: `{ids}`')
                if row_count == 0:
                    await ctx.send(f'{notindatabase} ID: `{ids}`')
            except:
                pass
        else:
            await ctx.send(f'{correctformattext} `{PREFIX}unbandb id`')
            return

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_permissions(administrator = True)
    async def setup(self, ctx):
        server = discord.utils.get(self.bot.guilds, id=int(SERVERID))
        role = discord.utils.get(server.roles, id=ROLEID)
        for channel in server.channels:
            try:
                await channel.set_permissions(role, send_messages=False, connect=False, read_messages=False, view_channel=False)
            except:
                pass
        await ctx.send('Done')

def setup(bot):
    bot.add_cog(cmds(bot))
