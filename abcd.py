import asyncio
import time
import anki_vector
import random
import time
import asyncio
import logging
import sys
import json
from threading import Thread

from anki_vector.util import degrees
from PIL import Image, ImageDraw, ImageFont
import anki_vector
from anki_vector.events import Events
from anki_vector.util import degrees, distance_mm, speed_mmps

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    logging.warning("Cannot import from PIL: Do `pip3 install --user Pillow` to install")


async def callback(robot, event_type, event):
    await asyncio.wrap_future(robot.anim.play_animation_trigger('GreetAfterLongTime'))
    await asyncio.sleep(2.0)
    await asyncio.wrap_future(robot.behavior.set_head_angle(anki_vector.util.degrees(40)))


def run():
    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(serial=args.serial, enable_face_detection=True) as robot:



if __name__ == "__main__":
    # def getFunc(num):
    #     for i in range(0,num):
    #         yield i
    #         print("generator loading")
    # for data in getFunc(5):
    #     print(data)
    #     time.sleep(1.5)
    run()


