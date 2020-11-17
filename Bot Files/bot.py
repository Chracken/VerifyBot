import discord
import mysql.connector
import math
import asyncio
import aiohttp
import json
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.ext.commands import MemberNotFound
from discord.ext.commands import MissingPermissions
from discord.ext.commands import BadArgument
from random import randint
import traceback
import sys
import random
import string

client = discord.Client()
intents=intents=discord.Intents.all()

with open('credentials.json') as credentials:
  jsdata = json.load(credentials)

PREFIX = jsdata['PREFIX']
SITE = jsdata['SITE']
ROLEID = jsdata['ROLEID']
SERVERID = jsdata['SERVERID']
bot = commands.Bot(command_prefix=PREFIX,intents=intents, case_insensitive=True)
DISCORD_TOKEN = jsdata['DISCORD_TOKEN']
mysql_ip = jsdata['mysql_ip']
mysql_username = jsdata['mysql_username']
mysql_password = jsdata['mysql_password']
onjointext1 = jsdata['onjointext1']
onjointext2 = jsdata['onjointext2']
signedtext = jsdata['signedtext']
allowipban = jsdata['allowipban']

initial_extensions = ['botcmd.cmds']

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_member_join(member):
    try:
        role = discord.utils.get(member.guild.roles, id=ROLEID)
        await member.add_roles(role)
    except:
        pass
    database = mysql.connector.connect(
      host=mysql_ip,
      user=mysql_username,
      password=mysql_password,
      database='verifybot'
    )
    cursor = database.cursor(buffered=True)
    CheckIfAlreadyExists = ("SELECT authorization FROM security WHERE userid = " + str(member.id))
    cursor.execute(CheckIfAlreadyExists)
    row_count = cursor.rowcount
    if row_count == 1:
        authorization = cursor.fetchone()
        await member.send(onjointext1 + '\n' + "Link: " + SITE +"/verify.php?u=" + f"{authorization[0]}" + '\n' + onjointext2 + " `" + PREFIX + "verify CODE`")
    if row_count == 0:
        letters = string.ascii_lowercase + string.digits
        authgenerate = ''.join(random.choice(letters) for i in range(8))
        passgenerate = ''.join(random.choice(letters) for i in range(6))
        passphraseandid = (f"{member.id}" + str(authgenerate))
        querytosend = (f"INSERT INTO security(userid,authorization,passcode) VALUES('{member.id}','{passphraseandid}','{passgenerate}')")
        cursor.execute(querytosend)
        await member.send(onjointext1 + '\n' + "Link: " + SITE + "/verify.php?u=" + str(passphraseandid) + '\n' + onjointext2 + " `" + PREFIX + "verify CODE`")
    database.commit()
    cursor.close()
    database.close()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    if isinstance(error, MemberNotFound):
        return
    if isinstance(error, MissingPermissions):
        return
    if isinstance(error, BadArgument):
        return
    raise error

