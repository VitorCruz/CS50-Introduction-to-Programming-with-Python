
def main():
    looking_for = ['42','forty-two','forty two']
    user_answer = input("What's the answer to the Great Question of Life, the Universe and Everything? ")
    if check_for_number(user_answer,looking_for):
        print("Yes")
    else:
        print("No")

def check_for_number(answer, looking_for):
    for word in looking_for:
        if word in answer:
            return True
    return False

if __name__ == "__main__":
    main()