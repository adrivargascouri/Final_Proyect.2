
import json
import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
from functions_zodiac_signs import calculate_zodiac_sign, load_zodiac_signs
from get_zodiac_message import get_zodiac_message
from get_and_check import get_and_check_days, get_and_check_months

#Function to load the zodiac sign data from JSON file

def load_data():
    with open ("Zodiacsigns.json", "r") as z:
        return json.load(z)

#Function to show the user's zodiac sign based on their birthdate
    
def show_zodiac_sign(result_label,entry_day,entry_month,zodiac_signs):
    try:
        #Get the day and month input by the user

        day_input = entry_day.get()

        month_input = entry_month.get()

        # Print the day and month input (for debugging purposes)
        print(f"Day input: {day_input}, Month input: {month_input}")
        
        #Validate the input day and month
        day = get_and_check_days(day_input) 
        month = get_and_check_months(month_input)
        
        # Check if the inputs are valid
        if day is None or month is None:
            messagebox.showerror("Error", "Please, insert a valid date")
            return

        #Calculate the zodiac signs data 
        sign = calculate_zodiac_sign(day, month)

        # Load the zodiac signs data
        zodiac_signs = load_zodiac_signs()
        
        # If the zodiac sign is found, display the message; otherwise, show an error
        if sign:
            message = get_zodiac_message(sign,zodiac_signs)
            result_label.config(text = f"Your zodiac sign is {sign}, {message}")
        
        else:
            messagebox.showerror("Error", "Invalid date. Please, Try again")
    except ValueError:
        messagebox.showerror("Error", "Please, insert a valid date")

# Function to show the user's season based on their birth month

def show_season(result_label, entry_month):
    try:
        #Get the month input by the user and validate it 
        month = get_and_check_months(entry_month.get())
        if month is None:
            messagebox.showerror("Error", "Invalid month. Please, insert a number between 1 and 12.")
            return

        #Determine the season based on the month and display the result
        if month in [12, 1, 2]:
            result_label.config(text="Season: Winter")
        elif 3 <= month <= 5:
            result_label.config(text="Season: Spring")
        elif 6 <= month <= 8:
            result_label.config(text="Season: Summer")
        elif 9 <= month <= 11:
            result_label.config(text="Season: Autumn")
        
    except ValueError:
        messagebox.showerror("Error", "Please, Insert a valid month")

# Main function that sets up the graphical user interface (GUI)
def main():
    
    global zodiac_signs
    # Load zodiac signs data
    zodiac_signs = load_data()

    # Create the main window for the game 
    window = tk.Tk()
    window.title("ZODIAC AND SEASON GAME")
    window.geometry("400x500")
    
    # Load and resize the background image 
    img = Image.open("photo.png")
    img = img.resize((1100, 1200), Image.Resampling.LANCZOS)  
    photo = ImageTk.PhotoImage(img)
    
    # Set the background image of the window 
    bg_image = tk.Label(window, image=photo)
    bg_image.image = photo  
    bg_image.place(relwidth=1, relheight=1)
    
    # Create a frame for widgets (buttons, labels, entry fields)
    frame = tk.Frame(window, bg= "white")
    frame.place(relx=0.5, rely=0.5, anchor= "center")

    # Display a welcome text label
    text_label=tk.Label (frame, text="Welcome to your zodiac and season game", font= 20)
    text_label.pack(pady=5)

    # Create a label and entry field for day of birth
    label_day = tk.Label(frame, text="Day of Birth (1-31):", font=("Arial", 12))
    label_day.pack(pady=5)
    entry_day = tk.Entry(frame)
    entry_day.pack(pady=5)
    
    # Create label and entry field for month of birth
    label_month = tk.Label(frame, text= "Month of Birth (1-12):", font=("Arial", 12))
    label_month.pack(pady=5)
    entry_month = tk.Entry(frame)
    entry_month.pack(pady=5)

    #Label to display the result (zodiac sign or season)
    result_label = tk.Label(frame, text="", font=("Arial", 12), bg="#D6C8FC")
    result_label.pack(pady=10)

    # Button to show the zodiac sign based on user's input
    button_zodiac = tk.Button(frame, text="See your zodiac sign", command=lambda: show_zodiac_sign(result_label,entry_day,entry_month,zodiac_signs))
    button_zodiac.pack(pady=10)
    
    # Button to show the season of the year based on the user's birth month
    button_season = tk.Button(frame, text="See your season of the year ", command=lambda:show_season(result_label, entry_month))
    button_season.pack(pady=20)

    # Button to exit the game
    button_exit = tk.Button(frame, text="Exit", command=window.quit)
    button_exit.pack(pady=40)

    # Start the Tkinter main loop
    window.mainloop()

# Entry point of the program
if __name__ == "__main__":
    main()
