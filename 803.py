import tkinter as tk

def get_weather_text(city: str) -> str | None:
    #no real api yet -- stub for now

    return f"Sunny in {city}"
def on_get_weather():
    city = entry.get().strip()
    label.config(text=get_weather_text(city))

root = tk.Tk()
root.title("Weather dashboard")
entry = tk.entry(root); entry.pack(pack=8, pack=4)
btn = tk.Button(root, text="Get weather", command=on_get_weather);btn.pack(pack=4)

label = tk.label(root, text="enter your city")
label.pack()

entry =tk.entry(root)
entry.pack()

button = tk.button(root, text="submit")
button.pack()