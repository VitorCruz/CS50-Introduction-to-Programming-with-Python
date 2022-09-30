
from pyfiglet import Figlet
import random
import sys

def main():

    if len(sys.argv) == 3 and (sys.argv[1] not in ['-f', '--font'] or sys.argv[2] not in Figlet().getFonts()):
        sys.exit("Usage: figlet.py --font font_name")

    if len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font_name = sys.argv[2]
    else:
        font_name = 'random'

    figlet = set_font(font_name)
    text_input = input("Input Text: ")
    print(figlet.renderText(text_input))

def set_font(font_name):

    figlet = Figlet()

    if font_name == 'random':
        font_used = random.choice(figlet.getFonts())
    else:
        font_used = font_name

    figlet.setFont(font=font_used)
    return figlet

if __name__ == "__main__":
    main()

