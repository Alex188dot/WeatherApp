# Weather App

This is a simple Python app that uses the OpenWeatherMap API to get the current weather data for a given city in the world and display it in a graphical user interface (GUI) using Tkinter and Pillow.

## Requirements

To run this app, you need to have Python 3 installed on your system. You also need to install the following packages using pip:

- requests
- json
- tkinter
- pillow

And you need to get a free API key from OpenWeatherMap by signing up on their website: https://openweathermap.org/api

## Usage

To run this app, you need to replace the value of the API_KEY constant in the code with your own API key. You can also change the value of the CITY_NAME constant to any city you want, followed by a comma and an ISO 3166-2 country code. For example, "New York, US" or "Paris, FR".

Then, you can run the app by typing the following command in your terminal:

`python weatherAppFinal.py`

A GUI window will pop up showing an image of the current weather conditions and some text labels with the weather information, expressed in Celsius. You can close the window by clicking on the X button on the top right corner (or top left corner if you have a Mac).

## Example

Here is an example of how the app looks like when run with the default city name of "Rome, IT":


<img width="400" alt="Rome, IT" src="https://github.com/Alex188dot/WeatherApp/assets/117444853/db5d327e-aae8-4f76-b339-ddded7b3a11b">
