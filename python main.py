Skip to content

Library
Other
artifacts/api-server: API ServerWebsite
main.py
-0+17
import aiohttp
import os
from datetime import datetime
from flask import Flask
from threading import Thread
# ===== سيرفر ويب عشان Replit يفضل شغال =====
app = Flask('')
@app.route('/')
def home():
    return "Bot is alive!"
def run_web():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run_web)
    t.start()
# ============================================
intents = discord.Intents.default()
intents.members = True
-0+2
        print(f"Error: {e}")
        return None
# تشغيل السيرفر والبوت
keep_alive()
TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("Error: TOKEN not found in environment variables")
Add express server for keeping the application online

Create a blank Node.js project with only one file: index.js.
In index.js, create a basic HTTP server using the built-in http module that listens on process.env.PORT and returns "Server is running" on any request.
Do not install any packages and do not add any other files
6:00 am, May 24, 2026
6:02 am, May 24, 2026

pip install discord.py aiohttp
6:04 am, May 24, 2026
6:07 am, May 24, 2026

TOKEN
6:10 am, May 24, 2026
6:10 am, May 24, 2026

TOKEN
6:11 am, May 24, 2026

run = "python main.py"
6:13 am, May 24, 2026

async def get_roblox_full_info(username):
try:
async with aiohttp.ClientSession() as session:
# 1. جيب الـUser ID من اليوزرنيم
url1 = "https://users.roblox.com/v1/usernames/users"
data = {"usernames": [username], "excludeBannedUsers": True}
async with session.post(url1, json=data, timeout=10) as resp:
if resp.status!= 200:
return None
result = await resp.json()
if not result["data"]:
return None
user_id = result["data"][0]["id"]

        # 2. جيب بيانات الحساب
        url2 = f"https://users.roblox.com/v1/users/{user_id}"
        async with session.get(url2, timeout=10) as resp:
            if resp.status!= 200:
                return None
            user_data = await resp.json()
        # 3. جيب الصورة بالـAPI الجديد
        avatar_url = f"https://thumbnails.roblox.com/v1/users/avatar-headshot?userIds={user_id}&size=420x420&format=Png"
        async with session.get(avatar_url, timeout=10) as resp:
            thumb_data = await resp.json()
            if thumb_data["data"]:
                avatar_url = thumb_data["data"][0]["imageUrl"]
            else:
                avatar_url = None
        created_dt = datetime.fromisoformat(user_data["created"].replace("Z", "+00:00"))
        created_timestamp = int(created_dt.timestamp())
        return {
            "userId": user_id,
            "username": user_data["name"],
            "displayName": user_data["displayName"],
            "created_timestamp": created_timestamp,
            "avatar": avatar_url
        }
except Exception as e:
    print(f"Error: {e}")
    return None

6:20 am, May 24, 2026
6:23 am, May 24, 2026

log_channel = bot.get_channel(LOG_CHANNEL_ID)
if log_channel:
log_embed = discord.Embed(
title="✅ توثيق جديد",
color=0x57F287,
timestamp=discord.utils.utcnow()
)
log_embed.add_field(name="👤 Discord", value=f"{interaction.user.mention}\n{interaction.user}\nID: {interaction.user.id}", inline=True)
log_embed.add_field(name="🎮 Roblox", value=f"{self.username}\nID: {self.roblox_id}\nالبروفايل", inline=True)

log_embed.set_thumbnail(url=interaction.user.display_avatar.url)
data = await get_roblox_full_info(self.username)
if data and data['avatar']:
    log_embed.set_image(url=data['avatar'])
log_embed.set_footer(text=f"تم التوثيق بواسطة {interaction.user}", icon_url=interaction.user.display_avatar.url)
# المنشن هنا
mention = f"<@&{STAFF_MENTION_ID}>" if STAFF_MENTION_ID else ""
await log_channel.send(content=mention, embed=log_embed)

6:26 am, May 24, 2026

log_channel = bot.get_channel(LOG_CHANNEL_ID)
if log_channel:
# رسالة المنشن لوحدها
await log_channel.send(f"{interaction.user.mention} تم توثيق حسابك بنجاح ✅")

# رسالة الإمبد بالمعلومات والصور
log_embed = discord.Embed(
    title="✅ توثيق جديد",
    color=0x57F287,
    timestamp=discord.utils.utcnow()
)
log_embed.add_field(name="👤 Discord", value=f"{interaction.user.mention}\n`{interaction.user}`\nID: `{interaction.user.id}`", inline=True)
log_embed.add_field(name="🎮 Roblox", value=f"**{self.username}**\nID: `{self.roblox_id}`\n[البروفايل](https://www.roblox.com/users/{self.roblox_id}/profile)", inline=True)
log_embed.set_thumbnail(url=interaction.user.display_avatar.url)
data = await get_roblox_full_info(self.username)
if data and data['avatar']:
    log_embed.set_image(url=data['avatar'])
