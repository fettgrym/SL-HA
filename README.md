# Next Departure Information Fetcher

This Python script is designed to fetch the next departure information for a specific destination from a public transportation API. It queries the API for departures from a specified station, filters the departures for a given destination, and formats the departure times before returning the next departure details in JSON format.

## Features
- Fetch departure information from a specified URL.
- Filter departures by destination.
- Format departure times.
- Return the next departure information as JSON.

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
The script is designed to be used as a module. However, it can also be run directly. To use it directly, follow these steps:
1. Modify the `HEADERS`, `STATION`, and `DESTINATION` variables in the script to match your requirements.
2. Run the ID script:
```bash
python stationID.py
```
That will output a file with all available stations with their corresponding ID. Place this ID in the variable `STATION`. 

Change the variable `DESTINATION`to the name of your station(Not the ID).
```bash
python sl_departures.py
```
<img width="1181" alt="image" src="https://github.com/fettgrym/SL-HA/assets/15312902/5e7faf9f-3f14-47dd-8c83-82b63e07d3ea">

## Functions
- `get_departures(headers, url)`: Fetches departure data from the specified URL using the provided headers.
- `extract_next_departure(departures_data, destination)`: Extracts the next departure for the specified destination from the departure data.
- `format_departure_time(departure, key)`: Formats the departure time in the departure data.
- `get_next_departure_info(headers, url, destination)`: Orchestrates the fetching, filtering, and formatting of departure information.

## Example Output
```json
{
  "next_departure": {
    "destination": "Stockholms östra",
    "expected": "15:30",
    "scheduled": "15:25"
  }
}
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This README provides a basic overview and guide on how to use the script. You can customize it further based on the specifics of your project or repository.
