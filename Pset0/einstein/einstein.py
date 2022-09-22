
def main():
    user_input = int(input("What's your weight (mass) in kg? "))
    print(convert_to_energy(user_input))

def convert_to_energy(mass):
    return mass * pow(300000000,2)

if __name__ == "__main__":
    main()

