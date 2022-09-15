import requests

APPID = "e9f6751327674d4f5e452ad799d8146c"
CITY = 'London'
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={APPID}"

def get_weather_data():
    response = requests.get(URL) # get devuelve un objeto
    # print(response, type(response))
    http_response_code = response.status_code
    data = response.json() # metodo json nos permite leer los datos
    # print(http_response_code, type(http_response_code))
    # print(data, type(data))

    #returns tuple
    return response.status_code, data

def main():
    response = get_weather_data()
    status_code, weather_json = response
    if status_code != 200:
        print(f'Bad request {status_code}')
    else:
        main_weather = weather_json.get('main')
        temp = main_weather.get('temp')
        print(f'The circus current temperature is {temp}° farenheit')

main()