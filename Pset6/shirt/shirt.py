
## python shirt.py before1.jpg after.jpg
import sys
from PIL import Image
import PIL
import os

def main():

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif os.path.splitext(sys.argv[1])[1] not in ['.jpeg', '.png', '.jpg']:
        sys.exit("Input is not in the right image file format")
    elif os.path.splitext(sys.argv[2])[1] not in ['.jpeg', '.png', '.jpg']:
        sys.exit("Output is not in the right image file format")
    else:
        input_path = sys.argv[1]
        output_path = sys.argv[2]

    overlay_image(input_path, output_path)

def overlay_image(input_path, output_path):

    Shirt = Image.open("shirt.png")
    Size = Shirt.size

    Image1 = Image.open(input_path, mode='r')
    Image1 = PIL.ImageOps.fit(Image1, Size)
    Image1.paste(Shirt, Shirt)
    Image1.save(output_path)

if __name__ == "__main__":
    main()