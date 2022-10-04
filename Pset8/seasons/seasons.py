
import sys
from datetime import datetime
import inflect

def main():
    try:
        birth = input("Input your date of birth in YYYY-mm-dd format: ")
        birth = datetime.strptime(birth, '%Y-%m-%d')
    except (TypeError, ValueError):
        sys.exit("Not a valid date format")

    print(numbers_to_text(get_minutes(birth)))


def get_minutes(birth):
    ## TODAY AT MIDNIGHT
    now = datetime.today()
    now = datetime.combine(now, datetime.min.time())

    ## DATEDIFF IN MINUTES
    minutes = round((now - birth).total_seconds() / 60)

    if minutes < 0:
        sys.exit("Are you born in the future?")

    return minutes


def numbers_to_text(minutes):
    inf = inflect.engine()
    sentence = inf.number_to_words(minutes) + ' minutes.'
    return sentence.capitalize()


if __name__ == "__main__":
    main()

