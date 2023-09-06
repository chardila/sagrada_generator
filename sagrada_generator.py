from PIL import Image, ImageDraw, ImageFont
import os


class CardGenerator:
    def __init__(self, font_path, output_path, card_file, ball_image):
        self.font_path = font_path
        self.output_path = output_path
        self.card_file = card_file
        self.ball_image = ball_image

    def create_card(self, label, parameter_file):
        font = ImageFont.truetype(self.font_path, 42)
        img = Image.new('RGB', (1055, 934), color='black')

        text = label.strip()
        print(text)

        total_balls = int(parameter_file.readline())

        for row in range(4):
            row_line = parameter_file.readline().strip()
            for column in range(5):
                tile_image = Image.open(f'{row_line[column]}.png')
                (height, width) = tile_image.size
                pos = (25 * (column + 1) + width * column, 20 * (row + 1) + height * row)
                img.paste(tile_image, pos)

        ball = Image.open(self.ball_image)
        ball_size = ball.size
        for n_ball in range(total_balls):
            img.paste(ball, (995 - n_ball * (ball_size[0] + 6), 820))

        file_card_name = parameter_file.readline().strip()
        path_card = os.path.join(self.output_path, f'{file_card_name}.png')
        canvas = ImageDraw.Draw(img)
        _, _, text_width, text_height = canvas.textbbox((0, 0), text, font)
        text_position = ((1055 - text_width) / 2, 810)
        canvas.text(text_position, text, font=font, fill='white')

        img = img.resize((1063, 945), Image.LANCZOS)
        img.save(path_card, dpi=(300, 300))
        next_label = parameter_file.readline().strip()

        if next_label:
            self.create_card(next_label, parameter_file)

    def generate_cards(self):
        with open(self.card_file) as file:
            os.makedirs(self.output_path, exist_ok=True)
            self.create_card(file.readline(), file)
            print("✓ Finished")


if __name__ == '__main__':
    card_generator = CardGenerator(
        font_path='UncialAntiqua-Regular.ttf',
        output_path='sagrada_output',
        card_file='card.txt',
        ball_image='O.png'
    )
    card_generator.generate_cards()
