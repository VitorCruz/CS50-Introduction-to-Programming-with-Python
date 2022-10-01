
from fuel import calculate, gauge

def main():
    test_calculate1()
    test_calculate2()
    test_calculate3()
    test_gauge1()
    test_gauge2()
    test_gauge3()

def test_calculate1():
    fraction = '1/16'
    correct_value = 6

    try:
        assert calculate(fraction) == correct_value
    except AssertionError:
        print(f"Shorten of '{fraction}' was not '{correct_value}'")

def test_calculate2():
    fraction = '1/1000'
    correct_value = 0

    try:
        assert calculate(fraction) == correct_value
    except AssertionError:
        print(f"Shorten of '{fraction}' was not '{correct_value}'")

def test_calculate3():
    fraction = '1/12'
    correct_value = 8

    try:
        assert calculate(fraction) == correct_value
    except AssertionError:
        print(f"Shorten of '{fraction}' was not '{correct_value}'")

def test_gauge1():
    percentage = 1
    correct_value = 'E'

    try:
        assert gauge(percentage) == correct_value
    except AssertionError:
        print(f"Shorten of '{percentage}' was not '{correct_value}'")

def test_gauge2():
    percentage = 100
    correct_value = 'F'

    try:
        assert gauge(percentage) == correct_value
    except AssertionError:
        print(f"Shorten of '{percentage}' was not '{correct_value}'")

def test_gauge3():
    percentage = 50
    correct_value = '50%'

    try:
        assert gauge(percentage) == correct_value
    except AssertionError:
        print(f"Shorten of '{percentage}' was not '{correct_value}'")

if __name__ == "__main__":
    main()
