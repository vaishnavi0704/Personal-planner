import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(latitude=19.07, longitude=72.87):  # Mumbai example
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    weather = data.get("current_weather", {})
    temp = weather.get("temperature")
    wind = weather.get("windspeed")
    return f"Temp: {temp}°C, Wind: {wind} km/h"

def get_news():
    api_key = os.getenv("NEWS_API_KEY")
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])[:5]
    headlines = [f"- {article['title']}" for article in articles]
    return "\n".join(headlines)
