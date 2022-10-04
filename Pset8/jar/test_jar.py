
from jar import Jar

def main():
    test_deposit1()
    test_str()
    test_deposit2()
    test_withdraw()
    test_withdraw2()

def test_deposit1():

    jar = Jar()
    deposit = 8
    expected = None

    try:
        assert jar.deposit(deposit) == expected
    except AssertionError:
        print(f"Expected deposit of '{deposit}' was not {expected}.")

def test_str():

    jar = Jar()
    jar.deposit(8)
    expected = '🍪🍪🍪🍪🍪🍪🍪🍪'

    try:
        assert jar.__str__() == expected
    except AssertionError:
        print(f"Expected return of 'print' was not {expected}.")

def test_deposit2():

    jar = Jar()
    try:
        deposit = jar.deposit(800)
    except ValueError as e:
        deposit = str(e)

    expected = 'Not enough capacity for that amount of cookies'

    try:
        assert deposit == expected
    except AssertionError:
        print(f"Expected minutes of '{deposit}' was not {expected}.")

def test_withdraw():

    jar = Jar()
    try:
        withdraw = jar.withdraw(800)
    except ValueError as e:
        withdraw = str(e)

    expected = 'Not enough cookies in the jar. Maybe consider a diet?'

    try:
        assert withdraw == expected
    except AssertionError:
        print(f"Expected minutes of '{withdraw}' was not {expected}.")

def test_withdraw2():

    jar = Jar()
    jar.deposit(8)
    jar.withdraw(5)

    expected = 3

    try:
        assert jar.cookies == expected
    except AssertionError:
        print(f"Expected deposit of '{withdraw}' was not {expected}.")


if __name__ == "__main__":
    main()