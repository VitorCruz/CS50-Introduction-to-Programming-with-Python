
import working
from working import convert, validade

def main():
    test_working1()
    test_working2()
    test_working3()
    test_working4()
    test_working5()

def test_working1():
    time = '9 AM to 5 PM'
    expected = '09:00 to 17:00'

    try:
        assert convert(time) == expected
    except AssertionError:
        print(f"Expected converted time of '{time}' was not {expected}.")

def test_working2():
    time = '10:30 PM to 8:50 AM'
    expected = '22:30 to 08:50'

    try:
        assert convert(time) == expected
    except AssertionError:
        print(f"Expected converted time of '{time}' was not {expected}.")

def test_working3():
    time = '09:00 AM - 17:00 PM'
    expected = 'No matches found'

    try:
        assert convert(time) == expected
    except AssertionError:
        print(f"Expected converted time of '{time}' was not {expected}.")

def test_working4():
    time = '09:68 AM to 10:00 PM'
    expected = 'Not Valid Input'

    try:
        assert convert(time) == expected
    except AssertionError:
        print(f"Expected converted time of '{time}' was not {expected}.")

def test_working5():
    time = '09:00 AM to 17:00 PM'
    expected = 'Not Valid Input'

    try:
        assert convert(time) == expected
    except AssertionError:
        print(f"Expected converted time of '{time}' was not {expected}.")

if __name__ == "__main__":
    main()