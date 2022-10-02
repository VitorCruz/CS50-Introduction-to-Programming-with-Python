
import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    try:
        search = re.search(r'^([0-9]{1,3}\.){3}[0-9]{1,3}$', ip)
        split = search.group(0).split('.')

        for item in split:
            if int(item) > 255:
                return False
        return True

    except AttributeError:
        print("No match found")
        return False
    except TypeError:
        print("IP's must be numbers with . separators")
        return False

if __name__ == "__main__":
    main()