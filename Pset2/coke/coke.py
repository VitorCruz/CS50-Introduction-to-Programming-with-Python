
def main():
    user_has = 0
    change_owed = calculate_coke(user_has)
    print(f"Changed owed: {change_owed} cents")

def calculate_coke(user_has):
    while user_has < 50:
        try:
            amount_due = 50-user_has
            if amount_due > 0:
                print(f"Amount due: {amount_due}")
                
            coin = int(input("Insert a coin (valid values are 25,10 and 5 cents): "))
            if coin in [25,10,5]:
                user_has += coin
            else:
                print("Not a Valid value of coin")
        except TypeError:
            print("Not an integer")

    return user_has - 50

if __name__ == "__main__":
    main()