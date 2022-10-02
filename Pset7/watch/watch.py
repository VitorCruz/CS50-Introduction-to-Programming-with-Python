
import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    try:
        search = re.search(r'^<iframe.+src="http(s)?://(www\.)?youtube.com/embed/(\w+)"',s)
        link = 'https://youtu.be/' + search.group(3)
        return link

    except AttributeError:
        print("No match found")
        return None

if __name__ == "__main__":
    main()