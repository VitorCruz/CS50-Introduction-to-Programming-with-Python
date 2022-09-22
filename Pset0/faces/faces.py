
dict_faces = {
    ":)": "🙂",
    ":(": "🙁",
    ":|": "😐",
    }

def main():
    user_input = input("Say something: ")
    print(convert(user_input))

def convert(string):
    new_string = str(string)
    for face in dict_faces:
        new_string = new_string.replace(face, dict_faces[face])
    return new_string

if __name__ == "__main__":
    main()

