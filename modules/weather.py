import requests

class Weather:
    def __init__(self, api_key):
        self.api_key = api_key

    def show_weather(self, city):
        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric&lang=pt_br"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                print(f"Clima em {city}: {data['weather'][0]['description'].capitalize()}")
                print(f"Temperatura: {data['main']['temp']}°C")
            elif response.status_code == 404:
                print("Cidade não encontrada. Tente novamente.")
            else:
                print(f"Erro na API: {response.status_code}. Tente novamente mais tarde.")
        except requests.RequestException as e:
            print(f"Erro de conexão: {e}")

