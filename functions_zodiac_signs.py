import json


def load_zodiac_signs(file="Zodiacsigns.json"):
    try:
        with open(file, "r", encoding= "utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: Zodiac signs file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return {}


def calculate_zodiac_sign(day, month):

    sign_position = 0

    if (day >= 21 and month == 3) or (day <= 19 and month == 4):
        return "Aries"
       
    elif (day >= 20 and month == 4) or (day <= 20 and month == 5):
        return "Taurus"
    
    elif (day >= 21 and month == 5) or (day <= 20 and month == 6):
        return "Gemini"
        
    elif (day >= 21 and month == 6) or (day <= 22 and month == 7):
        return "Cancer"
        
    elif (day >= 23 and month == 7) or (day <= 22 and month == 8):
        return "Leo"
        
    elif (day >= 23 and month == 8) or (day <= 22 and month == 9):
        return "Virgo"
        
    elif (day >= 23 and month == 9) or (day <= 22 and month == 10):
        return "Libra"
        
    elif (day >= 23 and month == 10) or (day <= 21 and month == 11):
        return "Scorpio"
        
    elif (day >= 22 and month == 11) or (day <= 21 and month == 12):
        return "Sagittarius"
        
    elif (day >= 22 and month == 12) or (day <= 19 and month == 1):
        return "Capricorn"
    
    elif (day >= 20 and month == 1) or (day <= 18 and month == 2):
        return "Aquarious"
    
    elif (day >= 19 and month == 2) or (day <= 20 and month == 3):
        return "Pisces"
    
    else:
        return None