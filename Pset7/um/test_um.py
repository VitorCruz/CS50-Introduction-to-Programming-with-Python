
from um import count

def main():
    test_um1()
    test_um2()

def test_um1():
    sentence = 'Um, if I dont um, go, um... there in the room, people um, might notice the album'
    expected = 4

    try:
        assert count(sentence) == expected
    except AssertionError:
        print(f"Count number in '{sentence}' was not {expected}.")

def test_um2():
    sentence = 'Umma uma zum aum umon gum um um um1 um. um? um! um9 umz'
    expected = 5

    try:
        assert count(sentence) == expected
    except AssertionError:
        print(f"Count number in '{sentence}' was not {expected}.")

if __name__ == "__main__":
    main()