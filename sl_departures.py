from dateutil.parser import parse
import requests
import json

def get_departures(headers, url):
    departures_response = requests.get(url, headers=headers, timeout=5)
    departures_data = departures_response.json()
    return departures_data

def extract_upcoming_departures(departures_data, destination, num_departures=2):
    upcoming_departures = [departure for departure in departures_data["departures"] if departure["destination"] == destination][:num_departures]
    return upcoming_departures

def format_departure_time(departure, key):
    if key in departure:
        datetime_obj = parse(departure[key])
        departure[key] = datetime_obj.time().strftime("%H:%M")

def get_upcoming_departures_info(headers, url, destination, num_departures=2):
    departures_data = get_departures(headers, url)
    upcoming_departures = extract_upcoming_departures(departures_data, destination, num_departures)
    for departure in upcoming_departures:
        format_departure_time(departure, 'expected')
        format_departure_time(departure, 'scheduled')
    json_output = {"upcoming_departures": upcoming_departures}
    return json_output

HEADERS = {"Content-Type": "application/json"}

STATION = "9626"
DIRECTION = "1"
TRANSPORT = "TRAM"
LINE = "27"
FORECAST = "60"
DESTINATION = "Stockholms östra"

API = f"https://transport.integration.sl.se/v1/sites/{STATION}/departures?transport={TRANSPORT}&direction={DIRECTION}&line={LINE}&forecast={FORECAST}"

result = get_upcoming_departures_info(HEADERS, API, DESTINATION, 2)
print(json.dumps(result))