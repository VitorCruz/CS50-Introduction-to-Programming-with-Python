
from fpdf import FPDF
from PIL import Image, ImageDraw, ImageFont

def main():
    name = input("Name: ") + ' took CS50'
    make_pdf(name)


def make_pdf(name):

    ## DEFAULT VALUES > PORTRAIT AND A4 (210 X 297MM)
    pdf = FPDF()
    pdf.add_page()

    ## ADD FIRST LINE OF TEXT
    pdf.set_font('helvetica', 'B', size=46)
    pdf.cell(0, 60, txt="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    ## ADD IMAGE
    pdf.image("shirt_model.png", w=190, h=190)

    ## CHANGE FONT SIZE, COLOR, AND PRINT NAME ON THE SHIRT ON A "NEGATIVE" POSITION
    pdf.set_font('helvetica', 'B', size=22)
    pdf.set_text_color(255,255,255)
    pdf.cell(0, -250, txt=name, align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()

