
def main():
    user_input = input("Input a camelCase name: ")
    print(to_snake_case(user_input))

def to_snake_case(string):
    new_variable = ''
    for letter in string:
        if letter.isupper():
            new_variable += '_' + letter.lower()
        else:
            new_variable += letter

    return new_variable

if __name__ == "__main__":
    main()