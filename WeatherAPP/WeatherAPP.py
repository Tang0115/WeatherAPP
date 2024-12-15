import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
import ttkbootstrap


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")
        self.root.geometry("500x500")
        self.current_weather = None
        self.temp_unit = "C"

        self.setup_widgets()

    def setup_widgets(self):
        self.city_entry = ttkbootstrap.Entry(self.root, font="Helvetica, 18")
        self.city_entry.pack(pady=10)
        # Bind the Enter key to the search method
        self.city_entry.bind("<Return>", self.search)

        search_button = ttkbootstrap.Button(self.root, text="Search", command=self.search, bootstyle="warning")
        search_button.pack(pady=10)

        self.location_label = tk.Label(self.root, font="Helvetica, 25")
        self.location_label.pack(pady=20)

        self.icon_label = tk.Label(self.root)
        self.icon_label.pack()

        self.temperature_label = tk.Label(self.root, font="Helvetica, 20")
        self.temperature_label.pack()

        self.description_label = tk.Label(self.root, font="Helvetica, 20")
        self.description_label.pack()

        self.temp_unit_button = ttkbootstrap.Button(self.root, text="Switch to °F", command=self.toggle_temp_unit, bootstyle="info")

    def get_weather(self, city):
        API_key = "Enter API here"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
        res = requests.get(url)

        if res.status_code == 404:
            messagebox.showerror("Error", "City not found")
            return None

        weather = res.json()
        return {
            "icon_id": weather["weather"][0]["icon"],
            "temperature": weather['main']['temp'],
            "description": weather['weather'][0]['description'],
            "city": weather['name'],
            "country": weather['sys']['country']
        }

    def convert_temperature(self, temp_k, unit="C"):
        return temp_k - 273.15 if unit == "C" else (temp_k - 273.15) * 9 / 5 + 32

    def update_weather_display(self):
        if self.current_weather:
            icon_url = f"https://openweathermap.org/img/wn/{self.current_weather['icon_id']}@2x.png"
            temperature = self.convert_temperature(self.current_weather['temperature'], self.temp_unit)
            self.location_label.configure(text=f"{self.current_weather['city']}, {self.current_weather['country']}")

            image = Image.open(requests.get(icon_url, stream=True).raw)
            icon = ImageTk.PhotoImage(image)
            self.icon_label.configure(image=icon)
            self.icon_label.image = icon

            self.temperature_label.configure(text=f"Temperature: {temperature:.2f}°{self.temp_unit}")
            self.description_label.configure(text=f"Description: {self.current_weather['description']}")

            if self.temp_unit_button.winfo_manager() == "":
                self.temp_unit_button.pack(pady=5)

    def search(self, event=None):
        city = self.city_entry.get()
        weather_data = self.get_weather(city)
        if weather_data:
            self.current_weather = weather_data
            self.update_weather_display()

    def toggle_temp_unit(self):
        self.temp_unit = "F" if self.temp_unit == "C" else "C"
        self.temp_unit_button.configure(text="Switch to °C" if self.temp_unit == "F" else "Switch to °F")
        self.update_weather_display()


if __name__ == "__main__":
    root = ttkbootstrap.Window(themename="morph")
    app = WeatherApp(root)
    root.mainloop()
