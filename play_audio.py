#!/usr/bin/env python3

# Copyright (c) 2018 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License isvi distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Play audio files through Vector's speaker.
"""
import os
import threading
import random, time
import anki_vector
from anki_vector.util import degrees
from PIL import Image


def anim():
    anim = ["anim_dancebeat_headliftbody_left_large_01",
            "anim_dancebeat_headliftbody_right_large_01",
            "anim_dancebeat_headliftbody_fwd_01",
            "anim_dancebeat_headliftbody_back_01"]
    time.sleep(9.8)
    while True:
        if n == 1:
            print("break")
            break
        idx = random.choice(anim)
        robot.anim.play_animation("{}".format(idx))
        time.sleep(0.1)


def main():
    global robot,n
    global is_being_touched, is_being_pickup, current_lift_height_mm
    global i, the_song_end

    the_song_end = False#음악이 끝까지 재생되고 다음 음아긍로 넘어갈 변수

    volume = 40
    wname = "songs/mp3_{}.wav".format(i)
    print(wname)

    try:
        robot.audio.stream_wav_file(str(wname), volume)
        the_song_end = True
        print(">> the song end")
    finally:
        if anki_vector.audio.playback_error is not None:
            #print("쓰레드 실행")
            anki_vector.audio.playback_error = None
            mythread = threading.Thread(target=main)
            mythread.start()

    #print("쓰레드 END")



def photo():
    #current_directory = os.path.dirname(os.path.realpath(__file__))
    #image_path = os.path.join(current_directory, "face_images", "mp3.jpg")
    #image_file = Image.open("face_images/mp3.jpg")
    global is_being_touched, is_being_pickup, current_lift_height_mm
    global robot, n, i, the_song_end

    next_song = True#벡터를 들었을때 다음/이전 곡으로 넘어갈 변수
    is_being_touched = False

    is_being_pickup = robot.status.is_picked_up
    current_lift_height_mm = robot.lift_height_mm

    dir = os.getcwd()#현재 디렉토리 경로 가져오기
    dir = dir + "\\face_images"
    file_num = len(os.listdir(dir))#해당 디렉토리 경로에 파일 갯수 반환

    while True:
        if n == 1:
            print("break")
            break

        robot.behavior.set_head_angle(degrees(45.0))
        robot.behavior.set_lift_height(0.0)

        fname = "face_images\\mp3_{}.jpg".format(i)
        image_file = Image.open("{}".format(fname))
        resize_image = image_file.resize((184, 96))

        print(">> Play MP3...")
        screen_data = anki_vector.screen.convert_image_to_screen_data(resize_image)
        robot.screen.set_screen_with_image_data(screen_data, 15.0)

        time.sleep(0.5)
        mythread = threading.Thread(target=main)
        mythread.start()

        while True:
            rad = robot.pose_pitch_rad

            if round(rad,1) >= 0.3:
                if next_song:
                    print(">>  next song..")
                    next_song = False
                    break

            elif round(rad,1) <= -0.2:
                if next_song:
                    next_song = False
                    i-=2
                    if (i+1) == 0:
                        i = file_num - 1
                    print(">> Previous song..")
                    break
            elif round(rad,1) <= 0.1 and round(rad,1) >= -0.1:
                next_song = True
                if the_song_end:
                    the_song_end = False
                    print(">>  next song..")
                    break

            robot.screen.set_screen_with_image_data(screen_data, 1.2)
            #print(round(rad, 1), end="\n\n")
            time.sleep(1.0)


        robot.disconnect()
        time.sleep(0.1)
        args = anki_vector.util.parse_command_args()
        robot = anki_vector.Robot(args.serial)
        robot.connect()

        if i >= file_num:
            i = 1
        elif i == 0:
            i = 1
        else:
            i += 1



def stop():
    global robot
    global n
    n=1
    robot.disconnect()

def run():
    global robot
    global n,i
    n=0
    i=1

    args = anki_vector.util.parse_command_args()
    robot = anki_vector.Robot(args.serial)
    robot.connect()

    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    mythread = threading.Thread(target=main)
    mythread2 = threading.Thread(target=anim)
    mythread3 = threading.Thread(target=photo)

    mythread.start()
    #mythread2.start()
    mythread3.start()



if __name__ == "__main__":
    run()

