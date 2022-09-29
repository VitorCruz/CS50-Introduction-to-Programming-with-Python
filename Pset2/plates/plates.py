import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    s = s.upper()
    valid_letters = string.ascii_uppercase
    valid_numbers = string.digits

    if s[0] not in valid_letters or s[1] not in valid_letters:
        return False
    if len(s) < 2 or len(s) > 6:
        return False

    first_letter = 0
    first_number = 999
    last_letter = 0

    for character in range(len(s)):
        if s[character] not in valid_letters and s[character] not in valid_numbers:
            return False
        if s[character] in valid_letters:
            if first_letter == 0:
                first_letter = character
            last_letter = character
        if s[character] in valid_numbers and first_number == 999:
            first_number = int(s[character])

    if first_number == 0:
        return False

    for middle_character in s[first_letter:last_letter]:
        if middle_character in valid_numbers:
            return False

    return True

if __name__ == "__main__":
    main()