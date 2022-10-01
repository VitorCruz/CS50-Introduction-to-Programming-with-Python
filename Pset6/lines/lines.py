
import sys

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif '.py' not in sys.argv[1]:
        sys.exit("Not a python file")
    else:
        path = sys.argv[1]

    print(F"Number of lines on the file = {count_lines(path)} lines.")

def count_lines(path):
    lines = []
    line_count = 0

    try:
        with open(path) as file:
            for line in file:
                lines.append(line.strip())
    except FileNotFoundError:
        sys.exit("File does not exist")

    for line in lines:
        if not line.startswith("#") and len(line) > 0:
            line_count += 1

    return line_count

if __name__ == "__main__":
    main()