
import sys
import csv

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif '.csv' not in sys.argv[1]:
        sys.exit("Input is not a csv file")
    elif '.csv' not in sys.argv[2]:
        sys.exit("Output is not a csv file")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

    data = read_file(input_path)
    write_file(data, output_path)

def read_file(path):
    data = []

    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_dict = {}
            new_dict["Last"], new_dict["First"] = row["name"].split(",")
            new_dict["House"] = row["house"]
            data.append(new_dict)

    return data

def write_file(data, path):
    with open(path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=["First","Last","House"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)

if __name__ == "__main__":
    main()