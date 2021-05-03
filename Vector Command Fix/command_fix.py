import json
import os
import threading
import time
from pathlib import Path

import anki_vector
import random
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent
import asyncio

#anim_pounce_01 내려찍기
#anim_qa_head_updown 끄덕끄덕
#anim_qa_lift_updown
anim = [
            ["anim_petting_bliss_getout_01","anim_movement_alreadyhere_01_head_angle_40","anim_pounce_success_02","anim_communication_cantdothat_01","anim_dancebeat_getout_01","anim_explorer_lookaround_01","anim_greeting_goodmorning_01","anim_greeting_hello_02","anim_greeting_imhome_01"], #평범
            ["anim_reacttocliff_wheely_01","anim_pounce_03","anim_volume_stage_05", "anim_cube_success_getout_01","anim_onboarding_cube_success_getout_01"],#과함
            ["anim_reacttocliff_turtleroll_03","anim_reacttoblock_dropfail_02","anim_rtpickup_loop_09","anim_rtpickup_loop_10","anim_feedback_shutup_01"] #화남
        ]
# ["anim_rtshake_lv3pregetout_01", "anim_power_offon_03", "anim_knowledgegraph_fail_01", "anim_lookatphone_getin_01",
#  "anim_lowlightcharger_search_getout_01", "anim_nowifi_signal_01"],  # i have a question실패
#"anim_onboarding_wakeup_01"

