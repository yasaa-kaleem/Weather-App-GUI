import customtkinter as ctk
import pywinstyles as pyws
from update_weather import update_weather_on_click
from PIL import Image

# Generating CustomTKinter app
app = ctk.CTk()
app.title("Weather App GUI")
app.geometry("500x780")
app.resizable(False, False)

# Backgound image
bg_image = ctk.CTkImage(light_image=Image.open('images/clear-day.png'),
                        dark_image=Image.open('images/clear-day.png'),
                        size=(1024, 1024))

# Widgets
bg_label = ctk.CTkLabel(app, text="", image=bg_image, bg_color="#000001")
bg_label.place(x=0, y=0)
pyws.set_opacity(bg_label, value=0.05)

# Temperature Unit toggle
unit_switch = ctk.CTkSwitch(app, text="°C", bg_color="#000001")
unit_switch.pack(padx=5, pady=5, anchor='sw')
pyws.set_opacity(unit_switch, color="#000001")

# User input text field for zipcode
zip_entry = ctk.CTkEntry(app, placeholder_text="Enter Zip Code", bg_color="#000001")
zip_entry.pack(padx=10, pady=10)
pyws.set_opacity(zip_entry, color="#000001")

# get/ request weather button
get_weather_button = ctk.CTkButton(app, text="Get Weather", command=update_weather_on_click, bg_color="#000001")
get_weather_button.pack(pady=10)
pyws.set_opacity(get_weather_button, color="#000001")

# multi-day switch toggle
switch_multi_day = ctk.CTkSwitch(app, text="Multi-Day", bg_color="#000001")
switch_multi_day.pack(padx=5, pady=5)
pyws.set_opacity(switch_multi_day, color="#000001")

# city label
city_label = ctk.CTkLabel(app, text="", bg_color="#000001")
city_label.pack(pady=2)
pyws.set_opacity(city_label, color="#000001")

# Day 1 labels
icon_label1 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label1.pack(padx=2)
pyws.set_opacity(icon_label1, color="#000001")

date_label1 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label1.pack(padx=2)
pyws.set_opacity(date_label1, color="#000001")

temp_label1 = ctk.CTkLabel(app, text="", bg_color="#000001")
temp_label1.pack(pady=1)
pyws.set_opacity(temp_label1, color="#000001")

desc_label1 = ctk.CTkLabel(app, text="", bg_color="#000001")
desc_label1.pack(pady=1)
pyws.set_opacity(desc_label1, color="#000001")

# Day 2 labels
icon_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label2.pack(padx=2)
pyws.set_opacity(icon_label2, color="#000001")

date_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label2.pack(padx=2)
pyws.set_opacity(date_label2, color="#000001")

temp_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
temp_label2.pack(pady=1)
pyws.set_opacity(temp_label2, color="#000001")

desc_label2 = ctk.CTkLabel(app, text='', bg_color="#000001")
desc_label2.pack(pady=1)
pyws.set_opacity(desc_label2, color="#000001")

# Day 3 labels
icon_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
icon_label3.pack(padx=2)
pyws.set_opacity(icon_label3, color="#000001")

date_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
date_label3.pack(padx=2)
pyws.set_opacity(date_label3, color="#000001")

temp_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
temp_label3.pack(pady=1)
pyws.set_opacity(temp_label3, color="#000001")

desc_label3 = ctk.CTkLabel(app, text='', bg_color="#000001")
desc_label3.pack(pady=1)
pyws.set_opacity(desc_label3, color="#000001")