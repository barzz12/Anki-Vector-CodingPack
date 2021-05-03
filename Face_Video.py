import os
import sys
import time, threading

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import anki_vector
from anki_vector.util import degrees

args = anki_vector.util.parse_command_args()

def wav():
    global robot,n
    global is_being_touched, is_being_pickup, current_lift_height_mm
    global i, the_song_end, inList, anki_wav_file_list

    the_song_end = False#음악이 끝까지 재생되고 다음 음아긍로 넘어갈 변수

    volume = 40
    #wname = "songs/mp3_{}.wav".format(i)

    #wav_file_list = os.listdir("songs")
    #play_wav = "songs\\" + wav_file_list[i]

    # anki_wav_file_list = []
    # for name in inList:  # 안키 벡터용 이미지로 변환하여 리스트로 저장
    #     anki_wav_file_list.append("songs\\" + name + ".wav")
    #
    # play_wav = anki_wav_file_list[i]
    #evt = threading.Event()
    play_wav = "HAPPY NEW YEAR 2020.wav"
    try:
        #evt.wait(timeout=0.5)
        robot.audio.stream_wav_file(play_wav, volume)
        the_song_end = True
        print(">> the song end")
    finally:
        if anki_vector.audio.playback_error is not None:
            anki_vector.audio.playback_error = None
            mythread = threading.Thread(target=wav)
            mythread.start()


def face_animation():
    global n
    image_settings = []
    face_images = []

    robot.behavior.set_head_angle(anki_vector.behavior.MAX_HEAD_ANGLE)  # 고개를 들라
    robot.behavior.set_lift_height(0.0)


    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = os.path.join(current_directory, "video")

    file_list = os.listdir("./video")
    print(len(file_list))

    # for i in range(1, 24):
    #     image_settings.append(image_path + '/face' + str(i) + '.jpg')
    #
    # for image_name in image_settings:
    #     image = Image.open(image_name)
    #
    #     pixel_bytes = anki_vector.screen.convert_image_to_screen_data(image)
    #
    #     face_images.append(pixel_bytes)

    anki_image_file_list = []
    i=0
    for name in file_list:  # 안키 벡터용 이미지로 변환하여 리스트로 저장
        image_file = Image.open("video\\" + name)
        resize_image = image_file.resize((184, 96))
        screen_data = anki_vector.screen.convert_image_to_screen_data(resize_image)
        anki_image_file_list.append(screen_data)
        i+=1
        if i % 100 == 0:
            print("{}".format(i))


    num_loops = 2
    duration_s = 0.04 #1/24
    mythread = threading.Thread(target=wav)
    mythread.start()

    #print("Press CTRL-C to quit (or wait %s seconds to complete)" % int(num_loops * duration_s * len(face_images)))
    print("Start")

    for i in range(0, len(anki_image_file_list)):
        robot.screen.set_screen_with_image_data(anki_image_file_list[i], 0.04)
        #time.sleep(0.01)

    print("END")
    while True:
        continue


with anki_vector.robot.Robot() as robot:
    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)
    robot.conn.release_control()
    time.sleep(1)
    robot.conn.request_control()
    face_animation()