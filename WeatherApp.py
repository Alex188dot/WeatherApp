import requests
import tkinter as tk
from PIL import ImageTk, Image

# Define constants
API_KEY = "your-api-key"  # Get your API key from OpenWeatherMap
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY_NAME = "Rome, IT"  # Change this to any city you want, followed by a comma and ISO 3166-2 country code

# Make API call and get response
URL = BASE_URL + "q=" + CITY_NAME + "&appid=" + API_KEY

# This code will center the window
def centerWindow(window):
    width = 600  # Width
    height = 400  # Height

    screen_width = window.winfo_screenwidth()  # Width of the screen
    screen_height = window.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    window.geometry('%dx%d+%d+%d' % (width, height, x, y))


try:
    response = requests.get(URL)
    if response.status_code == 200:  # Check if the request was successful
        data = response.json()
        # Get relevant data from JSON response
        temp = int(data["main"]["temp"] - 273.15)  # Convert from Kelvin to Celsius and round to integer
        feels_like = int(data["main"]["feels_like"] - 273.15)  # Convert from Kelvin to Celsius and round to integer
        temp_min = int(data["main"]["temp_min"] - 273.15)  # Convert from Kelvin to Celsius and round to integer
        temp_max = int(data["main"]["temp_max"] - 273.15)  # Convert from Kelvin to Celsius and round to integer
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["main"]
        description = data["weather"][0]["description"]

        # Assign the corresponding image file name to IMG_PATH based on weather type
        if weather == "Clear":
            IMG_PATH = "sunny.png"
        elif weather == "Clouds":
            IMG_PATH = "cloudy.png"
        elif weather == "Rain":
            IMG_PATH = "rainy.png"
        elif weather == "Snow":
            IMG_PATH = "snowy.png"
        elif weather == "Thunderstorm":
            IMG_PATH = "thunderstorm.png"
        elif weather == "Mist":
            IMG_PATH = "mist.png"
        else:
            IMG_PATH = "weather.png"  # Default image for other weather types

        # Create GUI window
        window = tk.Tk()
        window.title("Weather App")
        window.geometry("400x400")
        window.configure(bg="light blue")

        # Create image object and label
        img = ImageTk.PhotoImage(Image.open(IMG_PATH))
        panel = tk.Label(window, image=img)
        panel.pack(side="top", fill="both", expand="yes")

        # Create text label for city name
        city_label = tk.Label(window, text=CITY_NAME, font=("Arial", 20), bg="light blue")
        city_label.configure(fg="black")
        city_label.pack()

        # Create text label for weather information
        info_label = tk.Label(window,
                              text=f"{weather}: {description}\nTemperature: {temp:.0f}°C\nFeels like: {feels_like:.0f}°C\nMin temp: {temp_min:.0f}°C\nMax temp: {temp_max:.0f}°C\nPressure: {pressure} hPa\nHumidity: {humidity}%",
                              font=("Arial", 10), bg="light blue")
        info_label.configure(fg="black")
        info_label.pack()

        #Call function to center window
        centerWindow(window)
        # Start GUI loop
        window.mainloop()
    else:  # The request was not successful
        print(f"Error: Unable to get weather data for {CITY_NAME}. Status code: {response.status_code}")
except Exception as e:  # Something else went wrong
    print(f"Error: {e}")

