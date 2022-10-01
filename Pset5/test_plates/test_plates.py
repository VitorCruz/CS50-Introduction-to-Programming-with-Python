
from plates import is_valid

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()

def test_1():
    plate = 'AOUIO3'
    correct_value = True

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_2():
    plate = 'AO4IO3'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")


def test_3():
    plate = 'AOUI'
    correct_value = True

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_4():
    plate = '44AOUI'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_5():
    plate = '44-OUI'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_6():
    plate = 'CER098'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_7():
    plate = 'CERVO0'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_8():
    plate = 'CE3498'
    correct_value = True

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

def test_9():
    plate = 'CE 498'
    correct_value = False

    try:
        assert is_valid(plate) == correct_value
    except AssertionError:
        print(f"Shorten of '{plate}' was not '{correct_value}'")

if __name__ == "__main__":
    main()

