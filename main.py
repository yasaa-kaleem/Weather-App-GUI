import svglib.utils
from get_location_api import get_location_response
from weather_api import get_weather_response
from multi_day_weather_api import get_multi_day_weather_response
from io import BytesIO
import customtkinter as ctk
import requests
from PIL import Image, ImageTk
import tksvg
import pywinstyles
from datetime import datetime
import calendar
from weather_icons import get_icon_per_weather_condition

bg_image = 'images/clear-day.svg'

def get_lat_lon_from_zip(zip):
    location_dict = get_location_response(zip)
    return location_dict

def get_response_using_lat_lon(location_dict, in_fahrenheit):
    lat = location_dict['lat']
    lon = location_dict['lon']
    if in_fahrenheit:
        lat_lon_response = get_weather_response(lat, lon,"imperial")
    else:
        lat_lon_response = get_weather_response(lat, lon,"metric")
    print(lat_lon_response)
    return lat_lon_response

def get_multi_day_response(location_dict, in_fahrenheit):
    lat = location_dict['lat']
    lon = location_dict['lon']
    if in_fahrenheit:
        lat_lon_response = get_multi_day_weather_response(lat, lon, "24", "imperial")
    else:
        lat_lon_response = get_multi_day_weather_response(lat, lon, "24", "metric")

    print(lat_lon_response)
    return lat_lon_response


# Update weather information on the GUI
def update_weather():
    in_fah = unit_switch.get() == 0
    is_multi = switch_multi_day.get() == 1

    zip = zip_entry.get()
    if zip.isnumeric():
        location_response = get_lat_lon_from_zip(zip)
        if not is_multi:
            weather = get_response_using_lat_lon(location_response, in_fah)
            if weather:

                temp_data = int(weather['main']['temp'])
                desc_data = (weather['weather'][0]['description']).capitalize()
                date_data = calendar.day_name[datetime.today().weekday()]
                city_data = weather['name']
                city_label.configure(text=f"{city_data}")

                if not in_fah:
                    temp_label1.configure(text=f"{temp_data}°C")
                else:
                    temp_label1.configure(text=f"{temp_data}°F")

                date_label1.configure(text=date_data)
                desc_label1.configure(text=f"{desc_data}")
                
                #Fetch and display weather icon
                svg_image = tksvg.SvgImage(file=bg_image, scale=2)        
                icon_label1.configure(image=svg_image)

                icon_label2.configure(image='')  
                temp_label2.configure(text="")
                desc_label2.configure(text="")
                date_label2.configure(text="")

                icon_label3.configure(image='')
                temp_label3.configure(text="")
                desc_label3.configure(text="")
                date_label3.configure(text="")
                
            else:
                city_label.configure(text="City not found")
        else:
            weather = get_multi_day_response(location_response, in_fah)
            if weather:
                date = ""
                payload_dict_list = []

                city_data = weather['city']['name']
                city_label.configure(text=f"{city_data}")

                for i in weather['list']:
                    payload_date = trim_date(i['dt_txt'])
                    if date != payload_date:
                        if len(payload_dict_list) <= 2:
                            payload_dict_list.append(i)
                        date = payload_date

                temp_data1 = int(payload_dict_list[0]['main']['temp'])
                desc_data1 = (payload_dict_list[0]['weather'][0]['description']).capitalize()
                date_data1 = calendar.day_name[convert_str_to_date(payload_dict_list[0]['dt_txt']).weekday()]
                
                temp_data2 = int(payload_dict_list[1]['main']['temp'])
                desc_data2 = (payload_dict_list[1]['weather'][0]['description']).capitalize()
                date_data2 = calendar.day_name[convert_str_to_date(payload_dict_list[1]['dt_txt']).weekday()]

                temp_data3 = int(payload_dict_list[2]['main']['temp'])
                desc_data3 = (payload_dict_list[2]['weather'][0]['description']).capitalize()
                date_data3 = calendar.day_name[convert_str_to_date(payload_dict_list[2]['dt_txt']).weekday()]

                if not in_fah:
                    temp_label1.configure(text=f"{temp_data1}°C")
                    temp_label2.configure(text=f"{temp_data2}°C")
                    temp_label3.configure(text=f"{temp_data3}°C")
                else:
                    temp_label1.configure(text=f"{temp_data1}°F")
                    temp_label2.configure(text=f"{temp_data2}°F")
                    temp_label3.configure(text=f"{temp_data3}°F")

                date_label1.configure(text=date_data1)
                desc_label1.configure(text=f"{desc_data1}")
                date_label2.configure(text=date_data2)
                desc_label2.configure(text=f"{desc_data2}")
                date_label3.configure(text=date_data3)
                desc_label3.configure(text=f"{desc_data3}")
                
                
                #Fetch and display weather icon
                svg_image = tksvg.SvgImage(file=bg_image, scale=2)        
                icon_label1.configure(image=svg_image)
                icon_label2.configure(image=svg_image)
                icon_label3.configure(image=svg_image)
                
            else:
                city_label.configure(text="City not found")
    else:
        city_label.configure(text="Invalid Zip Code! Please try again!")
        icon_label1.configure(image='')
        temp_label1.configure(text="")
        desc_label1.configure(text="")
        date_label1.configure(text="")

        icon_label2.configure(image='')  
        temp_label2.configure(text="")
        desc_label2.configure(text="")
        date_label2.configure(text="")

        icon_label3.configure(image='')
        temp_label3.configure(text="")
        desc_label3.configure(text="")
        date_label3.configure(text="")


