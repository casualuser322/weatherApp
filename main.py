import asyncio
import aiohttp

from api.weather.api import WeatherAPI

async def main():
    weatherEngine = WeatherAPI("Haifa, Il")
    data = await weatherEngine.get_weather()
    temp = int(round(data['main']['feels_like'] - 273.15, 0))
    print(temp, "°C")

if __name__ == '__main__':
    asyncio.run(main())