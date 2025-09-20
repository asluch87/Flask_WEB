import requests
from weather import weather_by_city
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Привет!"


@app.route('/app')
def index():
    try:
        weather_data = weather_by_city("Moscow,Russia")
        
        # Проверяем структуру ответа API
        if 'data' in weather_data and 'current_condition' in weather_data['data']:
            current = weather_data['data']['current_condition'][0]
            return f"Сейчас {current['temp_C']}°C, ощущается как {current['FeelsLikeC']}°C"
        else:
            return "Прогноз сейчас недоступен или ошибка в данных API"
            
    except Exception as e:
        return f"Ошибка получения погоды: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)