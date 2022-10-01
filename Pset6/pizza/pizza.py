
import sys
import csv
from tabulate import tabulate

def main():

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif '.csv' not in sys.argv[1]:
        sys.exit("Not a csv file")
    else:
        path = sys.argv[1]

    print(tabulate_file(path))

def tabulate_file(path):
    table = []

    try:
        with open(path, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                table.append(row)
    except FileNotFoundError:
        sys.exit("File does not exist")

    return tabulate(table, tablefmt="grid")

if __name__ == "__main__":
    main()