# Set up CustomTkinter GUI
app = ctk.CTk()

app.title("Weather App GUI")
app.geometry("500x780")
app.resizable(False, False)

# Widgets
bg_label = ctk.CTkLabel(app, text="", image=tksvg.SvgImage(file=bg_image, scale=20), bg_color="#000001")
bg_label.place(x=0, y=0)
pywinstyles.set_opacity(bg_label, value=0.05)

unit_switch = ctk.CTkSwitch(app, text="°C", bg_color="#000001")
unit_switch.pack(padx=5, pady=5, anchor='sw')
pywinstyles.set_opacity(unit_switch, color="#000001")

zip_entry = ctk.CTkEntry(app, placeholder_text="Enter Zip Code", bg_color="#000001")
zip_entry.pack(padx=10, pady=10)
pywinstyles.set_opacity(zip_entry, color="#000001")

search_button = ctk.CTkButton(app, text="Get Weather", command=update_weather, bg_color="#000001")
search_button.pack(pady=10)
pywinstyles.set_opacity(search_button, color="#000001")

switch_multi_day = ctk.CTkSwitch(app, text="Multi-Day", bg_color="#000001")
switch_multi_day.pack(padx=5, pady=5)
pywinstyles.set_opacity(switch_multi_day, color="#000001")

city_label = ctk.CTkLabel(app, text="", bg_color="#000001")
city_label.pack(pady=2)
pywinstyles.set_opacity(city_label, color="#000001")

#Day1
icon_label1 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label1.pack(padx=2)
pywinstyles.set_opacity(icon_label1, color="#000001")

date_label1 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label1.pack(padx=2)
pywinstyles.set_opacity(date_label1, color="#000001")

temp_label1 = ctk.CTkLabel(app, text="", bg_color="#000001")
temp_label1.pack(pady=1)
pywinstyles.set_opacity(temp_label1, color="#000001")

desc_label1 = ctk.CTkLabel(app, text="", bg_color="#000001")
desc_label1.pack(pady=1)
pywinstyles.set_opacity(desc_label1, color="#000001")

#Day2
icon_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label2.pack(padx=2)
pywinstyles.set_opacity(icon_label2, color="#000001")

date_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label2.pack(padx=2)
pywinstyles.set_opacity(date_label2, color="#000001")

temp_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
temp_label2.pack(pady=1)
pywinstyles.set_opacity(temp_label2, color="#000001")

desc_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
desc_label2.pack(pady=1)
pywinstyles.set_opacity(desc_label2, color="#000001")

#Day3
icon_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label3.pack(padx=2)
pywinstyles.set_opacity(icon_label3, color="#000001")

date_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label3.pack(padx=2)
pywinstyles.set_opacity(date_label3, color="#000001")

temp_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
temp_label3.pack(pady=1)
pywinstyles.set_opacity(temp_label3, color="#000001")

desc_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
desc_label3.pack(pady=1)
pywinstyles.set_opacity(desc_label3, color="#000001")

def convert_str_to_date(str_date):
    date_time_obj = datetime.strptime(str_date, '%Y-%m-%d %H:%M:%S')
    return date_time_obj

def trim_date(date_in_payload):
    date_time_obj = convert_str_to_date(date_in_payload)
    date_str = date_time_obj.strftime('%Y-%m-%d')
    return date_str

# Run the application
app.mainloop()