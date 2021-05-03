import anki_vector
import time
from anki_vector.util import degrees, distance_mm, speed_mmps, Pose
from anki_vector.events import Events

import functools
import threading
import sys

cube_pose = Pose(x=0, y=0, z=0, angle_z=degrees(0))
observed_event = threading.Event()
moved_event = threading.Event()


def on_oo(robot, event_type, event, evt):
    observed_event.set()



def on_om(robot, event_type, event, evt):
    moved_event.set()


def main():
    with anki_vector.Robot() as robot:
        #robot.conn.request_control()
        #print(robot.conn.requires_behavior_control)#컨트롤 상태일때 true
        try:
            while True:
                robot.behavior.set_eye_color(0.0, 1.0)
                robot.anim.play_animation('anim_eyepose_furious')

                #Events.robot_observed_object : Robot event triggered when an object is observed by the robot.
                # 이벤트가 발생하면 함수 호출, 리턴값이 함수의 아규먼트에 들어가게 된다. 이벤트핸들러에 등록. 한번 등록하면 이제 백그라운드에서 계속 실핼하고 있는거다
                robot.events.subscribe(on_oo, Events.robot_observed_object, (0,))

                robot.behavior.say_text("WHERE IS MY CUBE?", duration_scalar=1.0)#말하는 속도
                robot.behavior.set_head_angle(degrees(0))

                observed_event.clear()#쓰레드 0 세트 / 보통 전역변수로 루프조건을 하는데 이건 쓰레드 플래그를 이용하여 루프조건으로 씀
                while not observed_event.wait(timeout=0.4): #0.4초 지나면 무조건 리턴 -> 플래그가 1이면 true리턴 아니면 false
                    robot.behavior.turn_in_place(degrees(22.5), accel=degrees(5000), speed=degrees(5000))

                robot.events.unsubscribe(on_oo, Events.robot_observed_object)#이벤트핸들러에 등록했던 걸 백그라운드 해제

                print("move to cube")
                robot.world.connect_cube()
                robot.behavior.dock_with_cube(robot.world.connected_light_cube, num_retries=3)#큐브를 향해 감
                robot.behavior.say_text("GOTCHA!", duration_scalar=0.9)
                robot.behavior.set_lift_height(1.0, accel=255, max_speed=255)
                robot.behavior.set_lift_height(0, accel=255, max_speed=255)

                moved_event.clear()
                robot.events.subscribe(on_om, Events.object_moved, moved_event)#Events.object_moved: 사물이 카메라에서 벗어났을때
                while not moved_event.wait():
                    robot.events.unsubscribe(on_om, Events.object_moved)
                print("find cube")
        except KeyboardInterrupt:
            sys.exit()


if __name__ == '__main__':
    main()