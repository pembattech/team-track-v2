import datetime

def today_date():
    today_date = datetime.date.today()
    return today_date

def greeting():
    current_time = datetime.datetime.now()
    current_hour = current_time.hour

    if 5 <= current_hour < 12:
        result = "Good morning!"
    elif 12 <= current_hour < 17:
        result = "Good afternoon!"
    elif 17 <= current_hour < 21:
        result = "Good evening!"
    else:
        result = "Good night!"

    return result

def capitalized_string(input_string):
    capitalized_string = ' '.join(word.capitalize() for word in input_string.split())
    return capitalized_string