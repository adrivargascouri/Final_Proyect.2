def get_zodiac_message(sign, zodiac_signs):
    for entry in zodiac_signs.get(sign, []):
        return entry.get("message", "no message avaliable")
    return "No message found for your zodiac sign."