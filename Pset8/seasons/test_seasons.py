
from datetime import datetime
from seasons import get_minutes, numbers_to_text

def main():
    test_minutes()
    test_speech()


def test_minutes():
    date = datetime.strptime('2022-09-01', '%Y-%m-%d')
    expected = 46080

    try:
        assert get_minutes(date) == expected
    except AssertionError:
        print(f"Expected minutes of '{date}' was not {expected}.")


def test_speech():
    minutes = '1820960'
    expected = 'One million, eight hundred and twenty thousand, nine hundred and sixty minutes.'

    try:
        assert numbers_to_text(minutes) == expected
    except AssertionError:
        print(f"Expected minutes of '{minutes}' was not {expected}.")

if __name__ == "__main__":
    main()