async def repeater():
    while True:
        database = mysql.connector.connect(
          host=mysql_ip,
          user=mysql_username,
          password=mysql_password,
          database='verifybot'
        )
        CheckBlockedUsers = ("SELECT key1, key2, key3, key4, key5, key6, key7, key8, key9, key10 FROM security WHERE status = 'BLOCKED'")
        cursor = database.cursor(buffered=True)
        cursor.execute(CheckBlockedUsers)
        blocked_row_count = cursor.rowcount
        if blocked_row_count >= 1:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{blocked_row_count} banned users!"))
            blockedlistedvalues = cursor.fetchall()
            for blockedrows in blockedlistedvalues:
                if blockedrows[0] != 'NOTSET':
                    CheckForUsers0 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[0]}' or key2 = '{blockedrows[0]}' or key3 = '{blockedrows[0]}' or key4 = '{blockedrows[0]}' or key5 = '{blockedrows[0]}' or key6 = '{blockedrows[0]}' or key7 = '{blockedrows[0]}' or key8 = '{blockedrows[0]}' or key9 = '{blockedrows[0]}' or key10 = '{blockedrows[0]}')")
                    cursor2 = database.cursor(buffered=True)
                    cursor2.execute(CheckForUsers0)
                    CheckForUsers0_row_count = cursor2.rowcount
                    if CheckForUsers0_row_count >= 1:
                        CheckForUsers0values = cursor2.fetchall()
                        for CheckForUsers0user in CheckForUsers0values:
                            CheckForUsers0userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers0user[0]))
                            cursor3 = database.cursor(buffered=True)
                            cursor3.execute(CheckForUsers0userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers0user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor3.close()
                    cursor2.close()
                if blockedrows[1] != 'NOTSET':
                    CheckForUsers1 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[1]}' or key2 = '{blockedrows[1]}' or key3 = '{blockedrows[1]}' or key4 = '{blockedrows[1]}' or key5 = '{blockedrows[1]}' or key6 = '{blockedrows[1]}' or key7 = '{blockedrows[1]}' or key8 = '{blockedrows[1]}' or key9 = '{blockedrows[1]}' or key10 = '{blockedrows[1]}')")
                    cursor4 = database.cursor(buffered=True)
                    cursor4.execute(CheckForUsers1)
                    CheckForUsers1_row_count = cursor4.rowcount
                    if CheckForUsers1_row_count >= 1:
                        CheckForUsers1values = cursor4.fetchall()
                        for CheckForUsers1user in CheckForUsers1values:
                            CheckForUsers1userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers1user[0]))
                            cursor5 = database.cursor(buffered=True)
                            cursor5.execute(CheckForUsers1userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers1user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor5.close()
                    cursor4.close()
                if blockedrows[2] != 'NOTSET':
                    CheckForUsers2 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[2]}' or key2 = '{blockedrows[2]}' or key3 = '{blockedrows[2]}' or key4 = '{blockedrows[2]}' or key5 = '{blockedrows[2]}' or key6 = '{blockedrows[2]}' or key7 = '{blockedrows[2]}' or key8 = '{blockedrows[2]}' or key9 = '{blockedrows[2]}' or key10 = '{blockedrows[2]}')")
                    cursor6 = database.cursor(buffered=True)
                    cursor6.execute(CheckForUsers2)
                    CheckForUsers2_row_count = cursor6.rowcount
                    if CheckForUsers2_row_count >= 1:
                        CheckForUsers2values = cursor6.fetchall()
                        for CheckForUsers2user in CheckForUsers2values:
                            CheckForUsers2userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers2user[0]))
                            cursor7 = database.cursor(buffered=True)
                            cursor7.execute(CheckForUsers2userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers2user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor7.close()
                    cursor6.close()
                if blockedrows[3] != 'NOTSET':
                    CheckForUsers3 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[3]}' or key2 = '{blockedrows[3]}' or key3 = '{blockedrows[3]}' or key4 = '{blockedrows[3]}' or key5 = '{blockedrows[3]}' or key6 = '{blockedrows[3]}' or key7 = '{blockedrows[3]}' or key8 = '{blockedrows[3]}' or key9 = '{blockedrows[3]}' or key10 = '{blockedrows[3]}')")
                    cursor8 = database.cursor(buffered=True)
                    cursor8.execute(CheckForUsers3)
                    CheckForUsers3_row_count = cursor8.rowcount
                    if CheckForUsers3_row_count >= 1:
                        CheckForUsers3values = cursor8.fetchall()
                        for CheckForUsers3user in CheckForUsers3values:
                            CheckForUsers3userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers3user[0]))
                            cursor9 = database.cursor(buffered=True)
                            cursor9.execute(CheckForUsers3userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers3user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor9.close()
                    cursor8.close()
                if blockedrows[4] != 'NOTSET':
                    CheckForUsers4 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[4]}' or key2 = '{blockedrows[4]}' or key3 = '{blockedrows[4]}' or key4 = '{blockedrows[4]}' or key5 = '{blockedrows[4]}' or key6 = '{blockedrows[4]}' or key7 = '{blockedrows[4]}' or key8 = '{blockedrows[4]}' or key9 = '{blockedrows[4]}' or key10 = '{blockedrows[4]}')")
                    cursor10 = database.cursor(buffered=True)
                    cursor10.execute(CheckForUsers4)
                    CheckForUsers4_row_count = cursor10.rowcount
                    if CheckForUsers4_row_count >= 1:
                        CheckForUsers4values = cursor10.fetchall()
                        for CheckForUsers4user in CheckForUsers4values:
                            CheckForUsers4userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers4user[0]))
                            cursor11 = database.cursor(buffered=True)
                            cursor11.execute(CheckForUsers4userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers4user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor11.close()
                    cursor10.close()
                if blockedrows[5] != 'NOTSET':
                    CheckForUsers5 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[5]}' or key2 = '{blockedrows[5]}' or key3 = '{blockedrows[5]}' or key4 = '{blockedrows[5]}' or key5 = '{blockedrows[5]}' or key6 = '{blockedrows[5]}' or key7 = '{blockedrows[5]}' or key8 = '{blockedrows[5]}' or key9 = '{blockedrows[5]}' or key10 = '{blockedrows[5]}')")
                    cursor12 = database.cursor(buffered=True)
                    cursor12.execute(CheckForUsers5)
                    CheckForUsers5_row_count = cursor12.rowcount
                    if CheckForUsers5_row_count >= 1:
                        CheckForUsers5values = cursor12.fetchall()
                        for CheckForUsers5user in CheckForUsers5values:
                            CheckForUsers5userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers5user[0]))
                            cursor13 = database.cursor(buffered=True)
                            cursor13.execute(CheckForUsers5userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers5user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor13.close()
                    cursor12.close()
                if blockedrows[6] != 'NOTSET':
                    CheckForUsers6 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[6]}' or key2 = '{blockedrows[6]}' or key3 = '{blockedrows[6]}' or key4 = '{blockedrows[6]}' or key5 = '{blockedrows[6]}' or key6 = '{blockedrows[6]}' or key7 = '{blockedrows[6]}' or key8 = '{blockedrows[6]}' or key9 = '{blockedrows[6]}' or key10 = '{blockedrows[6]}')")
                    cursor14 = database.cursor(buffered=True)
                    cursor14.execute(CheckForUsers6)
                    CheckForUsers6_row_count = cursor14.rowcount
                    if CheckForUsers6_row_count >= 1:
                        CheckForUsers6values = cursor14.fetchall()
                        for CheckForUsers6user in CheckForUsers6values:
                            CheckForUsers6userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers6user[0]))
                            cursor15 = database.cursor(buffered=True)
                            cursor15.execute(CheckForUsers6userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers6user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor15.close()
                    cursor14.close()
                if blockedrows[7] != 'NOTSET':
                    CheckForUsers7 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[7]}' or key2 = '{blockedrows[7]}' or key3 = '{blockedrows[7]}' or key4 = '{blockedrows[7]}' or key5 = '{blockedrows[7]}' or key6 = '{blockedrows[7]}' or key7 = '{blockedrows[7]}' or key8 = '{blockedrows[7]}' or key9 = '{blockedrows[7]}' or key10 = '{blockedrows[7]}')")
                    cursor16 = database.cursor(buffered=True)
                    cursor16.execute(CheckForUsers7)
                    CheckForUsers7_row_count = cursor16.rowcount
                    if CheckForUsers7_row_count >= 1:
                        CheckForUsers7values = cursor16.fetchall()
                        for CheckForUsers7user in CheckForUsers7values:
                            CheckForUsers7userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers7user[0]))
                            cursor17 = database.cursor(buffered=True)
                            cursor17.execute(CheckForUsers7userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers7user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor17.close()
                    cursor16.close()
                if blockedrows[8] != 'NOTSET':
                    CheckForUsers8 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[8]}' or key2 = '{blockedrows[8]}' or key3 = '{blockedrows[8]}' or key4 = '{blockedrows[8]}' or key5 = '{blockedrows[8]}' or key6 = '{blockedrows[8]}' or key7 = '{blockedrows[8]}' or key8 = '{blockedrows[8]}' or key9 = '{blockedrows[8]}' or key10 = '{blockedrows[8]}')")
                    cursor18 = database.cursor(buffered=True)
                    cursor18.execute(CheckForUsers8)
                    CheckForUsers8_row_count = cursor18.rowcount
                    if CheckForUsers8_row_count >= 1:
                        CheckForUsers8values = cursor18.fetchall()
                        for CheckForUsers8user in CheckForUsers8values:
                            CheckForUsers8userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers8user[0]))
                            cursor19 = database.cursor(buffered=True)
                            cursor19.execute(CheckForUsers8userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers8user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor19.close()
                    cursor18.close()
                if blockedrows[9] != 'NOTSET':
                    CheckForUsers9 = (f"SELECT userid FROM security WHERE status = 'OK' AND (key1 = '{blockedrows[9]}' or key2 = '{blockedrows[9]}' or key3 = '{blockedrows[9]}' or key4 = '{blockedrows[9]}' or key5 = '{blockedrows[9]}' or key6 = '{blockedrows[9]}' or key7 = '{blockedrows[9]}' or key8 = '{blockedrows[9]}' or key9 = '{blockedrows[9]}' or key10 = '{blockedrows[9]}')")
                    cursor20 = database.cursor(buffered=True)
                    cursor20.execute(CheckForUsers9)
                    CheckForUsers9_row_count = cursor20.rowcount
                    if CheckForUsers9_row_count >= 1:
                        CheckForUsers9values = cursor20.fetchall()
                        for CheckForUsers9user in CheckForUsers9values:
                            CheckForUsers9userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers9user[0]))
                            cursor21 = database.cursor(buffered=True)
                            cursor21.execute(CheckForUsers9userquery)
                            try:
                                server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                role = discord.utils.get(server.roles, id=ROLEID)
                                memberidis = CheckForUsers9user[0]
                                usertoban = server.get_member(memberidis)
                                signed = signedtext
                                await usertoban.ban(reason = signed)
                            except:
                                pass
                            cursor21.close()
                    cursor20.close()
        if allowipban == True:
            CheckBlockedUsersOnIp = ("SELECT ipv41, ipv42, ipv43, ipv61, ipv62, ipv63 FROM security WHERE status = 'BLOCKED'")
            cursor22 = database.cursor(buffered=True)
            cursor22.execute(CheckBlockedUsersOnIp)
            blocked_row_count22 = cursor22.rowcount
            if blocked_row_count22 >= 1:
                blockedlistedvalues22 = cursor22.fetchall()
                for blockedrows22 in blockedlistedvalues22:
                    if blockedrows22[0] != '0.0.0.0':
                        CheckForUsers23 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv41 = '{blockedrows22[0]}' or ipv42 = '{blockedrows22[0]}' or ipv43 = '{blockedrows22[0]}')")
                        cursor23 = database.cursor(buffered=True)
                        cursor23.execute(CheckForUsers23)
                        CheckForUsers23_row_count = cursor23.rowcount
                        if CheckForUsers23_row_count >= 1:
                            CheckForUsers23values = cursor23.fetchall()
                            for CheckForUsers23user in CheckForUsers23values:
                                CheckForUsers23userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers23user[0]))
                                cursor24 = database.cursor(buffered=True)
                                cursor24.execute(CheckForUsers23userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers23user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor24.close()
                        cursor23.close()
                    if blockedrows22[1] != '0.0.0.0':
                        CheckForUsers24 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv41 = '{blockedrows22[1]}' or ipv42 = '{blockedrows22[1]}' or ipv43 = '{blockedrows22[1]}')")
                        cursor25 = database.cursor(buffered=True)
                        cursor25.execute(CheckForUsers24)
                        CheckForUsers24_row_count = cursor25.rowcount
                        if CheckForUsers24_row_count >= 1:
                            CheckForUsers24values = cursor25.fetchall()
                            for CheckForUsers24user in CheckForUsers24values:
                                CheckForUsers24userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers24user[0]))
                                cursor26 = database.cursor(buffered=True)
                                cursor26.execute(CheckForUsers24userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers24user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor26.close()
                        cursor25.close()
                    if blockedrows22[2] != '0.0.0.0':
                        CheckForUsers25 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv41 = '{blockedrows22[2]}' or ipv42 = '{blockedrows22[2]}' or ipv43 = '{blockedrows22[2]}')")
                        cursor27 = database.cursor(buffered=True)
                        cursor27.execute(CheckForUsers25)
                        CheckForUsers25_row_count = cursor27.rowcount
                        if CheckForUsers25_row_count >= 1:
                            CheckForUsers25values = cursor27.fetchall()
                            for CheckForUsers25user in CheckForUsers25values:
                                CheckForUsers25userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers25user[0]))
                                cursor28 = database.cursor(buffered=True)
                                cursor28.execute(CheckForUsers25userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers25user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor28.close()
                        cursor27.close()
                    if blockedrows22[3] != 'FEC0:0000:0000:0000:0000:0000:0000:0001':
                        CheckForUsers26 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv61 = '{blockedrows22[3]}' or ipv62 = '{blockedrows22[3]}' or ipv63 = '{blockedrows22[3]}')")
                        cursor29 = database.cursor(buffered=True)
                        cursor29.execute(CheckForUsers26)
                        CheckForUsers26_row_count = cursor29.rowcount
                        if CheckForUsers26_row_count >= 1:
                            CheckForUsers26values = cursor29.fetchall()
                            for CheckForUsers26user in CheckForUsers26values:
                                CheckForUsers26userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers26user[0]))
                                cursor30 = database.cursor(buffered=True)
                                cursor30.execute(CheckForUsers26userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers26user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor30.close()
                        cursor29.close()
                    if blockedrows22[4] != 'FEC0:0000:0000:0000:0000:0000:0000:0001':
                        CheckForUsers27 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv61 = '{blockedrows22[4]}' or ipv62 = '{blockedrows22[4]}' or ipv63 = '{blockedrows22[4]}')")
                        cursor31 = database.cursor(buffered=True)
                        cursor31.execute(CheckForUsers27)
                        CheckForUsers27_row_count = cursor31.rowcount
                        if CheckForUsers27_row_count >= 1:
                            CheckForUsers27values = cursor31.fetchall()
                            for CheckForUsers27user in CheckForUsers27values:
                                CheckForUsers27userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers27user[0]))
                                cursor32 = database.cursor(buffered=True)
                                cursor32.execute(CheckForUsers27userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers27user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor32.close()
                        cursor31.close()
                    if blockedrows22[5] != 'FEC0:0000:0000:0000:0000:0000:0000:0001':
                        CheckForUsers28 = (f"SELECT userid FROM security WHERE status = 'OK' AND (ipv61 = '{blockedrows22[5]}' or ipv62 = '{blockedrows22[5]}' or ipv63 = '{blockedrows22[5]}')")
                        cursor33 = database.cursor(buffered=True)
                        cursor33.execute(CheckForUsers28)
                        CheckForUsers28_row_count = cursor33.rowcount
                        if CheckForUsers28_row_count >= 1:
                            CheckForUsers28values = cursor33.fetchall()
                            for CheckForUsers28user in CheckForUsers28values:
                                CheckForUsers28userquery = ("UPDATE security SET status = 'BLOCKED' WHERE userid = " + str(CheckForUsers28user[0]))
                                cursor34 = database.cursor(buffered=True)
                                cursor34.execute(CheckForUsers28userquery)
                                try:
                                    server = discord.utils.get(bot.guilds, id=int(SERVERID))
                                    role = discord.utils.get(server.roles, id=ROLEID)
                                    memberidis = CheckForUsers28user[0]
                                    usertoban = server.get_member(memberidis)
                                    signed = signedtext
                                    await usertoban.ban(reason = signed)
                                except:
                                    pass
                                cursor34.close()
                        cursor33.close()
            cursor22.close()
        database.commit()
        cursor.close()
        database.close()
        await asyncio.sleep(15)

@bot.event
async def on_ready():
    print('Verify Bot Ready')
    client.loop.create_task(repeater())
    

bot.run(DISCORD_TOKEN)