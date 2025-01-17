
import json
from functions_zodiac_signs import calculate_zodiac_sign, load_zodiac_signs
from get_zodiac_message import get_zodiac_message
from get_and_check import get_and_check_days, get_and_check_months

print("Welcome to your Zodiac signs and season game")
print("")

with open ("Zodiacsigns.json", "r") as z:
    zodiac_signs = json.load(z)


def main():
    zodiac_signs = load_zodiac_signs()
    if not zodiac_signs:
        print("Error: could not load zodiac sings.")
        return
    
    while True:
        print("")
        print("Main Menu:")
        print("1. See your zodiac sign")
        print("2. See in which season of the month you were born")
        print("3. Exit")

        try:
            option = int(input("choose an option: "))

            if option == 1:
                day = get_and_check_days()
                if day is None:
                    print("Returning to main menu.")
                    continue
                month = get_and_check_months()
                if month is None:
                    print("Returning to main menu.")
                    continue
                sign = calculate_zodiac_sign(day,month)
                if sign:
                    message = get_zodiac_message(sign, zodiac_signs)
                    print(f"Your zodiac sign is {sign}. {message}")
                    
                else:
                    print("Invalid date. Please try again.")
                    print("")
                    
            elif option == 2:
                while True:
                    month = get_and_check_months()
                    if month in [12, 1, 2]:
                        print("Winter")
                        break
                    elif 3 <= month <= 5:
                        print("Spring")
                        break
                    elif 6 <= month <=8:
                        print("Summer")
                        break
                    elif 9 <= month <= 11:
                        print("Autumn")
                        break
                    else:
                        print("Invalid month. Please try again.")
                   

            elif option == 3:
                print("")
                print("Thanks for participating!")
                print("Hope to see you soon!")
                print("")
                break
            
            else:
                print("Invalid Option. Please enter a number between (1-2)")
                print("")
        
        except ValueError:
            print("Invalid Input. Please enter a number between (1-2)")
            print("")

main()

