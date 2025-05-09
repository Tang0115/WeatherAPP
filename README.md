# Weather App

A modern and user-friendly weather application built with Python and ttkbootstrap that provides real-time weather information for any city worldwide.

## Features

- 🔍 Search for weather by city name
- 🌡️ Display current temperature
- 🔄 Toggle between Celsius and Fahrenheit
- 🖼️ Weather condition icons
- 📍 Location display with country code
- 💬 Weather description
- ⌨️ Enter key support for quick searches
- 🎨 Modern UI with ttkbootstrap theme

## Prerequisites

- Python 3.x
- Virtual Environment (recommended)

## Required Packages

- tkinter
- ttkbootstrap
- Pillow (PIL)
- requests

## Installation

1. Clone the repository or download the source code:
```bash
git clone <repository-url>
cd WeatherAPP
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install ttkbootstrap pillow requests
```

4. Get your API key:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/)
   - Navigate to your account dashboard
   - Generate an API key
   - Replace the placeholder in `WeatherAPP.py`:
     ```python
     API_key = "Enter API here"  # Replace with your actual API key
     ```

## Usage

1. Activate the virtual environment if not already activated:
```bash
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

2. Run the application:
```bash
python WeatherAPP/WeatherAPP.py
```

3. Enter a city name in the search box and either:
   - Press Enter
   - Click the Search button

4. The app will display:
   - City name and country
   - Current temperature
   - Weather condition icon
   - Weather description

5. Use the temperature unit toggle button to switch between Celsius and Fahrenheit

## Features Explanation

- **Search Functionality**: Enter any city name to get real-time weather data
- **Temperature Units**: Toggle between Celsius (°C) and Fahrenheit (°F)
- **Visual Weather Representation**: Weather conditions are displayed with corresponding icons
- **Responsive Design**: Modern and clean interface using ttkbootstrap's "morph" theme
- **Error Handling**: Displays error message for invalid city names or API issues

## Technical Details

The application is built using:
- `tkinter` and `ttkbootstrap` for the GUI
- `requests` library for API calls to OpenWeatherMap
- `PIL` (Python Imaging Library) for handling weather icons
- Object-Oriented Programming with the `WeatherApp` class

## Error Handling

The app includes error handling for:
- Invalid city names
- Network connection issues
- API response errors

## Contributing

Feel free to fork the repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- UI components powered by [ttkbootstrap](https://ttkbootstrap.readthedocs.io/) 
