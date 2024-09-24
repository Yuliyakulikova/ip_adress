import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='208.95.112.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)
        data = {
            '[IP]': response.get('query'),  # ip
            '[Int prov]': response.get('isp'),  # интернет провайдер
            '[Org]': response.get('org'),  # организация
            '[Country]': response.get('country'),  # страна
            '[Region Name]': response.get('regionName'),  # регион
            '[City]': response.get('city'),  # город
            '[ZIP]': response.get('zip'),  # почт код
            '[Lat]': response.get('lat'),  # широта
            '[Lon]': response.get('lon'),  # долгота
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')


def main():
    preview_text = Figlet(font='standard')
    print(preview_text.renderText('ip.python'))
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)

main()