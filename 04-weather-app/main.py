import typer
import requests

BASE_WEATHER_URL="https://api.open-meteo.com/v1/forecast"
BASE_GEO_URL="https://geocoding-api.open-meteo.com/v1/search"
app=typer.Typer()

@app.command()
def check_weather(city:str)->None:
    geo_req=requests.get(f"{BASE_GEO_URL}",params={
        "name":city,
        "count":1
    })

    location = geo_req.json()["results"][0]
    lat=location["latitude"]
    long=location["longitude"]

    weather_req=requests.get(f"{BASE_WEATHER_URL}",params={
        "latitude": lat,
        "longitude": long,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    })

    res=weather_req.json()["current"]

    print("City:", location["name"])
    print("Temperature:", res["temperature_2m"], "°C")
    print("Humidity:", res["relative_humidity_2m"], "%")
    print("Wind Speed:", res["wind_speed_10m"], "km/h")



if __name__=="__main__":
    app()