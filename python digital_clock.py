import tkinter as tk
import time

# Function to update the clock
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    root.after(1000, update_clock)

# Creating the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x200")
root.configure(bg="#282c34")

# Configuring the clock label
clock_label = tk.Label(
    root, 
    font=("Helvetica", 48, "bold"), 
    bg="#282c34", 
    fg="#61dafb",
    padx=10,
    pady=10
)
clock_label.pack(expand=True)

# Adding some decorative elements
left_frame = tk.Frame(root, bg="#61dafb", width=10)
left_frame.pack(side="left", fill="y")

right_frame = tk.Frame(root, bg="#61dafb", width=10)
right_frame.pack(side="right", fill="y")

top_frame = tk.Frame(root, bg="#61dafb", height=10)
top_frame.pack(side="top", fill="x")

bottom_frame = tk.Frame(root, bg="#61dafb", height=10)
bottom_frame.pack(side="bottom", fill="x")

# Start the clock
update_clock()

# Run the application
root.mainloop()

