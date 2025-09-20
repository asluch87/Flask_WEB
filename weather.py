import requests

def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "d24a2d5cf9fa4e34983150243251909",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    return result.json()





if __name__ == "__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)