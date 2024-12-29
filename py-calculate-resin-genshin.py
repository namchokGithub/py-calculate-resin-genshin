import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk
import pytz
import os
import sys

def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def calculate_resin():
    try:
        current_resin = int(resin_entry.get())
        if 0 <= current_resin <= 200:
            now = datetime.now()
            resin_to_full = 200 - current_resin
            minutes_to_full = resin_to_full * 8  # Each resin takes 8 minutes to regenerate
            full_time = now+ timedelta(minutes=minutes_to_full)

            hours, remainder = divmod(minutes_to_full, 60)
            minutes, seconds = divmod(remainder * 60, 60)

            is_next_day = now.date() != full_time.date()
            next_day_text = " (TMR)" if is_next_day else " (TODAY)"

            time_label.config(text=f"Full refill in: {hours}h {minutes}m {seconds}s")
            at_label.config(text=f"Full refill at: {full_time.strftime('%I:%M %p')} {next_day_text}", fg="blue" if is_next_day else "green")
        else:
            time_label.config(text="Invalid resin number (0-200).", fg="red")
            at_label.config(text="")
    except ValueError:
        time_label.config(text="Please enter a valid number.", fg="red")
        at_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Genshin Impact Resin Timer")

icon_path = resource_path("assets/paimon.png")
icon = tk.PhotoImage(file=icon_path)
root.iconphoto(False, icon)

logo_path = resource_path("assets/logo.png")
original_logo = Image.open(logo_path)
resized_logo = original_logo.resize((300, 100))
logo = ImageTk.PhotoImage(resized_logo)

# Display the logo
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=(10, 5))

# Input section
resin_label = tk.Label(root, text="Current Resin (0 - 200)", font=("Arial", 12))
resin_label.pack(pady=5)

resin_entry = tk.Entry(root, font=("Arial", 14), width=10, justify="center")
resin_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate", font=("Arial", 12), command=calculate_resin)
calculate_button.pack(pady=10)

# Function to update current time
def update_time():
    bangkok_timezone = pytz.timezone("Asia/Bangkok")
    current_time = datetime.now(bangkok_timezone).strftime("%H:%M:%S")
    current_time_label.config(text=f"{current_time} (Bangkok)")
    root.after(1000, update_time)
current_time_label = tk.Label(root, text="Current Time:", font=("Arial", 12))
current_time_label.pack(pady=10)
update_time()

# Output section
time_label = tk.Label(root, text="Full refill in: 00h 00m 00s", font=("Arial", 12), justify="center")
time_label.pack(pady=10)

at_label = tk.Label(root, text="Full refill at: 00:00 AM", font=("Arial", 12), justify="center")
at_label.pack(pady=10)

# Button to close the app
close_button = tk.Button(
    root,
    text="Close",
    command=root.quit,
    bg="#ffcad4",
    fg="black",
    font=("Arial", 10),
    relief="raised",
    bd=1,
    padx=10,
    pady=5
)
close_button.pack(pady=10)

tk.Label(root, text="v0.0.1", font=("Arial", 7), fg="black").pack(pady=10)

# Run the app
# root.geometry("500x300")
root.mainloop()

