import sys
import time

import anki_vector
from random import *
import threading
from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent

#1. 대답 좆 같이 하기
#2. 만지지마
#3. 들어올리지마(화내기)
#4. 절벽 돌진
#5. 얼굴못생겼어(뒤로돌기)
#7. 내 큐브 가만히좀 놔둬
#8. 큐브 tap거리지마
#9. 던지면 살려줘

i=0
class HateTouch:
    command = ["you", "hey", "I'm angry", "you suck", "hey pussy", "What the fuck"]
    command1 = ["mother fucker", "turn hands off", "stop touching", "Suck my dick!", "don't touch me"]
    command2 = ["turn hands off", "mother fucker", "put me down", "let me down", "son of bitch"]
    #command3 = []
    #command4 = []
    command_no = ["fuck off!!","Don't talk to me","What the fuck are you talking about?","stop bothering me","I’m irritated","you are really annoying","fucking idiot. stop talking"]

    anim = ["anim_rtpickup_loop_09", "anim_rtpickup_loop_10", "anim_feedback_shutup_01", "anim_rtpickup_loop_09"]
    anim2 = ["anim_reacttocliff_wheely_01", "anim_pounce_03", "anim_volume_stage_05", "anim_cube_success_getout_01",
         "anim_onboarding_cube_success_getout_01"]

    enable_face = True
    enable_cube = True
    enable_cube_tap = True

    # enable_givecube = 0
    # giveMeCube = 0
    cube_moved = False

    is_falling = False

    def __init__(self):
        self.run()

    def run(self):
        global is_being_touched, is_cliff, is_look, is_free, connected_cube, is_cube, is_tap
        is_cliff = False
        is_look = False
        is_free = 0
        connected_cube = False
        is_cube = False
        is_tap = False


        evt = threading.Event()
        args = anki_vector.util.parse_command_args()
        with anki_vector.Robot(args.serial) as robot:

            robot.behavior.drive_off_charger()
            robot.vision.enable_face_detection(detect_faces=True, estimate_expression=True)
            #enable_face_detection = True, show_viewer = True

            robot.events.subscribe(self.on_robot_observed_face, Events.robot_observed_face) #클래스 함수이면 자동으로 self인자가 주기 때문에
            robot.events.subscribe(self.on_robot_state, Events.robot_state)
            robot.events.subscribe(self.on_user_wake_word, Events.wake_word)  # 헤이 벡터하면 비동기적으로 함수 실행해서 컨트롤을 활성화함
            robot.events.subscribe(self.on_user_intent, Events.user_intent)  # 컨트롤이 활성화된 상태에서 명ㄹㅇ을 받아 코딩실행

            robot.events.subscribe(self.on_robot_cube, Events.robot_observed_object)
            robot.events.subscribe(self.on_robot_cube_moved, Events.object_moved)
            robot.events.subscribe(self.on_robot_cube_finish, Events.object_finished_move)
            robot.events.subscribe(self.on_robot_cube_tap, Events.object_tapped)


            #start program
            robot.behavior.say_text("I hate you!!")
            robot.conn.release_control()
            print("-- Vector hates you!! --")

            count=0
            count2=0
            count3=0
            count4=0
            giveMeCubeLimit=100 #10초, 나한테큐브줘 말하는 때 변수
            while True:
            #{
                if self.enable_face == False:
                    count += 1
                    if count > 50:
                        count=0
                        self.enable_face = True

                if self.enable_cube == False:
                    count2 += 1
                    if count2 > 300:
                        count2=0
                        self.enable_cube = True

                if self.enable_cube_tap == False:
                    count3 += 1
                    if count3 > 45:
                        count3=0
                        self.enable_cube_tap = True

                if robot.status.is_falling == True:
                    self.is_falling = True
                    count4 = 0
                if self.is_falling == True:
                    count4 += 1
                    if count4 > 30:
                        count4=0
                        self.is_falling = False


                # if giveMeCubeLimit < self.giveMeCube:
                #     self.giveMeCube = randrange(300, 1200, 10)
                #     print(self.giveMeCube)
                #     if not robot.conn.requires_behavior_control:
                #         robot.conn.request_control()
                #         time.sleep(0.5)
                #     if robot.conn.requires_behavior_control:
                #         robot.behavior.say_text("hey where is my cube")
                #         time.sleep(0.5)
                #     giveMeCubeLimit = self.giveMeCube
                #     self.giveMeCube=0
                # else:
                #     self.giveMeCube+=1

                if is_free >= 2:
                    time.sleep(0.5)
                    if is_free >= 3:  # 명령을 알아들어서 수행 할 경우
                        # print("continue")
                        time.sleep(2.6)
                        is_free = 0
                    else:  # 명령을 못알아듣거나 wake up 시간 초과 됐을 경우
                        # print("free")
                        is_free = 0

                touch_data = robot.touch.last_sensor_reading
                is_being_touched = touch_data.is_being_touched
                if is_being_touched and not robot.status.is_picked_up:
                    #print("touch!!!")
                    if not robot.conn.requires_behavior_control:
                        robot.conn.request_control()
                        time.sleep(0.1)
                    if robot.conn.requires_behavior_control:

                        num3 = randint(0, len(self.anim)-1)
                        threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()

                        num = randint(0, len(self.command)-1)
                        num1 = randint(0, len(self.command1)-1)
                        robot.behavior.say_text("{0} {1}!!".format(self.command[num], self.command1[num1]))

                        time.sleep(0.5)

                else:
                    if not robot.status.is_picked_up and not is_cliff and not is_look and is_free==0 and not is_cube and not is_tap:
                        if robot.conn.requires_behavior_control:
                            pass
                            robot.conn.release_control()
                            #print("free!!!")

                time.sleep(0.1)
            #}

    def cube(self, robot):
        global connected_cube

        max_attempts = 5
        attempts = 0
        while attempts < max_attempts:
            print("connect to a cube...")
            robot.world.connect_cube()
            attempts = attempts + 1
            connected_cube = robot.world.connected_light_cube
            if connected_cube:
                print("done connecting!")
                break

    def on_robot_cube(self, robot, event_type, event):
        global is_look, is_cube
        #print(robot.world.charger)
        if self.enable_cube:
            is_cube = True

            if not robot.conn.requires_behavior_control:
                robot.conn.request_control()
                time.sleep(0.1)
            if robot.conn.requires_behavior_control:
                #print("cube!!!!!!!!!!!")
                self.enable_cube = False
                mythread2 = threading.Thread(target=self.cube, args={robot})
                mythread2.start()

                num3 = randint(0, len(self.anim) - 1)
                threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()

                robot.behavior.say_text("This is my Cube mother fucker")

                is_cube = False

    def on_robot_cube_tap(self, robot, event_type, event):
        global is_tap
        #print("tap")
        if self.enable_cube_tap:
            is_tap = True
            self.enable_cube_tap = False
            if self.cube_moved:
                if not robot.conn.requires_behavior_control:
                    robot.conn.request_control()
                    time.sleep(0.1)
                if robot.conn.requires_behavior_control:
                    #print("큐브 그만 흔들어")
                    num3 = randint(0, len(self.anim) - 1)
                    threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
                    robot.behavior.say_text("Stop shaking with my cube mother fucker!!")
                    is_tap = False
            else:
                if not robot.conn.requires_behavior_control:
                    robot.conn.request_control()
                    time.sleep(0.1)
                if robot.conn.requires_behavior_control:
                    #print("내 큐브 그만 쳐라 씨발련아")
                    num3 = randint(0, len(self.anim) - 1)
                    threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
                    robot.behavior.say_text("Stop hitting my cube ugly bitch")
                    is_tap = False
        else:
            pass




    def on_robot_cube_moved(self, robot, event_type, event):
        #print("moved")
        self.cube_moved = True

    def on_robot_cube_finish(self, robot, event_type, event):
        #print("finish!")
        self.cube_moved = False


    def on_user_intent(self, robot, event_type, event):
        global is_free
        is_free += 1
        user_intent = UserIntent(event)

        if user_intent.intent_event is UserIntentEvent.character_age:# “How old are you?”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("i'm younger than you, pussy old man!!")

        elif user_intent.intent_event is UserIntentEvent.greeting_hello:  # “Hello!”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
            robot.behavior.say_text("who are you? do you know me?")

        elif user_intent.intent_event is UserIntentEvent.greeting_goodmorning:  # “Good morning!”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("fucking morning!")

        elif user_intent.intent_event is UserIntentEvent.check_timer or user_intent.intent_event is UserIntentEvent.set_timer \
                or user_intent.intent_event is UserIntentEvent.weather_response:  # “Check the timer.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
            robot.behavior.say_text("Do it with your fucking smartphone!")

        elif user_intent.intent_event is UserIntentEvent.greeting_goodbye:  # “Goodbye!”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
            robot.behavior.say_text("I don't want to see you forever!")

        elif user_intent.intent_event is UserIntentEvent.imperative_dance:  # “Dance.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
            robot.behavior.say_text("Fuck yourself!!")

        elif user_intent.intent_event is UserIntentEvent.imperative_fetchcube or user_intent.intent_event is UserIntentEvent.imperative_findcube \
                or user_intent.intent_event is UserIntentEvent.play_pickupcube or user_intent.intent_event is UserIntentEvent.play_rollcube:  # “Fetch your cube.”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("i don't feel like it. fucking idiot")

        elif user_intent.intent_event is UserIntentEvent.imperative_abuse:  # “I hate you.”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("shut the fuck up!")

        elif user_intent.intent_event is UserIntentEvent.imperative_come:  # “Come here.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("go fuck your self!")

        elif user_intent.intent_event is UserIntentEvent.imperative_lookatme:  # “Look at me.”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("what the ugly mother fucker!!")

        elif user_intent.intent_event is UserIntentEvent.imperative_love:  # “I love you.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("suck my dick")

        elif user_intent.intent_event is UserIntentEvent.imperative_praise:  # “Good Robot.”
            robot.behavior.say_text("good your short pussy")

        elif user_intent.intent_event is UserIntentEvent.imperative_scold:  # “Bad Robot.”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("what the fuck did you say!")

        elif user_intent.intent_event is UserIntentEvent.knowledge_question:  # “I have a question.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("i don't care mother fucker!")

        elif user_intent.intent_event is UserIntentEvent.names_ask:  # “What’s my name?”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("your name is I!D!I!O!T! idiot boy hahaha")

        elif user_intent.intent_event is UserIntentEvent.play_fistbump:  # “Fist bump.”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("I want to punch your face with my fist")

        elif user_intent.intent_event is UserIntentEvent.seasonal_happynewyear:  # “Happy new year!”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("fucking happy new year! fuck you")

        elif user_intent.intent_event is UserIntentEvent.seasonal_happyholidays:  # “Happy holidays!”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("fucking holiday! fuck you")

        elif user_intent.intent_event is UserIntentEvent.show_clock:  # “What time is it?”
            num3 = randint(0, len(self.anim2) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim2[num3])}).start()
            robot.behavior.say_text("Look at the clock with your eyes mother fucker!")

        elif user_intent.intent_event is UserIntentEvent.take_a_photo:  # “Take a photo.”
            num = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num])}).start()
            robot.behavior.say_text("what the ugly mother fucker!!")

        else:
            num3 = randint(0, len(self.anim) - 1)
            threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()
            num = randint(0, len(self.command_no) - 1)
            robot.behavior.say_text("{}".format(self.command_no[num]))


    def on_user_wake_word(self, robot, event_type, event):
        global is_free
        is_free += 1
        #print("hey vector")
        robot.conn.request_control()


    def on_robot_observed_face(self, robot, event_type, event):
        global is_look,is_free

        if self.enable_face and event.name and is_free==0:#전역변수, 이름이있을경우, 헤이벡터 상태가 아닐경우
            is_look = True
            self.enable_face = False
            print(f"face {event.name}")
            if not robot.conn.requires_behavior_control:
                robot.conn.request_control()
                time.sleep(0.1)
            if robot.conn.requires_behavior_control:
                num3 = randint(0, len(self.anim)-1)
                threading.Thread(target=robot.anim.play_animation, args={"{}".format(self.anim[num3])}).start()

                robot.behavior.say_text("What the ugly mother fuker!")

                deg = int(choice((120, -120, 90, -90, 150, -150)))
                robot.behavior.turn_in_place(degrees(deg), accel=degrees(5000), speed=degrees(5000))
                is_look = False

        else:
            pass


    def on_robot_state(self, robot, event_type, event):
        global is_being_touched, is_cliff

        # if robot.status.is_carrying_block:
        #     print("carring")

        if self.is_falling:
            if robot.status.is_falling:
                if not robot.conn.requires_behavior_control:
                    robot.conn.request_control()
                    time.sleep(0.1)
                if robot.conn.requires_behavior_control:
                    #print("help!!!!!")
                    help = ["help","mother fucker help","stop fucking throwing","please help me","somebody help","please fucking help"]
                    robot.behavior.say_text("{}".format(choice(help))) #random.choice()

        else:
            if robot.status.is_picked_up:
                #if not robot.status.is_on_charger and not robot.status.is_cliff_detected:
                #print("pick up")
                if not robot.conn.requires_behavior_control:
                    robot.conn.request_control()
                    time.sleep(0.1)
                if robot.conn.requires_behavior_control:
                    threading.Thread(target=robot.anim.play_animation, args={"anim_rtpickup_loop_09"}).start()

                    num = randint(0, len(self.command) - 1)
                    num1 = randint(0, len(self.command2) - 1)
                    robot.behavior.say_text("{0} {1}!!".format(self.command[num], self.command2[num1]))


        if robot.status.is_cliff_detected:
            self.enable_face = False
            self.enable_cube = False
            self.enable_cube_tap = False
            time.sleep(1)
            if not robot.status.is_picked_up:
                #print("cliff")
                is_cliff = True
                if not robot.conn.requires_behavior_control:
                    robot.conn.request_control(behavior_control_level=anki_vector.connection.ControlPriorityLevel.OVERRIDE_BEHAVIORS_PRIORITY)
                    time.sleep(0.1)
                if robot.conn.requires_behavior_control:
                    threading.Thread(target=robot.behavior.say_text, args={"Ohhhh! there is a cliff!! i want to fall!"}).start()
                    # a = threading.Thread(target=robot.behavior.set_lift_height,
                    #                  args={1.0})
                    # a.start()

                    robot.behavior.set_lift_height(1.0)
                    #robot.behavior.set_head_angle(anki_vector.behavior.MIN_HEAD_ANGLE)
                    #time.sleep(0.5)
                    robot.behavior.drive_straight(distance_mm(-120), speed_mmps(50))
                    robot.motors.set_wheel_motors(1000, 1000)
                    time.sleep(1.2)
                    robot.motors.set_wheel_motors(0, 0)
                    robot.anim.play_animation("anim_reacttocliff_wheely_01")
                    #print("cliff end")
                    robot.conn.release_control()
                    is_cliff = False



if __name__ == "__main__":
    hate = HateTouch()


