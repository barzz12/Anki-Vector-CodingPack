import os

import anki_vector
import sys
import time
from anki_vector.util import degrees

text_to_draw = ""

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    sys.exit("Cannot import from PIL. Do `pip3 install --user Pillow` to install")

# Get font file from computer (change directory as needed)
try:
    font_file = ImageFont.truetype("arial.ttf", 20)
except IOError:
    try:
        font_file = ImageFont.truetype(
            "/usr/share/fonts/noto/NotoSans-Medium.ttf", 20)
    except IOError:
        pass


def make_text_image(text_to_draw, x, y, font=None):
    '''
    Make a PIL.Image with the given text printed on it
   Args:
       text_to_draw (string): the text to draw to the image
       x (int): x pixel location
       y (int): y pixel location
       font (PIL.ImageFont): the font to use

   Returns:
       :class:(`PIL.Image.Image`): a PIL image with the text drawn on it
   '''
    dimensions = (184, 96)

    # make a blank image for the text, initialized to opaque black
    text_image = Image.new('RGBA', dimensions, (0, 0, 0, 255))
    # get a drawing context
    dc = ImageDraw.Draw(text_image)
    # draw the text
    dc.text((x, y), text_to_draw, fill=(255, 255, 255, 255), font=font)
    return text_image


def main():

    # Set text to create image from here
    face_image = make_text_image(text_to_draw, 0, 0, font_file)
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        # If necessary, Move Vector's Head and Lift to make it easy to see his face
        robot.behavior.set_head_angle(degrees(50.0))
        robot.behavior.set_lift_height(0.0)

        # Convert the image to the format used by the Screen
        print("Display image on Vector's face... made by https://www.kinvert.com/")
        screen_data = anki_vector.screen.convert_image_to_screen_data(face_image)
        robot.screen.set_screen_with_image_data(screen_data, 5.0, interrupt_running=True)
        robot.behavior.say_text("{}".format(text_to_draw))

        time.sleep(1)

def run():
    global text_to_draw
    text_to_draw = ""

    filename = "screen_text.txt"

    if not os.path.isfile(filename):  # path경로에서 파일 잇는지 검사
        # 파일이 없으면..
        print("screen_text.txt 파일을 만들어주세요.\n screen_text.txt안에 있는 내용을 읽어서 화면에 띄워줍니다.")
    else:
        # 파일이 있으면..
        with open(filename, "r") as inFp:
            inList = inFp.readlines()
            for txt in inList:
                text_to_draw = text_to_draw + txt
    main()


if __name__ == "__main__":
    run()