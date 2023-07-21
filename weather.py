import requests

def Weather(city):
    api_key = '7075a4e2c739b64f7325fd60add08086'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'




    response = requests.get(base_url).json()
    

    #print(tmp)


    if 'message' in response and response['message'] == "city not found":
        return None
    elif 'main' in response and 'temp' in response['main']:
        temp = response['main']['temp'] - 273
        temp= round(temp,2)
        hum = response['main']['humidity']
        return {"temp":temp,"hum":hum}
    else:
        return None







