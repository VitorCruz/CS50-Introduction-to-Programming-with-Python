
def main():
    user_input = input("What time is it? ")
    user_input = user_input.split(":")
    hour = convert(list(user_input))
    mealtime = meal_time(hour)

    if mealtime != None:
        print(mealtime)

def convert(time):
    hours = float(time[0])

    try:
        minutes = float(time[1]) / 60
    except IndexError:
        minutes = 0
        
    both = hours + minutes
    return both

def meal_time(hour):
    if hour >= 7 and hour <= 8:
        return 'breakfast time'
    elif hour >= 12 and hour <= 13:
        return 'lunch time'
    elif hour >= 18 and hour <= 19:
        return 'dinner time'

def convert_at_once(time):
    if time[0] == '7' or (time[0] == '8' and time[1] == '00'):
        return 'breakfast time'
    elif time[0] == '12' or (time[0] == '13' and time[1] == '00'):
        return 'lunch time'
    elif time[0] == '18' or (time[0] == '19' and time[1] == '00'):
        return 'dinner time'

if __name__ == "__main__":
    main()