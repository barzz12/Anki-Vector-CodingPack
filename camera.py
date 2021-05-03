import anki_vector
import time
from PIL import Image
import threading
from anki_vector.util import degrees


def main():
    global robot
    global n
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    while True:
        if n == 1:
            print("break")
            break

        robot.camera.init_camera_feed()
        robot.vision.enable_display_camera_feed_on_face(True)
        #robot.vision.enable_face_detection(estimate_expression=True)

def run():
    global robot
    global n
    n = 0

    args = anki_vector.util.parse_command_args()
    robot = anki_vector.Robot(args.serial)
    robot.connect()

    mythread = threading.Thread(target=main)
    mythread.start()

def stop():
    global robot
    global n
    n=1
    robot.disconnect()

if __name__ == "__main__":
    run()