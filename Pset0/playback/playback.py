

def main():
    user_input = input("Say something: ")
    print(slower_output(user_input))

def slower_output(string):
    return string.replace(' ', '...')

if __name__ == "__main__":
    main()

