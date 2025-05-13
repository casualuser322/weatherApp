import requests
import asyncio
import aiohttp

ADDRESS = "http://api.openweathermap.org/data/2.5/weather?appid=c0acbd35d1cb1dc1b8e2f629dfad003e"

class WeatherAPI:
    def __init__(self, city: str):
        self.city = city
        self.url = f"{ADDRESS}&q={self.city}"
        self.data = None
         
    async def get_weather(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url) as response:
                if response.status == 200:
                    self.data = await response.json()
                    return self.data
                elif response.status == 404:
                    raise Exception(f"City {self.city} not found.")
                elif response.status == 429:
                    raise Exception("Too many requests. Please try again later.")
                else:
                    raise Exception(f"Error fetching weather data: {response.status}")