import discord
import json

intents = discord.Intents.default()
intents.members = True  # To track new members

client = discord.Client(intents=intents)

# Load configurations from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

WELCOME_CHANNEL_ID = config["WELCOME_CHANNEL_ID"]
ROLE_ID = config["ROLE_ID"]
TOKEN = config["DISCORD_TOKEN"]
WELCOME_MESSAGE = config["WELCOME_MESSAGE"]

@client.event
async def on_member_join(member):
    welcome_channel = client.get_channel(WELCOME_CHANNEL_ID)
    role = discord.utils.get(member.guild.roles, id=ROLE_ID)  # Get the role by ID

    if role:
        await member.add_roles(role)
        await welcome_channel.send(WELCOME_MESSAGE.format(member=member))

# Run the bot with the token
try:
    client.run(TOKEN)
except discord.HTTPException as e:
    if e.status == 429:
        print("The Discord servers denied the connection for making too many requests")
    else:
        raise e
