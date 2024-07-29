from get_location_api import get_location_response
from weather_api import get_weather_response
from io import BytesIO
import customtkinter as ctk
import requests
from PIL import Image, ImageTk

def get_lat_lon_from_zip(zip):
    location_dict = get_location_response(zip)
    return location_dict

def get_response_using_lat_lon(location_dict):
    lat = location_dict['lat']
    lon = location_dict['lon']
    lat_lon_response = get_weather_response(lat, lon)
    print(lat_lon_response)
    return lat_lon_response


# Update weather information on the GUI
def update_weather():
    zip = zip_entry.get()
    if zip.isnumeric():
        location_response = get_lat_lon_from_zip(zip)
        weather = get_response_using_lat_lon(location_response)
        if weather:
            temp_label.configure(text=f"{int(weather['main']['temp'])}°F")
            desc_label.configure(text=f"{(weather['weather'][0]['description']).capitalize()}")
            city_label.configure(text=f"{weather['name']}")
            
            #Fetch and display weather icon
            icon_url = f'http://openweathermap.org/img/wn/{weather['weather'][0]["icon"]}.png'
            icon_response = requests.get(icon_url)
            icon_image = Image.open(BytesIO(icon_response.content))
            icon_photo = ImageTk.PhotoImage(icon_image.resize((150, 150)))
            icon_label.configure(image = icon_photo)
            
        else:
            city_label.configure(text="City not found")
    else:
        city_label.configure(text="Invalid Zip Code! Please try again!")
        temp_label.configure(text="")
        desc_label.configure(text="")


# Set up CustomTkinter GUI
app = ctk.CTk()

app.title("Python Weather App")
app.geometry("250x400")

# Widgets
switch = ctk.CTkSwitch(app, text="°C")
switch.pack(padx=5, pady=5, anchor='sw')

icon_label = ctk.CTkLabel(app, text='')
icon_label.pack(padx=2)

temp_label = ctk.CTkLabel(app, text="")
temp_label.pack(pady=5)

desc_label = ctk.CTkLabel(app, text="")
desc_label.pack(pady=5)

city_label = ctk.CTkLabel(app, text="")
city_label.pack(pady=5)

zip_entry = ctk.CTkEntry(app, placeholder_text="Enter Zip Code")
zip_entry.pack(padx=10, pady=10)

search_button = ctk.CTkButton(app, text="Get Weather", command=update_weather)
search_button.pack(pady=10)

# Run the application
app.mainloop()