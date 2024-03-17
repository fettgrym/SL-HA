# SL Next Departure Information Fetcher

This Python script is designed to fetch the next departure information for a specific destination from a public transportation API(No API key needed). It queries the API for departures from a specified station, direction, line, transportation method and filters the departures for a given destination, and formats the departure times before returning the next departure details in JSON format.

## Features
- Fetch departure information from a specified URL.
- Filter departures by destination.
- Format departure times.
- Return the two next departure information as JSON.

## Requirements
- Python 3.x
- `requests` library
- `python-dateutil` library

## Installation
First, ensure that you have Python installed on your system. Then, install the required libraries using pip:

```bash
pip install requests python-dateutil
```

## Usage
- `STATION` - Station ID.
- `DESTINATION` - Station name.
- `DIRECTION` - Which direction, 1. or 2
- `TRANSPORT` - Way of transportation - `BUS`, `TRAM`, `METRO`, `TRAIN`, `FERRY`, `SHIP` or `TAXI`.
- `LINE` - Line number
- `FORECAST` - Forecast in minutes(Only capable of displaying two forecasts)


The script is designed to be used as a module. However, it can also be run directly.

1. Place the python script in the folder `/config/custom_components/SL/` on your Home Assistant. Make the folder if you don't already have it.
   
2. Run the ID script:
```bash
python stationID.py
```
That will output a file with all available stations with their corresponding ID. Place this ID in the variable `STATION`. 

3. Modify the `STATION`, `DESTINATION`, `DIRECTION`, `TRANSPORT`, `LINE` and `FORECAST` variables in the script to match your requirements.

4. Add the following to your `Configuration.yaml` file to display all the sensors.

```bash
command_line:
  - sensor:
      name: SL Departures - First Destination
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].destination'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Destination
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].destination'"
      scan_interval: 20

  - sensor:
      name: SL Departures - First Direction
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].direction'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Direction
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].direction'"
      scan_interval: 20

  - sensor:
      name: SL Departures - First Display
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].display'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Display
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].display'"
      scan_interval: 20

  - sensor:
      name: SL Departures - First Scheduled
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].scheduled'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Scheduled
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].scheduled'"
      scan_interval: 20

  - sensor:
      name: SL Departures - First Expected
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].expected'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Expected
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].expected'"
      scan_interval: 20

  - sensor:
      name: SL Departures - First Deviations
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[0].deviations'"
      scan_interval: 20

  - sensor:
      name: SL Departures - Second Deviations
      command: "python3 /config/custom_components/SL/sl_departures.py | jq -r '.upcoming_departures[1].deviations'"
      scan_interval: 20
```

5. Restart your Home Assistant.
   
<img width="1181" alt="image" src="https://github.com/fettgrym/SL-HA/assets/15312902/5e7faf9f-3f14-47dd-8c83-82b63e07d3ea">

That card is configured as this:
```bash
      - type: vertical-stack
        cards:
          - type: vertical-stack
            cards:
              - type: entities
                entities:
                  - entity: sensor.sl_departures_first_destination
                    name: Slutstation
                    icon: mdi:train
                  - entity: sensor.sl_departures_first_display
                    name: Avgångstid
                    icon: mdi:timer
                  - entity: sensor.sl_departures_first_expected
                    name: Förväntad avgångstid
                    icon: mdi:clock-time-eight
          - type: vertical-stack
            cards:
              - type: entities
                entities:
                  - entity: sensor.sl_departures_second_destination
                    name: Slutstation
                    icon: mdi:train
                  - entity: sensor.sl_departures_second_display
                    name: Avgångstid
                    icon: mdi:timer
                  - entity: sensor.sl_departures_second_expected
                    name: Förväntad Avgångstid
                    icon: mdi:clock-time-eight
```
## Functions
- `get_departures(headers, url)`: Fetches departure data from the specified URL using the provided headers.
- `extract_next_departure(departures_data, destination)`: Extracts the next departure for the specified destination from the departure data.
- `format_departure_time(departure, key)`: Formats the departure time in the departure data.
- `get_next_departure_info(headers, url, destination)`: Orchestrates the fetching, filtering, and formatting of departure information.

## Example Output (If runned directly)
```json
{
  "upcoming_departures":[
    {
      "destination":"Stockholms \u00f6stra",
      "direction_code":1,
      "direction":"Stockholms \u00f6stra",
      "state":"ATSTOP",
      "display":"1 min",
      "scheduled":"16:00",
      "expected":"16:00",
      "journey":{
        "id":2024031707519,
        "state":"NORMALPROGRESS",
        "prediction_state":"NORMAL"
      },
      "stop_area":{
        "id":7361,
        "name":"Vallentuna",
        "type":"TRAMSTN"
      },
      "stop_point":{
        "id":7362,
        "name":"Vallentuna",
        "designation":"2"
      },
      "line":{
        "id":27,
        "designation":"27",
        "transport_mode":"TRAM",
        "group_of_lines":"Roslagsbanan"
      },
      "deviations":[
        
      ]
    },
    {
      "destination":"Stockholms \u00f6stra",
      "direction_code":1,
      "direction":"Stockholms \u00f6stra",
      "state":"EXPECTED",
      "display":"16 min",
      "scheduled":"16:15",
      "expected":"16:15",
      "journey":{
        "id":2024031707425,
        "state":"EXPECTED"
      },
      "stop_area":{
        "id":7361,
        "name":"Vallentuna",
        "type":"TRAMSTN"
      },
      "stop_point":{
        "id":7362,
        "name":"Vallentuna",
        "designation":"2"
      },
      "line":{
        "id":27,
        "designation":"27",
        "transport_mode":"TRAM",
        "group_of_lines":"Roslagsbanan"
      },
      "deviations":[
        
      ]
    }
  ]
}
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## LICENSE
MIT License

Copyright (c) 2024

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


This README provides a basic overview and guide on how to use the script. You can customize it further based on the specifics of your project or repository.
