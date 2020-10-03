import os
from datetime import datetime
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def watermark_text(input_image_path, output_image_path, text):
    photo = Image.open(input_image_path)
    drawing = ImageDraw.Draw(photo)
    w, h = photo.size
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 50)
    text_w, text_h = drawing.textsize(text, font)
    pos = w - text_w - 25, (h - text_h) - 25
    c_text = Image.new('RGB', (text_w, (text_h)), color = '#000000')
    drawing = ImageDraw.Draw(c_text)
    drawing.text((0,0), text, fill="#ffffff", font=font)
    c_text.putalpha(100)
    photo.paste(c_text, pos, c_text)
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
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('{0} | Developer: Daniil Mironyk'.format(dt_string))
    print('{0} | Version: 1.0.3'.format(dt_string))
    print('{0} | Required packages: pillow tqdm matplotlib'.format(dt_string))
    Tk().withdraw()
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    img = askopenfilename(filetypes=[('PNG pictures','*.png'), ('JPEG pictures','*.jpg')], title= "Please select a Image")
    print('Input file: {0}'.format(img))
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    ans = input("Watermark text: ")
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    output_file = input("Output file name: ") + '.png'
    watermark_text(img, output_file, text = ans)
    now = datetime.now(); dt_string = now.strftime("%d/%m/%Y %H:%M:%S"); print('{0} |'.format(dt_string), end=' ')
    pwd = os.getcwd()
    print('Saved file: {0}/{1}'.format(pwd, output_file))