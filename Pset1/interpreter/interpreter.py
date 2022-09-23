
import sys

def main():
    user_input = input("Input a math operation: ").strip()
    user_input_list = user_input.split()
    print(calculator(user_input_list))

def calculator(string):
    x = float(string[0])
    y = string[1]
    z = float(string[2])

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    else:
        try:
            result = x / z
        except ZeroDivisionError:
            sys.exit("Can't divide by zero")
    return round(result,1)

if __name__ == "__main__":
    main()