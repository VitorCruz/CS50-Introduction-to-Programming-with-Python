
def main():
    fraction = input("Fraction: ")
    result = calculate(fraction)
    print(gauge(result))

def calculate(fraction):
    while True:
        try:
            numbers = fraction.split("/")
            result = float(numbers[0]) / float(numbers[1])
            break
        except ZeroDivisionError:
            fraction = input("Can't divide by zero. Input a valid division number: ")
        except ValueError:
            fraction = input("Not an integer. Input only integers: ")
        except IndexError:
            fraction = input("Input a correct fraction with X/Y: ")

    return round(result * 100)

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return str(percentage)+'%'

if __name__ == "__main__":
    main()