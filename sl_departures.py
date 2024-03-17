from dateutil.parser import parse
from datetime import time
import json
import requests
from datetime import datetime

def get_departures(headers, url):
    departures_vallentuna = requests.get(url, headers=headers, timeout=5)
    departures_data = departures_vallentuna.json()
    return departures_data

def extract_next_departure(departures_data, destination):
    next_departure = next((departure for departure in departures_data["departures"] if departure["destination"] == destination), None)
    return next_departure

def format_departure_time(departure, key):
    if key in departure:
        datetime_obj = parse(departure[key])
        departure[key] = datetime_obj.time().strftime("%H:%M")

def get_next_departure_info(headers, url, destination):
    departures_data = get_departures(headers, url)
    next_departure = extract_next_departure(departures_data, destination)
    if next_departure:
        format_departure_time(next_departure, 'expected')
        format_departure_time(next_departure, 'scheduled')
        json_output = {"next_departure": next_departure}
        return json_output

HEADERS = {"Content-Type": "application/json"}
STATION = "9626"
VALLANTUNA_STATION = "https://transport.integration.sl.se/v1/sites/{}/departures?transport=TRAM&line=27&forecast=60".format(STATION)
DESTINATION = "Stockholms östra"

result = get_next_departure_info(HEADERS, VALLANTUNA_STATION, DESTINATION)
print(json.dumps(result))