import os
from datetime import datetime
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

    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 50)
    drawing.text(pos, text, fill=black, font=font)
    photo.save(output_image_path)

if __name__ == '__main__':
    os.system('clear')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    print('░██╗░░░░░░░██╗░█████╗░████████╗███████╗██████╗░███╗░░░███╗░█████╗░██████╗░██╗░░██╗░')
    print('░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗████╗░████║██╔══██╗██╔══██╗██║░██╔╝░')
    print('░╚██╗████╗██╔╝███████║░░░██║░░░█████╗░░██████╔╝██╔████╔██║███████║██████╔╝█████═╝░░')
    print('░░████╔═████║░██╔══██║░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗░░')
    print('░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║░░██║██║░░██║██║░╚██╗░')
    print('░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░')
    print('░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░')
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    print('Developer: Daniil Mironyk')
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    print('Version: 1.0.3')
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    print('Required packages: pillow tqdm matplotlib')
    Tk().withdraw()
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    img = askopenfilename(filetypes=[('PNG pictures','*.png'), ('JPEG pictures','*.jpg')], title= "Please select a Image")
    print('Input file: {0}'.format(img))
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    ans = input("Water mark text: ") + ' (c) Master Daniil'
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    output_file = input("File name: ") + '.png'
    for i in tqdm(range(100)):
      time.sleep(0.04)
    watermark_text(img, output_file, text = ans, pos=(0, 0))
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    print('Saved file: {0}'.format(output_file))