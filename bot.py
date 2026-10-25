import os
import discord
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

# permission integer 5630188876843072

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

    try:
        synced = await tree.sync()
        print(f"🔄 Synced {len(synced)} command(s) globally.")
    except Exception as e:
        print(f"❌ Error syncing commands: {e}")

@tree.command(name="whoami", description="Heroes cannot be real...")
async def whoami(interaction: discord.Interaction):
    await interaction.response.send_message(f"...Thou mayest know my name as Quixote! The righteous Fixer of justice, Don Quixote!")

@tree.command(name="peam", description="its so peam!")
async def peam(interaction: discord.Interaction):
    await interaction.response.send_message(f"https://giphy.com/gifs/don-quixote-qui-limbus-company-OlL7fNmWcpity669PH")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "fixer of justice":
        await message.channel.send(f":3")

    if message.content.lower() == "it's peam!":
        await message.channel.send(f"https://giphy.com/gifs/don-quixote-qui-limbus-company-OlL7fNmWcpity669PH")


client.run(TOKEN)
