
## VALIDATE E-MAIL WITHOUT RE LIBRARY
from validator_collection import checkers

def main():
    print(validade(input("Email Address: ")))

def validade(email):

    if checkers.is_email(email):
        return 'Valid'
    return 'Invalid'

if __name__ == "__main__":
    main()