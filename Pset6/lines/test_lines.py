
from lines import count_lines

def main():
    test_file1()
    test_file2()
    test_file3()

def test_file1():
    path = '/workspaces/14237047/indoor/indoor.py'
    correct_value = 7

    try:
        assert count_lines(path) == correct_value
    except AssertionError:
        print(f"Number of lines from '{path}' was not '{correct_value}'")

def test_file2():
    path = '/workspaces/14237047/professor/professor.py'
    correct_value = 47

    try:
        assert count_lines(path) == correct_value
    except AssertionError:
        print(f"Number of lines from '{path}' was not '{correct_value}'")

def test_file3():
    path = '/workspaces/14237047/taqueria/taqueria.py'
    correct_value = 29

    try:
        assert count_lines(path) == correct_value
    except AssertionError:
        print(f"Number of lines from '{path}' was not '{correct_value}'")

if __name__ == "__main__":
    main()