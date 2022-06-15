import requests
import discord,os
from dotenv import load_dotenv

load_dotenv()
api_endpoint ="https://api.openweathermap.org/data/2.5/onecall"
api_key= os.getenv('API_KEY')
DISCORDTOKEN = os.getenv('DISCORD_TOKEN')
# get the weather data and check is it going to rain?------------------------------
parser={
    "lat": 42.36,
    "lon":71.05,
    "exclude": "current,minutely,daily",
    "appid" : api_key
}
response = requests.get(api_endpoint,params=parser)
weather_data = response.json()
weather_hourly =weather_data["hourly"]
# weather_hourly[hour]["weather"][0]["id"] = the weather id for that hour
# loop through 12 hours
# if the weather id is less than 600, put the id to the list
predit_weather_id = [weather_hourly[hour]["weather"][0]["id"] for hour in range(0,12) if weather_hourly[hour]["weather"][0]["id"]< 600]



#load my discord clinet
bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    # get the channel
    channel = bot.get_channel(986467816746147873)
    # if list has something means it is going to rain
    if predit_weather_id:
        await channel.send("bring the ☂")
    else:
        await channel.send("good to go")

    # Turn off the bot
    try:
        await bot.close()
    except:
        pass

bot.run(DISCORDTOKEN)