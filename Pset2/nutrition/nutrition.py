
def main():
    dict_fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80,
    }

    user_fruit = input("Item: ")
    print(search_fruits_calories(user_fruit.lower(), dict_fruits))

def search_fruits_calories(user_fruit, dict_fruits):
    if user_fruit in dict_fruits.keys():
        return f"Calories: {dict_fruits[user_fruit]}"
    else:
        return "Fruit not in the list"

if __name__ == "__main__":
    main()