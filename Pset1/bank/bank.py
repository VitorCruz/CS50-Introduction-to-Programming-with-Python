

def main():
    greeting = input("Say something: ").strip()
    money = money_owed(greeting)
    print(f"${money}")

def money_owed(greeting):
    if greeting[0:5] == 'hello':
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()

