import requests
from tkinter import *
import os

GEO_ENDPOINT = "http://api.openweathermap.org/geo/1.0/direct"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

API_KEY = os.environ.get("API_KEY")



def fetch_weather():
    location = location_entry.get().lower()
    geo_params = {
        "q": location,
        "appid": API_KEY,
        "limit": 1

    }
    geo_response = requests.get(GEO_ENDPOINT,params=geo_params)
    geo_response.raise_for_status()
    geo_data = geo_response.json()
    weather_param = {
        "lat": geo_data[0]['lat'],
        "lon": geo_data[0]['lon'],
        "cnt": 4,
        "appid": API_KEY
    }
    weather_response = requests.get(WEATHER_ENDPOINT, params=weather_param)
    weather_response.raise_for_status()
    weather_data = weather_response.json()
    weather_description = weather_data['weather'][0]['description']
    temp = round(weather_data['main']['temp'] - 273.15)
    canvas.itemconfig(weather_info, text=f"{location.title()}\n{weather_description.title()}, {temp}°C")



#--------------------UI-------------------------------#
FONT= ("corbel", 14, "bold")

window = Tk()
window.title("Weather Forcast")
window.geometry("400x250+500+300")
window.iconbitmap("")
window.config(padx=20, pady=20, bg="white")


#Label
location_label = Label(text="Enter location:", font=FONT, fg="black", bg="white")
location_label.grid(column=0, row=0, sticky="W", pady=3)

#Entry
location_entry = Entry(width=25, bg="white", fg="black", insertbackground="black")
location_entry.grid(column=0, row=1, pady=5, sticky="W")

#Button
search_button = Button(text="Search",highlightthickness=0, bg="white", command=fetch_weather, highlightbackground="white", height=1)
search_button.grid(column=1, row=1)



canvas = Canvas(width=350, height=150, bg="white", highlightthickness=0)
weather_info = canvas.create_text(175,75, text="", fill="black", font=("corbel", 24), width=330, anchor="center", justify="center")
canvas.grid(column=0, row=2, columnspan=2, sticky="W")




window.mainloop()