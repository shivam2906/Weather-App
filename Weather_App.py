import tkinter as tk
import requests 
import time 
import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

# defining a function to get the data from weather api
def getWeatherInfo(window):
    # first we will get the city name from textfiled
    city = textfield.get()
    weather_api = "https://api.openweathermap.org/data/2.5/weather?q=" +city +"&appid=9a6988fb1184082e19b930ed69cec73f"
    
    timezone_api ="https://api.ipgeolocation.io/timezone?apiKey=1a8566a0112f4a7a9d2b78bc8085f974&location="+ city +""
    
    # Now timezone_api is variable of timezone json file
    timezone_json_data = requests.get(timezone_api).json()
    
    # now getting details from json file and storing into different variables 
    city_time = timezone_json_data['time_12']
    curr_date = timezone_json_data['date']
    time_zone = timezone_json_data['timezone']

    
    info_date_time = curr_date +'  '+ city_time + "\n" + "("+ time_zone +")"
    label4.config(text = info_date_time)
    
    
    # Now weather_api is variable of weather json file 
    weather_json_data = requests.get(weather_api).json()
    
   # now getting details from json file and storing into different variables 
    
    city_condition = weather_json_data['weather'][0]['main']
    temp =int(weather_json_data['main']['temp'] - 273.15)
    min_temp = int(weather_json_data['main']['temp_min'] -273.15)
    max_temp = int(weather_json_data['main']['temp_max'] -273.15)
    humidity = weather_json_data['main']['humidity']
    wind_speed =weather_json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(weather_json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(weather_json_data['sys']['sunset'] - 21600))
    
    info_celcius = str(temp) +"°C" 
    label0.config(text= info_celcius)
    
    info_condition = '"' + city_condition +'"' + "\n"
    label1.config(text = info_condition)
    
    info_temp_range = "Max Temperature: " +str(max_temp) + "°C" + "\n" + "Min Temperature: " + str(min_temp) +"°C" +"\n"+ "Humidity: " +str(humidity) +"g/m3" + "\n"+ "Wind Speed: " +str(wind_speed) +"km/h" +"\n"+ "Sunrise: " + sunrise +"\n"+ "Sunset: " + sunset +"\n"
    label5.config(text = info_temp_range)
    
    name ="@shivamProduction"
    label6.config(text=name)


window = tk.Tk()
window.geometry("450x570")

#setting background colour of window
window.configure(bg="light blue")

# title is title of python app 
window.title("Weather App")


f1 = ("poppins", 15, "bold")
f2 = ("poppins", 25, "bold")


name = tk.Label(window,text="\n"+"Enter City/State/Country", justify='center',
                font =("Candara Light", 12,'bold') ,fg="Black",bg="light blue")
name.pack(padx=5)

textfield = tk.Entry(window, justify ="center",width=18, font = f2)
textfield.pack(pady =10,padx =10)
textfield.focus()
textfield.bind('<Return>',getWeatherInfo)


label0 = tk.Label(window, font =("Copperplate Gothic Light",35,"bold"),fg="Black",bg="light blue")
label0.pack(pady=15)

label1 = tk.Label(window, font =("Copperplate Gothic Light",20,"bold"),fg="Black",bg="light blue")
label1.pack()

label5 = tk.Label(window, font =("Candara Light", 12,'bold'), fg="Black",bg="light blue")
label5.pack(anchor="center")

label4 = tk.Label(window, font =("Candara Light", 12,'bold'), fg="Black",bg="light blue")
label4.pack(anchor="center",pady=2)

label6 = tk.Label(window,font =("Candara Light", 10,'bold italic'), fg="Black",bg="light blue")
label6.pack(anchor="center",pady=2)
window.mainloop()
