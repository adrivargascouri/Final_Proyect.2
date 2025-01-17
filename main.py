
import json
import tkinter as tk 
from tkinter import messagebox
from PIL import Image, ImageTk
from functions_zodiac_signs import calculate_zodiac_sign, load_zodiac_signs
from get_zodiac_message import get_zodiac_message
from get_and_check import get_and_check_days, get_and_check_months

def load_data():
    with open ("Zodiacsigns.json", "r") as z:
        return json.load(z)
    
def show_zodiac_sign(result_label,entry_day,entry_month,zodiac_signs):
    try:
        day_input = entry_day.get()

        month_input = entry_month.get()

        print(f"Day input: {day_input}, Month input: {month_input}")

        day = get_and_check_days(day_input) 
        month = get_and_check_months(month_input)

        if day is None or month is None:
            messagebox.showerror("Error", "Please, insert a valid date")
            return
        
        sign = calculate_zodiac_sign(day, month)


        zodiac_signs = load_zodiac_signs()
        
        if sign:
            message = get_zodiac_message(sign,zodiac_signs)
            result_label.config(text = f"Your zodiac sign is {sign}, {message}")
        
        else:
            messagebox.showerror("Error", "Invalid date. Please, Try again")
    except ValueError:
        messagebox.showerror("Error", "Please, insert a valid date")


def show_season(result_label, entry_month):
    try:
        month = get_and_check_months(entry_month.get())
        if month is None:
            messagebox.showerror("Error", "Invalid month. Please, insert a number between 1 and 12.")
            return
        
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


def main():
    
    global zodiac_signs
    zodiac_signs = load_data()

    window = tk.Tk()
    window.title("ZODIAC AND SEASON GAME")
    window.geometry("400x500")

    img = Image.open("photo.png")
    img = img.resize((400, 500), Image.Resampling.LANCZOS)  # Redimensionar la imagen para ajustarla al tamaño de la ventana
    photo = ImageTk.PhotoImage(img)

    bg_image = tk.Label(window, image=photo)
    bg_image.image = photo  # Guardar una referencia a la imagen
    bg_image.place(relwidth=1, relheight=1)

    frame = tk.Frame(window, bg= "white")
    frame.place(relx=0.5, rely=0.5, anchor= "center")


    text_label=tk.Label (frame, text="Welcome to your zodiac and season game", font= 20)
    text_label.pack(pady=5)


    label_day = tk.Label(frame, text="Day of Birth (1-31):", font=("Arial", 12))
    label_day.pack(pady=4)

    entry_day = tk.Entry(frame)
    entry_day.pack(pady=5)

    label_month = tk.Label(frame, text= "Month of Birth (1-12):", font=("Arial", 12))
    label_month.pack(pady=5)

    entry_month = tk.Entry(frame)
    entry_month.pack(pady=5)

    result_label = tk.Label(frame, text="", font=("Arial", 12), bg="white")
    result_label.pack(pady=10)


    button_zodiac = tk.Button(frame, text="See your zodiac sign", command=lambda: show_zodiac_sign(result_label,entry_day,entry_month,zodiac_signs))
    button_zodiac.pack(pady=10)

    button_season = tk.Button(frame, text="See your season of the year ", command=lambda:show_season(result_label, entry_month))
    button_season.pack(pady=20)

    button_exit = tk.Button(frame, text="Exit", command=window.quit)
    button_exit.pack(pady=40)

    window.mainloop()

if __name__ == "__main__":
    main()
