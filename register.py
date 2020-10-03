from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from tkinter import *
from tkinter.filedialog import askopenfilename

def watermark_text(input_image_path, output_image_path, text, pos):
    photo = Image.open(input_image_path)

    # make the image editable
    drawing = ImageDraw.Draw(photo)

    black = (3, 8, 12)
    font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    drawing.text(pos, text, fill=black, font=font)
    photo.show()
    photo.save(output_image_path)

if __name__ == '__main__':
    filename = askopenfilename(defaultextension='.jpg', filetypes=[('PNG pictures','*.png'), ('JPEG pictures','*.jpg')])
    answer = input("Watter mark: ")
    img = print(filename)
    watermark_text(img, 'lighthouse_watermarked.jpg', text = print(answer), pos=(0, 0))