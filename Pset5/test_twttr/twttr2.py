
import unidecode

def main():
    user_string = input("Say something: ")
    print(shorten(user_string))

def shorten(word):
    word = unidecode.unidecode(word)
    vowels = 'aeiou'
    vowels_list = list(vowels) + list(vowels.upper())

    new_string = ''
    for letter in word:
        if letter not in vowels_list:
            new_string += letter

    return new_string.replace('  ', ' ').strip()

if __name__ == "__main__":
    main()