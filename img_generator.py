from PIL import Image, ImageDraw, ImageFont

with Image.open('background_img.jpg') as im:
    draw = ImageDraw.Draw(im)

    text = 'ЖК "Зеленодар"\n' \
           'https://drane.one/'
    font = ImageFont.truetype("fonts/Times New Roman.ttf", 70)
    w_text, h_text = draw.textsize(text, font=font)
    w_img, h_img = im.size

    draw.text(
        ((w_img - w_text) // 2, (h_img - h_text) // 2),
        text,
        fill='white',
        font=font
        )

    # draw.text(((W - w) / 2, (H - h) / 2), msg, fill="black")

    im.show()
