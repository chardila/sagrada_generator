# Import necessary modules from the Python Imaging Library (PIL) and the os module
from PIL import Image, ImageDraw, ImageFont
import os

# Define constants
REGULAR_TTF = 'UncialAntiqua-Regular.ttf'  # Path to a TrueType font file
WHITE = 'white'  # Color used for text and drawing
OUTPUT_PATH = 'sagrada_output'  # Directory where the generated images will be saved
CARDS_FILE = 'card.txt'  # File containing card data
BALL = "O.png"  # Path to the ball image


# Function to create a card image based on label and parameters from a file
def create_card(label, parameter_file):
    # Load the font and create a blank black image
    font = ImageFont.truetype(REGULAR_TTF, 42)
    img = Image.new('RGB', (1055, 934), color='black')

    text = label.strip()  # Clean up label by removing leading/trailing whitespace
    print(text)

    total_balls = int(parameter_file.readline())  # Read the total number of balls from the parameter file

    # Loop through rows and columns to paste tile images onto the blank image
    for row in range(4):
        row_line = parameter_file.readline().strip()  # Clean up row line by removing leading/trailing whitespace
        for column in range(5):
            tile_image = Image.open(row_line[column] + ".png")  # Open a tile image
            (height, width) = tile_image.size
            pos = (25 * (column + 1) + width * column,
                   20 * (row + 1) + height * row)  # Calculate the position to paste the tile
            img.paste(tile_image, pos)  # Paste the tile image onto the blank image

    ball = Image.open(BALL)  # Open the ball image
    ball_size = ball.size
    for n_ball in range(total_balls):
        img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))  # Paste balls onto the image

    file_card_name = parameter_file.readline().strip()  # Read the card name from the parameter file
    path_card = os.path.join(OUTPUT_PATH,
                             file_card_name + ".png")  # Create a path for the card image using os.path.join
    canvas = ImageDraw.Draw(img)
    _, _, w, h = canvas.textbbox((0, 0), text, font=font)  # Get the bounding box for the text
    canvas.text(((1055 - w) / 2, 810), text, font=font, fill=WHITE)  # Add the text to the image

    img = img.resize((1063, 945), Image.LANCZOS)  # Resize the image
    img.save(path_card, dpi=(300, 300))  # Save the image with a specified DPI
    next_label = parameter_file.readline().strip()  # Read the next label from the parameter file

    # Recursive call to create_card if there's a next label
    if next_label:
        create_card(next_label, parameter_file)


if __name__ == '__main__':
    # Use a context manager (with statement) to open and close the file automatically
    with open(CARDS_FILE) as file:
        # Check if the OUTPUT_PATH directory exists, if not, create it
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

        # Call create_card with the first label and the open file
        create_card(file.readline(), file)
        print("✓ Finished")  # Print a message when the card generation is complete
