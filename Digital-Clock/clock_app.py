from customtkinter import *  # Import CustomTkinter for modern themed GUI
from datetime import datetime  # For working with current time
from tkinter.messagebox import showinfo  # For showing popup alerts

# Set the theme appearance
set_appearance_mode("dark")
set_default_color_theme("blue")

# Create main window
win = CTk()
win.geometry("500x550+700+50")  # Size and position
win.resizable(False, False)
win.title("🕒 Digital Clock")

# ----------- Clock Display -----------
frame1 = CTkFrame(win, fg_color="#1f1f2e", corner_radius=15, height=130)
frame1.pack(fill="x", pady=10, padx=10)

# Label for displaying the date
lab_date = CTkLabel(
    frame1, text="", font=("Courier New", 24, "bold"),
    text_color="#00ffff", fg_color="#33334d",
    corner_radius=10, width=250, height=70
)
lab_date.place(x=0, y=10)

# Label for displaying the time
lab_time = CTkLabel(
    frame1, text="", font=("Courier New", 36, "bold"),
    text_color="#ffffff", fg_color="#4a4a6a",
    corner_radius=10, width=250, height=70
)
lab_time.place(x=250, y=45)

# Function to update time every second
def update_label():
    day = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M:%S")
    lab_date.configure(text=day)
    lab_time.configure(text=time)
    win.after(1000, update_label)  # Call this function every 1 second

update_label()  # Start the clock

# ----------- Alarm Section -----------
frame2 = CTkFrame(win, fg_color="#4a4a6a", corner_radius=15, height=150)
frame2.pack(fill="x", pady=10, padx=10)

# Alarm input title
title1 = CTkLabel(
    frame2, text="⏰ Set Alarm (HH:MM):",
    font=("Courier New", 20, "bold"),
    text_color="#ffffff", corner_radius=10,
)
title1.place(x=0, y=10)

# Input field for alarm time
alarm_entry = CTkEntry(
    frame2, font=("Courier New", 20, "bold"),
    text_color="#ffffff", placeholder_text=("e.g. 07:30"),
    corner_radius=10, width=150
)
alarm_entry.place(x=270, y=10)

# Label for showing alarm status
alarm_status = CTkLabel(
    frame2, text="", font=("Courier New", 20, "bold"),
    text_color="#ffffff", corner_radius=10,
)
alarm_status.place(x=0, y=80)

# Variable to store the alarm time
alarm_set_time = None

# Set alarm from user input
def set_alarm():
    global alarm_set_time
    user_input = alarm_entry.get().strip()
    try:
        datetime.strptime(user_input, "%H:%M")  # Validate time format
        alarm_set_time = user_input
        alarm_status.configure(text=f"⏰ Alarm set for: {alarm_set_time}")
    except ValueError:
        alarm_status.configure(text="❌ Invalid time format (HH:MM)")

# Check every second if alarm time matches
def check_alarm():
    global alarm_set_time
    if alarm_set_time:
        current = datetime.now().strftime("%H:%M")
        if current == alarm_set_time:
            showinfo("⏰ Alarm", "Time's up!")  # Popup notification
            alarm_status.configure(text="✅ Alarm rang!")
            alarm_set_time = None  # Disable after ringing
    win.after(1000, check_alarm)  # Check every second

check_alarm()  # Start checking

# Set Alarm button
CTkButton(frame2, text="Set Alarm", command=set_alarm).place(x=275, y=50)

# Remove Alarm button
def remove_alarm():
    global alarm_set_time
    alarm_set_time = None
    alarm_status.configure(text="❌ Alarm cleared.")

CTkButton(frame2, text="Remove Alarm", command=remove_alarm).place(x=130, y=50)

# ----------- Stopwatch Section -----------
frame3 = CTkFrame(win, fg_color="#4a4a6a", corner_radius=15, height=150)
frame3.pack(fill="x")

# Initialize stopwatch variables
stopwatch_time = 0
running = False

# Stopwatch display label
stopwatch_label = CTkLabel(
    frame3, text="00:00:00", font=("Courier New", 32, "bold"),
    text_color="white"
)
stopwatch_label.place(x=150, y=20)

# Function to update stopwatch display
def update_stopwatch():
    global stopwatch_time
    if running:
        stopwatch_time += 1
        mins, secs = divmod(stopwatch_time, 60)
        hrs, mins = divmod(mins, 60)
        stopwatch_label.configure(text=f"{hrs:02}:{mins:02}:{secs:02}")
        win.after(1000, update_stopwatch)

# Start stopwatch
def start_stopwatch():
    global running
    if not running:
        running = True
        update_stopwatch()

# Stop stopwatch
def stop_stopwatch():
    global running
    running = False

# Reset stopwatch
def reset_stopwatch():
    global stopwatch_time, running
    running = False
    stopwatch_time = 0
    stopwatch_label.configure(text="00:00:00")

# Stopwatch control buttons
CTkButton(frame3, text="▶ Start", command=start_stopwatch).place(x=60, y=100)
CTkButton(frame3, text="⏸ Stop", command=stop_stopwatch).place(x=190, y=100)
CTkButton(frame3, text="🔄 Reset", command=reset_stopwatch).place(x=310, y=100)

# ----------- Footer Section -----------
frame4 = CTkFrame(win, fg_color="#4a4a6a", corner_radius=15, height=50)
frame4.pack(fill="x", pady=10, padx=10)

# Developer credit
CTkLabel(frame4, text="👨‍💻 Made by Ritik Sharma", font=("Courier New", 16), text_color="white").place(x=120, y=10)

# ----------- Run Application -----------
win.mainloop()
