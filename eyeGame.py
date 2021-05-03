import anki_vector
from anki_vector.util import degrees
from math import cos
import time


def main():
    args = anki_vector.util.parse_command_args()

    with anki_vector.Robot(args.serial) as robot:
        robot.behavior.set_head_angle(degrees(45))
        robot.behavior.say_text("Don't touch me yet")

        untouchTotal = 0
        for i in range(20):
            untouchTotal += robot.touch.last_sensor_reading.raw_touch_value
        untouched = untouchTotal / 20.0
        time.sleep(1.0)
        robot.behavior.say_text("touch my whole back")
        while not robot.touch.last_sensor_reading.is_being_touched:
            time.sleep(0.1)
        time.sleep(1.0)
        touchTotal = 0
        for i in range(20):
            touchTotal += robot.touch.last_sensor_reading.raw_touch_value
        touched = touchTotal / 20.0

        diff = touched - untouched

        robot.behavior.say_text("Experiment with how to change my eye color")
        robot.behavior.say_text("Keep my eyes red for one full second")
        score = 0
        wins = 0
        for i in range(100):
            for j in range(50):
                value = (robot.touch.last_sensor_reading.raw_touch_value - untouched) / diff
                robot.behavior.set_eye_color(hue=value, saturation=1.0)
                time.sleep(0.01)
                print(score)
                if wins == 0 and value < 0.02:  # red lowHue score += 0.01 if score > 1.0:
                    wins += 1
                    robot.behavior.say_text("Good job")
                    animation = 'anim_pounce_success_02'
                    robot.anim.play_animation(animation)
                    robot.behavior.say_text("Keep my eyes purple for one full second")
                    robot.behavior.set_head_angle(degrees(45))
                    score = 0
                if wins == 0 and value > 0.98:  # red hiHue
                    score += 0.01
                    if score > 1.0:
                        wins += 1
                        robot.behavior.say_text("Good job")
                        animation = 'anim_pounce_success_02'
                        robot.anim.play_animation(animation)
                        robot.behavior.say_text("Keep my eyes purple for one full second")
                        robot.behavior.set_head_angle(degrees(45))
                        score = 0
                elif wins == 1 and value > .77 and value < .94:  # purple score += 0.01 if score > 1.0:
                    wins += 1
                    robot.behavior.say_text("Good job")
                    animation = 'anim_pounce_success_02'
                    robot.anim.play_animation(animation)
                    robot.behavior.say_text("Keep my eyes blue for one full second")
                    robot.behavior.set_head_angle(degrees(45))
                    score = 0
                elif wins == 2 and value > .5 and value < .75:  # blue score += 0.01 if score > 1.0:
                    wins += 1
                    robot.behavior.say_text("Good job")
                    animation = 'anim_pounce_success_02'
                    robot.anim.play_animation(animation)
                    robot.behavior.say_text("Keep my eyes green for one full second")
                    robot.behavior.set_head_angle(degrees(45))
                    score = 0
                elif wins == 3 and value > .25 and value < .42:  # green score += 0.01 if score > 1.0:
                    wins += 1
                    robot.behavior.say_text("Good job")
                    animation = 'anim_pounce_success_02'
                    robot.anim.play_animation(animation)
                    robot.behavior.say_text("Keep my eyes yellow for one full second")
                    robot.behavior.set_head_angle(degrees(45))
                    score = 0
                elif wins == 4 and value > .1 and value < .175:  # yellow score += 0.01 if score > 1.0:
                    wins += 1
                    robot.behavior.say_text("Good job")
                    animation = 'anim_pounce_success_02'
                    robot.anim.play_animation(animation)
                    robot.behavior.say_text("You win")

                else:
                    score = 0
            if wins == 5:
                ang = robot.pose_angle_rad + 0.01
                robot.behavior.set_head_angle(degrees(45))
                robot.behavior.set_lift_height(1.0)

                robot.behavior.say_text("Thanks Keith's wife for suggesting the fist bump")
                time.sleep(0.5)
                robot.behavior.say_text("Please like the video. Keith is very self conscious about it, l o l")
                break


if __name__ == '__main__':
    main()