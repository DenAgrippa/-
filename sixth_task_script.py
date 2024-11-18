import requests
import json
from bs4 import BeautifulSoup

url = "https://api.open-meteo.com/v1/forecast?latitude=56.8519&longitude=60.6122&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,cloud_cover,wind_speed_10m,wind_direction_10m"
data = requests.get(url).json()


soup = BeautifulSoup('', 'html.parser')

main_ul = soup.new_tag('ul')

for key, value in data.items():
    li = soup.new_tag('li')

    if isinstance(value, dict):
        li.string = key + ": "
        sub_ul = soup.new_tag('ul')
        for sub_key, sub_value in value.items():
            sub_li = soup.new_tag('li')
            sub_li.string = f"{sub_key}: {sub_value}"
            sub_ul.append(sub_li)
        li.append(sub_ul)
    else:
        li.string = f"{key}: {value}"
    
    main_ul.append(li)


with open("./results/sixth_task_result.html", "w", encoding="utf-8") as file:
    file.write(main_ul.prettify())