def main():
    global robot, is_free

    def on_user_intent(robot, event_type, event, done):
        global is_free

        is_free += 1
        print("Vector : ", end='')

        user_intent = UserIntent(event)

        if user_intent.intent_event is UserIntentEvent.character_age:# “How old are you?”
            #is_being_anim = True
            is_anim_index = anim[anim_index[0]]
            Str = random.choice(command[0])
            anim_start = random.choice(is_anim_index)
            #my_thread = threading.Thread(target=sub1, args=())
            #my_thread.start()
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()#비동기용 로봇 실행
            b.result()


        elif user_intent.intent_event is UserIntentEvent.check_timer:#“Check the timer.”
            is_anim_index = anim[anim_index[1]]
            Str = random.choice(command[1])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.explore_start:#“Go explore.”
            is_anim_index = anim[anim_index[2]]
            Str = random.choice(command[2])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.global_stop:#“Stop the timer.”
            is_anim_index = anim[anim_index[3]]
            Str = random.choice(command[3])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.greeting_goodbye:# “Goodbye!”
            is_anim_index = anim[anim_index[4]]
            Str = random.choice(command[4])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.greeting_goodmorning:#“Good morning!”
            is_anim_index = anim[anim_index[5]]
            Str = random.choice(command[5])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.greeting_hello:#“Hello!”
            is_anim_index = anim[anim_index[6]]
            Str = random.choice(command[6])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_abuse:#“I hate you.”
            is_anim_index = anim[anim_index[7]]
            Str = random.choice(command[7])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_affirmative:#“Yes.”
            is_anim_index = anim[anim_index[8]]
            Str = random.choice(command[8])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_apology:# “I’m sorry.”
            is_anim_index = random.choice(anim[9])
            Str = random.choice(command[9])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_come:# “Come here.”
            is_anim_index = anim[anim_index[10]]
            Str = random.choice(command[10])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_dance:# “Dance.”
            is_anim_index = anim[anim_index[11]]
            Str = random.choice(command[11])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_fetchcube:# “Fetch your cube.”
            is_anim_index = anim[anim_index[12]]
            Str = random.choice(command[12])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_findcube:# “Find your cube.”
            is_anim_index = anim[anim_index[13]]
            Str = random.choice(command[13])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_lookatme:#“Look at me.”
            is_anim_index = anim[anim_index[14]]
            Str = random.choice(command[14])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_love:#“I love you.”
            is_anim_index = anim[anim_index[15]]
            Str = random.choice(command[15])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_negative:#“No.”
            is_anim_index = anim[anim_index[16]]
            Str = random.choice(command[16])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_praise:#“Good Robot.”
            is_anim_index = anim[anim_index[17]]
            Str = random.choice(command[17])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_scold:#“Bad Robot.”
            is_anim_index = anim[anim_index[18]]
            Str = random.choice(command[18])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_volumelevel:  # “Volume down.”
            is_anim_index = anim[anim_index[19]]
            Str = random.choice(command[19])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_volumelevel:  # “Volume 2.”
            is_anim_index = anim[anim_index[20]]
            Str = random.choice(command[20])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.imperative_volumeup:#“Volume up.”
            is_anim_index = anim[anim_index[21]]
            Str = random.choice(command[21])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.knowledge_question:# “I have a question.”
            is_anim_index = anim[anim_index[22]]
            Str = random.choice(command[22])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.movement_backward:#“Go backward.”
            is_anim_index = anim[anim_index[23]]
            Str = random.choice(command[23])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.movement_forward:  # “Go forward.”
            is_anim_index = anim[anim_index[24]]
            Str = random.choice(command[24])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.movement_turnaround:  #“Turn around.”
            is_anim_index = anim[anim_index[25]]
            Str = random.choice(command[25])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.movement_turnleft:  # “Turn left.”
            is_anim_index = anim[anim_index[26]]
            Str = random.choice(command[26])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.movement_turnright:  #“Turn right.”
            is_anim_index = anim[anim_index[27]]
            Str = random.choice(command[27])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.names_ask:#“What’s my name?”
            is_anim_index = anim[anim_index[28]]
            Str = random.choice(command[28])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_anygame:#“Play a game.”
            is_anim_index = anim[anim_index[29]]
            Str = random.choice(command[29])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_anytrick:#“Play a trick.”
            is_anim_index = anim[anim_index[30]]
            Str = random.choice(command[30])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_blackjack:#“Let’s play Blackjack.”
            is_anim_index = anim[anim_index[31]]
            Str = random.choice(command[31])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_fistbump:#“Fist bump.”
            is_anim_index = anim[anim_index[32]]
            Str = random.choice(command[32])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_pickupcube:# “Pick up your cube.”
            is_anim_index = anim[anim_index[33]]
            Str = random.choice(command[33])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_popawheelie:# “Pop a wheelie.”
            is_anim_index = anim[anim_index[34]]
            Str = random.choice(command[34])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.play_rollcube:#“Roll your cube.”
            is_anim_index = anim[anim_index[35]]
            Str = random.choice(command[35])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.seasonal_happyholidays:# “Happy holidays!”
            is_anim_index = anim[anim_index[36]]
            Str = random.choice(command[36])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.seasonal_happynewyear:# “Happy new year!”
            is_anim_index = anim[anim_index[37]]
            Str = random.choice(command[37])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.set_timer:#“Set timer for 10 minutes”
            is_anim_index = anim[anim_index[38]]
            Str = random.choice(command[38])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.show_clock:#“What time is it?”
            is_anim_index = anim[anim_index[39]]
            Str = random.choice(command[39])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.take_a_photo:#“Take a photo.”
            is_anim_index = anim[anim_index[40]]
            Str = random.choice(command[40])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

        elif user_intent.intent_event is UserIntentEvent.weather_response:# “What is the weather report?”
            is_anim_index = anim[anim_index[41]]
            Str = random.choice(command[41])
            anim_start = random.choice(is_anim_index)
            print(Str)
            a = robot.behavior.say_text("{}".format(Str))
            b = robot.anim.play_animation("{}".format(anim_start))
            a.result()  # 비동기용 로봇 실행
            b.result()

            # data = json.loads(user_intent.intent_data)
            # print(f"Weather report for {data['speakableLocationString']}: "
            #        f"{data['condition']}, temperature {data['temperature']} degrees")
            # robot.behavior.say_text(f"Weather report for {data['speakableLocationString']}: "
            #         f"{data['condition']}, temperature {data['temperature']} degrees")
        else:
            robot.behavior.say_text("{}".format("I don't understand"))

        #done.set()
        robot.conn.release_control()


    def on_user_wake_word(robot, event_type, event, done2):
        global is_free
        is_free += 1
        robot.conn.request_control()


    #------
    is_free = 0
    done = threading.Event()
    robot.events.subscribe(on_user_wake_word, Events.wake_word, done)#헤이 벡터하면 비동기적으로 함수 실행해서 컨트롤을 활성화함
    robot.events.subscribe(on_user_intent, Events.user_intent, done)#컨트롤이 활성화된 상태에서 명ㄹㅇ을 받아 코딩실행

    robot.conn.release_control()#벡터 자유행동

    while not done.wait(timeout=1.5):#1.5초마다 루프 하라는것과 같음
        #print(is_free)
        if is_free >= 2:
            time.sleep(0.5)
            if is_free >= 3:#명령을 알아들어서 수행 할 경우
                #print("continue")
                is_free = 0
            else:#명령을 못알아듣거나 wake up 시간 초과 됐을 경우
                robot.conn.release_control()  # 벡터 자유행동
                #print("free")
                is_free = 0



def stop():
    global robot
    global n
    n=1
    robot.disconnect()


def run():
    global robot
    global n, command,anim_index
    global is_being_anim, is_anim_index

    n=0

    command = list()
    anim_index = list()

    is_being_anim = False
    is_anim_index = 0

    args = anki_vector.util.parse_command_args()
    robot = anki_vector.AsyncRobot(args.serial)
    #robot = anki_vector.Robot(args.serial)
    robot.connect()

    filename = "command.txt"

    if not os.path.isfile(filename):  # path경로에서 파일 잇는지 검사
        # 파일이 없으면..
        print("Please create 'command.txt' file in the forder...")
    else:
        # 파일이 있으면..
        with open(filename, "r", encoding="utf-8-sig") as inFp:
            inList = inFp.readlines()
            # print(inList)
            i = 0
            for txt in inList:
                if txt[0] == '#':
                    tmpList = txt[1:-1].split(',')
                    command.append(tmpList)
                if txt[0] == '%':
                    anim_index.append(int(txt[1]))
                i += 1

    main()



if __name__ == '__main__':
    run()


