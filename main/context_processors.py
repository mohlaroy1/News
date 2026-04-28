import requests
import datetime

def weather(request):
    city='fergana'
    token='07b099488fdc42c2b76171123262704'
    data=requests.get(f'https://api.weatherapi.com/v1/current.json?q={city}&key={token}').json()
    temp_c=data.get('current').get('temp_c')
    icon=data.get('current').get('condition').get('icon')

    return {
        'temp_c': temp_c,
        'icon': icon,
        'time': datetime.datetime.now().strftime('%d.%m.%Y %H:%M')
    }
