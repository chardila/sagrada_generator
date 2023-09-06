from PIL import Image, ImageDraw, ImageFont
import os


def create_card(label, parameter_file):
    # Load the font and create a blank image
    font = ImageFont.truetype('UncialAntiqua-Regular.ttf', 42)
    img = Image.new('RGB', (1055, 934), color='black')

    text = label.strip()  # Clean up label
    print(text)
    total_balls = int(parameter_file.readline())

    for row in range(4):
        row_line = parameter_file.readline().strip()  # Clean up row line
        for column in range(5):
            tile_image = Image.open(row_line[column] + ".png")
            (height, width) = tile_image.size
            pos = (25 * (column + 1) + width * column, 20 * (row + 1) + height * row)
            img.paste(tile_image, pos)

    ball = Image.open("O.png")
    ball_size = ball.size
    for n_ball in range(total_balls):
        img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))

    file_card_name = parameter_file.readline().strip()
    path_card = os.path.join("sagrada_output", file_card_name + ".png")  # Use os.path.join for paths
    canvas = ImageDraw.Draw(img)
    _, _, w, h = canvas.textbbox((0, 0), text, font=font)
    canvas.text(((1055 - w) / 2, 810), text, font=font, fill='white')

    img = img.resize((1063, 945), Image.LANCZOS)
    img.save(path_card, dpi=(300, 300))
    next_label = parameter_file.readline().strip()

    if next_label:
        create_card(next_label, parameter_file)


if __name__ == '__main__':
    # Use a context manager (with statement) to open and close the file automatically
    with open('card.txt') as file:
        if not os.path.exists('sagrada_output'):
            os.mkdir('sagrada_output')
        create_card(file.readline(), file)
        print("✓ Finished")
