import os
from typing import TextIO

from PIL import Image, ImageDraw, ImageFont


# https://boardgamegeek.com/filepage/219948/sagrada-card-generator
# https://www.geeksforgeeks.org/working-images-python/
# https://www.geeksforgeeks.org/adding-text-on-image-using-python-pil/'
# https://stackoverflow.com/questions/8376359/how-to-create-a-transparent-gif-or-png-with-pil-python-imaging


def createCard(label: str, file_parameter: TextIO) -> None:
    font = ImageFont.truetype('UncialAntiqua-Regular.ttf', 42)
    img = Image.new('RGB', (1055, 934), color='black')
    text = label.strip()
    print(text)
    total_balls = int(file_parameter.readline())

    while label:
        for row in range(4):
            rowline = file_parameter.readline()
            for column in range(5):
                tile = Image.open(rowline[column] + ".png")
                (height, width) = tile.size
                pos = (25 * (column + 1) + width * column, 20 * (row + 1) + height * row)
                img.paste(tile, pos)

        ball = Image.open("O.png")
        ball_size = ball.size
        for n_ball in range(total_balls):
            img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))

        file_card_name = file_parameter.readline().strip()
        pathCard = "sagrada_output/" + file_card_name + ".png"
        kanvas = ImageDraw.Draw(img)
        _, _, w, h = kanvas.textbbox((0, 0), text, font=font)
        kanvas.text(((1055 - w) / 2, 810), text, font=font, fill='white')

        img = img.resize((1063, 945), Image.LANCZOS)
        img.save(pathCard, dpi=(300, 300))
        label = file_parameter.readline().strip()


if __name__ == '__main__':

    file = open('card.txt')
    try:
        if not os.path.exists('sagrada_output'):
            os.mkdir('sagrada_output')
        createCard(file.readline(), file)
        print("√ finish")
    finally:
        file.close()
