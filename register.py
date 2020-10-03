from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import time
from tqdm import tqdm

def watermark_text(input_image_path,
                   output_image_path,
                   text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (10, 18, 24)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 50)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)

if __name__ == '__main__':
    print('░██╗░░░░░░░██╗░█████╗░████████╗███████╗██████╗░░░░███╗░░░███╗░█████╗░██████╗░██╗░░██╗░')
    print('░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗░░░████╗░████║██╔══██╗██╔══██╗██║░██╔╝░')
    print('░╚██╗████╗██╔╝██║░░██║░░░██║░░░█████╗░░██████╔╝░░░██╔████╔██║███████║██████╔╝█████═╝░░')
    print('░░████╔═████║░██║░░██║░░░██║░░░██╔══╝░░██╔══██╗░░░██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░░')
    print('░░╚██╔╝░╚██╔╝░╚█████╔╝░░░██║░░░███████╗██║░░██║░░░██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗░')
    print('░░░╚═╝░░░╚═╝░░░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░░░Daniil░Mironyk░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░v░1.0.0░░░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    Tk().withdraw()
    img = askopenfilename(filetypes=[('PNG pictures','*.png'), ('JPEG pictures','*.jpg')], title= "Please select a Image")
    ans = input("Water mark text: ")
    output_file = input("File name: ") + '.png'
    for i in tqdm(range(100)):
      time.sleep(0.1)
    watermark_text(img, output_file, text = ans, pos=(0, 0))