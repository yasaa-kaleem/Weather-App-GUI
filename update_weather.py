# # Update weather information on the GUI
# def update_weather():
#     in_fah = unit_switch.get() == 0
#     is_multi = switch_multi_day.get() == 1

#     zip = zip_entry.get()
#     if zip.isnumeric():
#         location_response = get_lat_lon_from_zip(zip)
#         if not is_multi:
#             weather = get_response_using_lat_lon(location_response, in_fah)
#             if weather:

#                 temp_data = int(weather['main']['temp'])
#                 desc_data = (weather['weather'][0]['description']).capitalize()
#                 date_data = calendar.day_name[datetime.today().weekday()]
#                 city_data = weather['name']
#                 city_label.configure(text=f"{city_data}")

#                 if not in_fah:
#                     temp_label1.configure(text=f"{temp_data}°C")
#                 else:
#                     temp_label1.configure(text=f"{temp_data}°F")

#                 date_label1.configure(text=date_data)
#                 desc_label1.configure(text=f"{desc_data}")
                
#                 #Fetch and display weather icon
#                 weather_icon = get_icon_per_weather_condition(desc_data)
#                 ctk_image = ctk.CTkImage(light_image=Image.open(weather_icon),
#                                          dark_image=Image.open(weather_icon),
#                                          size=(100,100))        
#                 icon_label1.configure(image=ctk_image)

#                 try:
#                     icon_label2.configure(image='')
#                 except:
#                     pass
                 
#                 temp_label2.configure(text="")
#                 desc_label2.configure(text="")
#                 date_label2.configure(text="")

#                 icon_label3.configure(image='')
#                 temp_label3.configure(text="")
#                 desc_label3.configure(text="")
#                 date_label3.configure(text="")
                
#             else:
#                 city_label.configure(text="City not found")
#         else:
#             weather = get_multi_day_response(location_response, in_fah)
#             if weather:
#                 date = ""
#                 payload_dict_list = []

#                 city_data = weather['city']['name']
#                 city_label.configure(text=f"{city_data}")

#                 for i in weather['list']:
#                     payload_date = trim_date(i['dt_txt'])
#                     if date != payload_date:
#                         if len(payload_dict_list) <= 2:
#                             payload_dict_list.append(i)
#                         date = payload_date

#                 temp_data1 = int(payload_dict_list[0]['main']['temp'])
#                 desc_data1 = (payload_dict_list[0]['weather'][0]['description']).capitalize()
#                 date_data1 = calendar.day_name[convert_str_to_date(payload_dict_list[0]['dt_txt']).weekday()]
                
#                 temp_data2 = int(payload_dict_list[1]['main']['temp'])
#                 desc_data2 = (payload_dict_list[1]['weather'][0]['description']).capitalize()
#                 date_data2 = calendar.day_name[convert_str_to_date(payload_dict_list[1]['dt_txt']).weekday()]

#                 temp_data3 = int(payload_dict_list[2]['main']['temp'])
#                 desc_data3 = (payload_dict_list[2]['weather'][0]['description']).capitalize()
#                 date_data3 = calendar.day_name[convert_str_to_date(payload_dict_list[2]['dt_txt']).weekday()]

#                 if not in_fah:
#                     temp_label1.configure(text=f"{temp_data1}°C")
#                     temp_label2.configure(text=f"{temp_data2}°C")
#                     temp_label3.configure(text=f"{temp_data3}°C")
#                 else:
#                     temp_label1.configure(text=f"{temp_data1}°F")
#                     temp_label2.configure(text=f"{temp_data2}°F")
#                     temp_label3.configure(text=f"{temp_data3}°F")

#                 date_label1.configure(text=date_data1)
#                 desc_label1.configure(text=f"{desc_data1}")
#                 date_label2.configure(text=date_data2)
#                 desc_label2.configure(text=f"{desc_data2}")
#                 date_label3.configure(text=date_data3)
#                 desc_label3.configure(text=f"{desc_data3}")
                
                
#                 #Fetch and display weather icon
#                 weather_icon1 = get_icon_per_weather_condition(desc_data1)
#                 weather_icon2 = get_icon_per_weather_condition(desc_data2)
#                 weather_icon3 = get_icon_per_weather_condition(desc_data3)
                
#                 ctk_image1 = ctk.CTkImage(light_image=Image.open(weather_icon1),
#                                          dark_image=Image.open(weather_icon1),
#                                          size=(100,100))        
#                 ctk_image2 = ctk.CTkImage(light_image=Image.open(weather_icon2),
#                                          dark_image=Image.open(weather_icon2),
#                                          size=(100,100))        
#                 ctk_image3 = ctk.CTkImage(light_image=Image.open(weather_icon3),
#                                          dark_image=Image.open(weather_icon3),
#                                          size=(100,100))        
#                 icon_label1.configure(image=ctk_image1)
#                 icon_label2.configure(image=ctk_image2)
#                 icon_label3.configure(image=ctk_image3)
                
#             else:
#                 city_label.configure(text="City not found")
#     else:
#         city_label.configure(text="Invalid Zip Code! Please try again!")
#         icon_label1.configure(image='')
#         temp_label1.configure(text="")
#         desc_label1.configure(text="")
#         date_label1.configure(text="")

#         icon_label2.configure(image='')  
#         temp_label2.configure(text="")
#         desc_label2.configure(text="")
#         date_label2.configure(text="")

#         icon_label3.configure(image='')
#         temp_label3.configure(text="")
#         desc_label3.configure(text="")
#         date_label3.configure(text="")