log_embed.set_footer(text=f"تم التوثيق بواسطة {interaction.user}", icon_url=interaction.user.display_avatar.url)
await log_channel.send(embed=log_embed)

6:30 am, May 24, 2026

python main.py
6:33 am, May 24, 2026

import sqlite3
import os

DB_FILE = "verify.db"

def init_db():
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS verifications
(roblox_id INTEGER PRIMARY KEY, discord_id INTEGER)""")
conn.commit()
conn.close()

def is_roblox_linked(roblox_id):
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("SELECT discord_id FROM verifications WHERE roblox_id=?", (roblox_id,))
result = c.fetchone()
conn.close()
return result[0] if result else None

def save_verification(roblox_id, discord_id):
conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("INSERT OR REPLACE INTO verifications VALUES (?,?)", (roblox_id, discord_id))
conn.commit()
conn.close() bot = commands.Bot(command_prefix="!", intents=intents)

init_db() # حط السطر ده هنا @discord.ui.button(label="تأكيد الحساب", style=discord.ButtonStyle.success, emoji="✅", custom_id="confirm_btn")
async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
if interaction.user.id!= self.discord_id:
return await interaction.response.send_message("❌ دي مش رسالتك", ephemeral=True)

# التشييك الجديد
existing_discord = is_roblox_linked(self.roblox_id)
if existing_discord and existing_discord!= interaction.user.id:
    existing_user = await bot.fetch_user(existing_discord)
    return await interaction.response.edit_message(
        content=f"❌ حساب روبلوكس ده مربوط أصلاً بـ {existing_user.mention}",
        embed=None,
        view=None
    )
role = interaction.guild.get_role(VERIFIED_ROLE_ID)
if role:
    try:
        await interaction.user.add_roles(role)
    except discord.Forbidden:
        return await interaction.response.edit_message(
            content="❌ معنديش صلاحية أدي الرتبة. حط البوت فوق رتبة 'موثق'",
            embed=None,
            view=None
        )
# احفظ في الداتا بيز
save_verification(self.roblox_id, interaction.user.id)
# باقي الكود زي ما هو - رسالة التأكيد واللوج
embed = discord.Embed(
    title="✅ تم التوثيق بنجاح",
    description=f"**تم ربط حسابك:**\n**Discord:** {interaction.user.mention}\n**Roblox:** {self.username}\n**ID:** `{self.roblox_id}`",
    color=0x57F287,
    timestamp=discord.utils.utcnow()
)
await interaction.response.edit_message(embed=embed, view=None)
log_channel = bot.get_channel(LOG_CHANNEL_ID)
if log_channel:
    await log_channel.send(f"{interaction.user.mention} تم توثيق حسابك بنجاح ✅")
    #... باقي كود اللوج زي ما هو

6:37 am, May 24, 2026

Build the full Discord bot from the code we made. Make sure main.py has everything and it's runnable. Then tell me when it's ready to publish.
6:43 am, May 24, 2026

from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
return "Bot is alive!"

def run():
app.run(host='0.0.0.0', port=8000)

def keep_alive():
t = Thread(target=run)
t.start()
6:52 am, May 24, 2026
Vmok04601 started: Fix 1 security CVE

const express = require("express");
const app = express();

app.get("/", (req, res) => {
res.send("Bot Online");
});

app.listen(3000, "0.0.0.0", () => {
console.log("Server Ready");
});
8:02 am, May 24, 2026
Completed: Fix 1 security CVE
Updated environment

const express = require("express");
const app = express();

app.get("/", (req, res) => {
res.send("Bot Online");
});

app.listen(3000, "0.0.0.0");
8:22 am, May 24, 2026

What do you want to do with the Express keep-alive code?
Save it as a separate keep_alive.js file alongside the bot
8:22 am, May 24, 2026

const express = require("express");
const app = express();

app.get("/", (req, res) => {
res.send("Bot Online");
});

app.listen(3000, "0.0.0.0", () => {
console.log("Server Ready");
});
8:25 am, May 24, 2026

node keep_alive.js
8:28 am, May 24, 2026

express isn't installed yet at the root level. Let me install it and set up the workflow.

Let me try installing express directly via bash.

Express is installed. Now setting up the workflow to run it.

The server started ("Server Ready" printed) but the workflow monitor marked it failed. Let me restart it directly.

All good — the Keep Alive Server is running on port 3000 and logs "Server Ready". You can see it's active alongside the Discord bot.

Here's what's running now:

    Start application — Discord bot (python main.py) with Flask keep-alive on port 8000
    Keep Alive Server — Node.js Express server on port 3000 (node keep_alive.js)

Next, I can add an !unverify @user admin command to remove a user's verification from the database and take back their verified role. Would you like me to do that?
You're out of credits.

Make, test, iterate…

Simple Server - Replit
Pasted-import-discord-from-discord-ext-import-commands-import-_1779592241619.txt
import discord
from discord.ext import commands
import aiohttp
import os
from datetime import datetime
from flask import Flask
from threading import Thread

# ===== سيرفر ويب عشان Replit يفضل شغال =====
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()
# ============================================

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# === غير دول بس ===
VERIFY_CHANNEL_ID = 1507921235776901260
LOG_CHANNEL_ID = 1507921827304046725
VERIFIED_ROLE_ID = 1507920548309766245
BANNER_URL = "https://media.discordapp.net/attachments/1507921235776901260/1507932470790590484/ChatGPT_Image_24_2026_05_24_35_.png"
# ===================

@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user}")
    bot.add_view(VerifyView())
    bot.add_view(ConfirmView())

@bot.command()
@commands.has_permissions(administrator=True)
async def setup_verify(ctx):
    if ctx.channel.id!= VERIFY_CHANNEL_ID:
        return await ctx.send("❌ استخدم الأمر في روم التوثيق بس", delete_after=5)

    embed = discord.Embed(
        title="🔗 | توثيق حساب روبلوكس",
        description=(
            "**اضغط على الزر بالأسفل واكتب يوزرنيم روبلوكس الخاص بك 🎮**\n"
            "سيتم التحقق من بيانات حسابك بشكل تلقائي وآمن 100% ✅\n\n"
            "━━━━━━━━━━━━━━\n"
            "⭐ **بعد إتمام التوثيق:**\n"
            "• هتستلم رتبة **'موثق'** تلقائيًا\n"
            "• هيتفتحلك كل الرومات والفعاليات الخاصة\n"
            "🔒 **الأمان والخصوصية:**\n"
            "• بياناتك محمية ومش بتتخزن عندنا"
        ),
        color=0x5865F2,
        timestamp=discord.utils.utcnow()
    )
    embed.set_image(url=BANNER_URL)
    embed.set_footer(text="نظام التوثيق الآمن | Powered by Meta AI")

    await ctx.message.delete()
    await ctx.send(embed=embed, view=VerifyView())

class VerifyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.green, emoji="✅", custom_id="verify_btn")
    async def verify_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_modal(VerifyModal())

class VerifyModal(discord.ui.Modal, title="توثيق حساب روبلوكس"):
    roblox_username = discord.ui.TextInput(
        label="اسم حساب روبلوكس",
        placeholder="اكتب اليوزر بالظبط",
        max_length=20,
        required=True
    )

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)
        username = str(self.roblox_username)
        data = await get_roblox_full_info(username)

        if not data:
            return await interaction.followup.send("❌ الحساب ده مش موجود في روبلوكس", ephemeral=True)

        embed = discord.Embed(
            title="🔍 | تأكيد بيانات الحساب",
            description=f"**لقينا الحساب ده. هل هو حسابك؟**",
            color=0xFEE75C,
            timestamp=discord.utils.utcnow()
        )
        embed.add_field(name="👤 Username", value=f"`{data['username']}`", inline=True)
        embed.add_field(name="🏷️ Display Name", value=f"`{data['displayName']}`", inline=True)
        embed.add_field(name="🆔 User ID", value=f"`{data['userId']}`", inline=True)
        embed.add_field(name="📅 تاريخ الإنشاء", value=f"<t:{data['created_timestamp']}:F>", inline=False)
        embed.add_field(name="🔗 البروفايل", value=f"[اضغط هنا](https://www.roblox.com/users/{data['userId']}/profile)", inline=False)

        embed.set_thumbnail(url=data['avatar'])
        embed.set_footer(text="لو البيانات صح دوس 'تأكيد الحساب'")

        view = ConfirmView(data['userId'], data['username'], interaction.user.id)
        await interaction.followup.send(embed=embed, view=view, ephemeral=True)

class ConfirmView(discord.ui.View):
    def __init__(self, roblox_id=None, username=None, discord_id=None):
        super().__init__(timeout=120)
        self.roblox_id = roblox_id
        self.username = username
        self.discord_id = discord_id

    @discord.ui.button(label="تأكيد الحساب", style=discord.ButtonStyle.success, emoji="✅", custom_id="confirm_btn")
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id!= self.discord_id:
            return await interaction.response.send_message("❌ دي مش رسالتك", ephemeral=True)

        role = interaction.guild.get_role(VERIFIED_ROLE_ID)
        if role:
            try:
                await interaction.user.add_roles(role)
            except discord.Forbidden:
                return await interaction.response.edit_message(
                    content="❌ معنديش صلاحية أدي الرتبة. حط البوت فوق رتبة 'موثق'",
                    embed=None,
                    view=None
                )

        embed = ...
