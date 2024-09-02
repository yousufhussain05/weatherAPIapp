import requests  # Import the requests library to make HTTP requests
import tkinter as tk  # Import tkinter library for creating GUI applications so there is a pop-up window

def get_weather():
    city = city_entry.get()  # Get the city name entered by the user in the input field
    api_key = 'c9e720f521c5734c911a974a5eee34b7'  # Unique API key to access the weather service
    # Make a request to the weather API, asking for data about the entered city
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}").json()

    if weather_data.get('cod') == 200:  # Check if the API successfully found the city (code 200 = works)
        weather = weather_data['weather'][0]['main']  # Get the main weather conditions
        temp = round(weather_data['main']['temp'])  # Get the temperature and round it to the nearest whole number
        # Update the result label in the GUI to show the weather and temperature
        result_label.config(text=f"Weather: {weather}\nTemperature: {temp}ºF")
    else:  # If the city wasn't found
        result_label.config(text="City not found")  # Update the label to inform the user the city wasn't found

def show_text():
    bottom_label.config(text = "The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career.\n From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations.")

# Create the main window for the application
root = tk.Tk()
root.title("Weather App")  # Set the window title to "Weather App"

# Create the input field where the user will type the city name
city_entry = tk.Entry(root)
city_entry.pack()  # Add the input field to the window

# Create the button that will trigger the weather search
get_weather_button = tk.Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack()  # Add the button to the window

# Create a label to display the weather results
result_label = tk.Label(root, text="")
result_label.pack()  # Add the label to the window

# Create labe but don't show the text yet
bottom_label = tk.Label(root, text="", font=("Arial", 10))
bottom_label.pack(side="bottom")  # Pack this label at the bottom of the window)

show_text_button = tk.Button(root, text="Show Info", command=show_text)
show_text_button.pack()  # Add the button to the window

# Start the application's main event loop
root.mainloop()
