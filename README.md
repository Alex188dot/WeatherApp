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

Here is an example of how the app looks like with different weather conditions:

<p align="center">
  <img width="597" alt="WA1" src="https://github.com/Alex188dot/WeatherApp/assets/117444853/4478f737-6264-40b4-9d29-81b66b6bd932">
</p>

<p align="center">
  <img width="592" alt="WA2" src="https://github.com/Alex188dot/WeatherApp/assets/117444853/0ce3f43c-e16a-4306-8ab2-659c3968fd54">
</p>

<p align="center">
  <img width="597" alt="WA3" src="https://github.com/Alex188dot/WeatherApp/assets/117444853/f9ecbba0-5999-4c95-b270-0c676f4d702c">
</p>

<p align="center">
  <img width="594" alt="WA4" src="https://github.com/Alex188dot/WeatherApp/assets/117444853/32a5809c-8c8d-453e-b3a5-5c28424199c6">
</p>
