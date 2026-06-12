# SA Weather CLI

A command-line tool that fetches live weather data for any city in South Africa.
Built to practise Python fundamentals, API integration, and JSON parsing.

## Features

- Live temperature and humidity for any SA city
- Two chained API calls — geocoding and weather data
- Clean terminal output
- Handles invalid city input gracefully

## Tech stack

- Python 3
- `requests` library
- Open-Meteo API (weather data)
- Nominatim API via OpenStreetMap (geocoding)

## How to run

Clone the repo:
```bash
git clone https://github.com/thapelongcobo3/sa-weather-cli.git
cd sa-weather-cli
```

Install dependencies:
```bash
pip install requests
```

Run the tool:
```bash
python weather.py
```

## Example output
Enter city: Durban
Durban, South Africa
Temperature: 24.8°C
Humidity: 72%

## What I learned

- How to chain two API calls where the output of one feeds into the next
- Parsing nested JSON responses using direct dictionary access
- Structuring Python scripts with clean reusable functions
- Why `params` is safer than f-strings for building URLs with user input

## Future improvements

- Add wind speed and weather conditions
- Support for cities outside South Africa
- Save weather history to a local database
