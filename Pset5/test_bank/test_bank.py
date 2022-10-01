
from bank2 import value

def main():
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()

def test_1():
    text = 'hellomyfriend how you doing?'
    correct_value = 0

    try:
        assert value(text) == correct_value
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct_value}'")


def test_2():
    text = '       hello my friend how you doing?'
    correct_value = 0

    try:
        assert value(text) == correct_value
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct_value}'")

def test_3():
    text = 'hell o my friend how you doing?'
    correct_value = 20

    try:
        assert value(text) == correct_value
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct_value}'")

def test_4():
    text = 'ohello my friend how you doing?'
    correct_value = 100

    try:
        assert value(text) == correct_value
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct_value}'")

def test_5():
    text = 'HElLoOOOooOOO my friend how you doing?'
    correct_value = 0

    try:
        assert value(text) == correct_value
    except AssertionError:
        print(f"Shorten of '{text}' was not '{correct_value}'")

if __name__ == "__main__":
    main()