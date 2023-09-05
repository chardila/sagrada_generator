# https://boardgamegeek.com/filepage/219948/sagrada-card-generator

# https://www.geeksforgeeks.org/working-images-python/
# https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/'
# https://stackoverflow.com/questions/8376359/how-to-create-a-transparent-gif-or-png-with-pil-python-imaging

from PIL import Image, ImageDraw, ImageFont
import os


def createCard(label, parameter_file):
    font = ImageFont.truetype('UncialAntiqua-Regular.ttf', 42)
    img = Image.new('RGB', (1055, 934), color='black')

    text = label.strip()
    print(text)
    total_balls = int(parameter_file.readline())

    for row in range(4):
        rowline = parameter_file.readline()
        for column in range(5):
            tile_image = Image.open(rowline[column] + ".png")
            (height, width) = tile_image.size
            pos = (25 * (column + 1) + width * column, 20 * (row + 1) + height * row)
            img.paste(tile_image, pos)

    ball = Image.open("O.png")
    ball_size = ball.size
    for n_ball in range(total_balls):
        img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))

    file_card_name = parameter_file.readline().strip()
    pathCard = "sagrada_output/" + file_card_name + ".png"
    kanvas = ImageDraw.Draw(img)
    _, _, w, h = kanvas.textbbox((0, 0), text, font=font)
    kanvas.text(((1055 - w) / 2, 810), text, font=font, fill='white')

    img = img.resize((1063, 945), Image.LANCZOS)
    img.save(pathCard, dpi=(300, 300))
    label = parameter_file.readline()
    if not label:
        return
    else:
        createCard(label, parameter_file)


if __name__ == '__main__':

    file = open('card.txt')
    try:
        if not os.path.exists('sagrada_output'):
            os.mkdir('sagrada_output')
        createCard(file.readline(), file)
        print("√ finish")
    finally:
        file.close()
