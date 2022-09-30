
def main():
    result = grocery_list()
    result_sorted = sorted(result, reverse=False, key=lambda x: x)

    print()
    for item in result_sorted:
       print(result[item], ' x ', item.upper(), sep="")

def grocery_list():
    list = {}

    while True:
        try:
            item = input("Enter a grocery item: ")
            if item in list.keys():
                list[item] += 1
            else:
                list[item] = 1
        except EOFError:
            break

    return list

if __name__ == "__main__":
    main()