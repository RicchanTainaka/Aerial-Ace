import os
import discord

# Bot data
TOKEN = os.environ["TOKEN"]
TEST_TOKEN = os.environ["TEST_TOKEN"]
ADMIN_ID = os.environ["ADMIN_ID"]
POKETWO_ID = os.environ["POKETWO_ID"]

# Mongo Data
MONGO_URI = os.environ["MONGO"]

# bot links
INVITE_LINK = "https://discord.com/api/oauth2/authorize?client_id=908384747393286174&permissions=277025647680&scope=bot%20applications.commands"
AVATAR_LINK = "https://cdn.discordapp.com/avatars/908384747393286174/312dafe2a71e0338db6f2ef5315899a7.webp"
SUPPORT_SERVER_LINK = "https://discord.gg/4mPdqevgsH"
REPO_LINK = "https://github.com/Devanshu19/Aerial-Ace"
GITHUB_PROFILE_LINK = "https://github.com/Devanshu19/"
VOTE_LINK = "https://top.gg/bot/908384747393286174/"

# file locations
SERVER_FILE_LOCATION = "data/servers.json"
STATS_FILE_LOCATION = "data/stats.json"
FAV_FILE_LOCATION = "data/fav.json"
TAG_FILE_LOCATION = "data/tags.json"
MOVESET_FILE_LOCATION = "data/moveset.json"
BATTLE_LOG_FILE_LOCATION = "data/battle_log.json"
ALT_NAME_FILE_LOCATION = "data/poke_alt_names.json"
RARITY_FILE_LOCATION = "data/poke_rarity.json"
NATURE_FILE_LOCATION = "data/nature.json"
TYPE_FILE_LOCATION = "data/type_data.json"
WEAKNESS_FILE_LOCATION = "data/weakness_data.json"

# colors
NORMAL_COLOR = discord.Color.blue()
ERROR_COLOR = discord.Color.red()
WARNING_COLOR = discord.Color.orange()
RARE_CATCH_COLOR = discord.Color.gold()

# Reactions
PIKA_WOW = "https://cdn.discordapp.com/attachments/911547825274388511/918840026094247976/pika_woo.png"
JIRACHI_WOW = "https://cdn.discordapp.com/attachments/911547825274388511/918840025477681152/jirachi_wow.png"
PIKA_SHOCK = "https://cdn.discordapp.com/attachments/911547825274388511/918840025746137158/pika_shock.png"

TIER_LINK = {
    "rare" : "https://media.discordapp.net/attachments/793689115689353247/924912850953195520/IMG_0018.png",
    "mega" : "https://cdn.discordapp.com/attachments/774499540938129429/870761603153416202/my-image_50.png",
    "common" : " https://media.discordapp.net/attachments/839209309371891802/900488066437894144/my-image_271.png https://media.discordapp.net/attachments/839209309371891802/900488066756640888/my-image_2721.png https://media.discordapp.net/attachments/839209309371891802/900488065229942804/my-image_272.png https://media.discordapp.net/attachments/839209309371891802/900488065594826863/my-image_273.png",
    "bug" : "https://media.discordapp.net/attachments/774499540938129429/845692957214375966/image0.png",
    "dark" : "https://cdn.discordapp.com/attachments/918973688932630589/935020376717672448/my-image_6.png",
    "dragon" : "https://cdn.discordapp.com/attachments/793689115689353247/931947498937921596/my-image_3.png",
    "electric" : "https://cdn.discordapp.com/attachments/793689115689353247/868569489938210836/my-image_46.png",
    "fairy" : "https://cdn.discordapp.com/attachments/793689115689353247/936020121900703744/my-image_11.png",
    "fighting" : "https://cdn.discordapp.com/attachments/718008298837770290/901298772783558716/my-image_14.png",
    "fire" : "https://cdn.discordapp.com/attachments/899753866638266418/900555487437807657/my-image_11.png",
    "flying" : "https://cdn.discordapp.com/attachments/774499540938129429/887928654116552724/my-image.png", 
    "ghost" : "https://media.discordapp.net/attachments/718008298837770290/844752635684454460/image0.png",
    "grass" : "https://media.discordapp.net/attachments/793689115689353247/920423300692332564/IMG_9676.png",
    "ground" : "https://cdn.discordapp.com/attachments/718008298837770290/866929735920254976/my-image_43.png",
    "ice" : "https://media.discordapp.net/attachments/774499540938129429/850456657120591943/my-image_9.png",
    "normal" : "https://cdn.discordapp.com/attachments/718008298837770290/896314513895329853/my-image_1.png",
    "poison" : "https://cdn.discordapp.com/attachments/718008298837770290/934966138415239198/my-image_4.png",
    "psychic" : "https://cdn.discordapp.com/attachments/877212831240560752/909264788935311360/my-image_17.png",
    "rock" : "https://cdn.discordapp.com/attachments/718008298837770290/900550270050787358/my-image_8.png",
    "steel" : "https://cdn.discordapp.com/attachments/918973688932630589/935029992541278208/my-image_8.png",
    "water" : "https://cdn.discordapp.com/attachments/774499540938129429/876979764773126225/my-image_55.png"
}