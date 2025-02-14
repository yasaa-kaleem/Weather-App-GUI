import calendar
import weather_helper as helper
import weather_gui as gui
from datetime import datetime
from weather_icons import get_icon_per_weather_condition
from PIL import Image

# Update weather information on the GUI
def update_weather_on_click():
    in_fah = gui.unit_switch.get() == 0
    is_multi = gui.switch_multi_day.get() == 1
    zip = gui.zip_entry.get()

    if zip.isnumeric():
        location_response = helper.get_lat_lon_from_zip(zip)
        if not is_multi:
            get_one_day_weather(location_response, in_fah)
        else:
            get_multi_day_weather(location_response, in_fah)
    else:
        clear_labels_invalid()

# Get one day weather and update labels        
def get_one_day_weather(location_response, in_fah):
    weather = helper.get_one_day_response(location_response, in_fah)
    if weather:
        temp_data = int(weather['main']['temp'])
        condition_data = weather['weather'][0]['main']
        desc_data = (weather['weather'][0]['description']).capitalize()
        date_data = calendar.day_name[datetime.today().weekday()]
        city_data = weather['name']
        gui.city_label.configure(text=city_data)

        if not in_fah:
            gui.temp_label1.configure(text=f"{temp_data}°C")
        else:
            gui.temp_label1.configure(text=f"{temp_data}°F")

        gui.date_label1.configure(text=date_data)
        gui.desc_label1.configure(text=desc_data)

        # Fetch and display weather icon
        weather_icon = get_icon_per_weather_condition(condition_data)
        ctk_image = gui.ctk.CTkImage(light_image=Image.open(weather_icon),
                                                dark_image=Image.open(weather_icon),
                                                size=(100, 100))
        gui.icon_label1.configure(image=ctk_image)
        gui.icon_label2.configure(image='')
        gui.temp_label2.configure(text='')
        gui.desc_label2.configure(text='')
        gui.date_label2.configure(text='')

        gui.icon_label3.configure(image='')
        gui.temp_label3.configure(text='')
        gui.desc_label3.configure(text='')
        gui.date_label3.configure(text='')
    else:
        city_error()

# Get multi-day weather and update labels
def get_multi_day_weather(location_response, in_fah):
    weather = helper.get_multi_day_response(location_response, in_fah)
    if weather:
        date = ""
        payload_dict_list = []

        # Setting city from payload
        city_data = weather['city']['name']
        gui.city_label.configure(text=city_data)

        # Grabbing 3 days of weather data
        for i in weather['list']:
            payload_date = helper.trim_date(i['dt_txt'])
            if date != payload_date:
                if len(payload_dict_list) <= 2:
                    payload_dict_list.append(i)
                date = payload_date

        # Grabbing data from payload and setting to variables
        temp_data1 = int(payload_dict_list[0]['main']['temp'])
        condition_data1 = payload_dict_list[0]['weather'][0]['main']
        desc_data1 = (payload_dict_list[0]['weather'][0]['description']).capitalize()
        date_data1 = calendar.day_name[helper.convert_str_to_date(payload_dict_list[0]['dt_txt']).weekday()]

        temp_data2 = int(payload_dict_list[1]['main']['temp'])
        condition_data2 = payload_dict_list[1]['weather'][0]['main']
        desc_data2 = (payload_dict_list[1]['weather'][0]['description']).capitalize()
        date_data2 = calendar.day_name[helper.convert_str_to_date(payload_dict_list[1]['dt_txt']).weekday()]

        temp_data3 = int(payload_dict_list[2]['main']['temp'])
        condition_data3 = payload_dict_list[2]['weather'][0]['main']
        desc_data3 = (payload_dict_list[2]['weather'][0]['description']).capitalize()
        date_data3 = calendar.day_name[helper.convert_str_to_date(payload_dict_list[2]['dt_txt']).weekday()]

        if not in_fah:
            gui.temp_label1.configure(text=f"{temp_data1}°C")
            gui.temp_label2.configure(text=f"{temp_data2}°C")
            gui.temp_label3.configure(text=f"{temp_data3}°C")
        else:
            gui.temp_label1.configure(text=f"{temp_data1}°F")
            gui.temp_label2.configure(text=f"{temp_data2}°F")
            gui.temp_label3.configure(text=f"{temp_data3}°F")

        # Setting data to labels
        gui.date_label1.configure(text=date_data1)
        gui.desc_label1.configure(text=desc_data1)

        gui.date_label2.configure(text=date_data2)
        gui.desc_label2.configure(text=desc_data2)

        gui.date_label3.configure(text=date_data3)
        gui.desc_label3.configure(text=desc_data3)

        # Fetch weather icons
        weather_icon1 = get_icon_per_weather_condition(condition_data1)
        weather_icon2 = get_icon_per_weather_condition(condition_data2)
        weather_icon3 = get_icon_per_weather_condition(condition_data3)

        # Set weather icons
        ctk_image1 = gui.ctk.CTkImage(light_image=Image.open(weather_icon1),
                                                dark_image=Image.open(weather_icon1),
                                                size=(100, 100))
        ctk_image2 = gui.ctk.CTkImage(light_image=Image.open(weather_icon2),
                                                dark_image=Image.open(weather_icon2),
                                                size=(100, 100))
        ctk_image3 = gui.ctk.CTkImage(light_image=Image.open(weather_icon3),
                                                dark_image=Image.open(weather_icon3),
                                                size=(100, 100))

        # Display weather icons
        gui.icon_label1.configure(image=ctk_image1)
        gui.icon_label2.configure(image=ctk_image2)
        gui.icon_label3.configure(image=ctk_image3)
    else:
        city_error()

def city_error():
    gui.city_label.configure(text="City not found")

def clear_labels_invalid():
    gui.city_label.configure(text="Invalid Zip Code! Please try again!")
    gui.icon_label1.configure(image='')
    gui.temp_label1.configure(text='')
    gui.desc_label1.configure(text='')
    gui.date_label1.configure(text='')

    gui.icon_label2.configure(image='')
    gui.temp_label2.configure(text='')
    gui.desc_label2.configure(text='')
    gui.date_label2.configure(text='')

    gui.icon_label3.configure(image='')
    gui.temp_label3.configure(text='')
    gui.desc_label3.configure(text='')
    gui.date_label3.configure(text='')