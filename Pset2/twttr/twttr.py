
def main():
    vowels = 'aeiou'
    vowels_list = list(vowels) + list(vowels.upper())
    user_string = input("Say something: ")
    print(omit_vowels(user_string, vowels_list))

def omit_vowels(string, vowels_list):
    new_string = ''
    for letter in string:
        if letter not in vowels_list:
            new_string += letter

    return new_string.replace('  ', ' ').strip()

if __name__ == "__main__":
    main()