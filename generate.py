from PIL import Image, ImageDraw, ImageFont
import pandas as pd


def draw_text_multiline(draw, xy, text, font, line_len, line_height):
    i = 0
    while i < len(text):
        draw.text(xy, text[i:i + line_len], font=font, fill='white')
        i += line_len
        xy = (xy[0], xy[1] + line_height)


ATTACK_CARD_IMAGE_PATH = "card-attack.png"
SKILL_CARD_IMAGE_PATH = "card-skill.png"

if __name__ == "__main__":

    card_data = pd.read_excel('card_data.xlsx', sheet_name='单卡')
    print(card_data.values)

    for entity in card_data.values:

        width, height = 700, 1200
        # image = Image.new('RGB', (width, height), color='white')

        type_name = entity[1]
        image = None
        if type_name == "攻击":
            image = Image.open(ATTACK_CARD_IMAGE_PATH)
        elif type_name == "技能":
            image = Image.open(SKILL_CARD_IMAGE_PATH)

        title_font = ImageFont.truetype('Songti.ttc', 100)
        desc_font = ImageFont.truetype('Songti.ttc', 50)

        title_x, title_y = 50, 60
        desc_x, desc_y = 50, 250

        draw = ImageDraw.Draw(image)

        # draw title
        draw.text((title_x, title_y), entity[0], font=title_font, fill='white')

        # draw desc
        draw_text_multiline(draw, (desc_x, desc_y), entity[1], desc_font, 12, 65)

        image.save(f'exports/{entity[0]}.png')