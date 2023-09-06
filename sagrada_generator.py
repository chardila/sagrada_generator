from PIL import Image, ImageDraw, ImageFont
import os

# Constants
REGULAR_TTF = 'UncialAntiqua-Regular.ttf'
WHITE = 'white'
OUTPUT_PATH = 'sagrada_output'
CARDS_FILE = 'card.txt'
BALL = "O.png"


# Function to create a card image based on label and parameters from a file
def create_card(label, parameter_file):
    # Load the font and create a blank black image
    font = ImageFont.truetype(REGULAR_TTF, 42)
    img = Image.new('RGB', (1055, 934), color='black')

    text = label.strip()
    print(text)

    total_balls = int(parameter_file.readline())

    # Loop through rows and columns to paste tile images onto the blank image
    for row in range(4):
        row_line = parameter_file.readline().strip()
        for column in range(5):
            tile_image = Image.open(f'{row_line[column]}.png')
            (height, width) = tile_image.size
            pos = (25 * (column + 1) + width * column, 20 * (row + 1) + height * row)
            img.paste(tile_image, pos)

    ball = Image.open(BALL)
    ball_size = ball.size
    for n_ball in range(total_balls):
        img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))

    file_card_name = parameter_file.readline().strip()
    path_card = os.path.join(OUTPUT_PATH, f'{file_card_name}.png')
    canvas = ImageDraw.Draw(img)
    # text_width, text_height = canvas.textsize(text, font=font)
    _, _, text_width, text_height = canvas.textbbox((0, 0), text, font)
    text_position = ((1055 - text_width) / 2, 810)
    canvas.text(text_position, text, font=font, fill=WHITE)

    img = img.resize((1063, 945), Image.LANCZOS)
    img.save(path_card, dpi=(300, 300))
    next_label = parameter_file.readline().strip()

    if next_label:
        create_card(next_label, parameter_file)


def main():
    # Use a context manager (with statement) to open and close the file automatically
    with open(CARDS_FILE) as file:
        # Check if the OUTPUT_PATH directory exists, if not, create it
        os.makedirs(OUTPUT_PATH, exist_ok=True)

        # Call create_card with the first label and the open file
        create_card(file.readline(), file)
        print("✓ Finished")


if __name__ == '__main__':
    main()
