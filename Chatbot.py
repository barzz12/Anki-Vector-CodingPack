import random
import datetime
import sys
import threading
import webbrowser
import pyttsx3
import wikipedia
from pygame import mixer
import speech_recognition as sr
import anki_vector
import time
from PIL import Image
from anki_vector.util import degrees
import os

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 5.0)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 25)

greetings = ['hey there', 'hello', 'hi', 'hey']
greetings_ = ' '.join(greetings)
question = ['how are you', 'how are you doing']
responses = ['Okay', "I'm fine"]

var1 = ['who made you', 'who created you', 'who made are you']
var2 = ['I was created by anki company.', 'ANKI!', 'some guy whom i never got to know. haha']

var3 = ['what time is it', 'what is the time', 'time', 'what\'s the time']

var4 = ['who are you', 'what is your name', 'what\'s your name']


cmd1 = ['open browser', 'open google', 'open Google']

cmd4 = ['open YouTube','open youtube']

cmd10 = ['open naver', 'open neighbor', 'open Naver']

cmd3 = ['tell a joke', 'tell me a joke', 'say something funny', 'tell something funny', 'tell me joke']
jokes = ['Can a kangaroo jump higher than a house? Of course, a house doesn’t jump at all.', 'My dog used to chase people on a bike a lot. It got so bad, finally I had to take his bike away.', 'Doctor: Im sorry but you suffer from a terminal illness and have only 10 to live.Patient: What do you mean, 10? 10 what? Months? Weeks?!"Doctor: Nine.']

cmd6 = ['stop', 'stop program']

cmd9 = ['thank you', 'I love you']
repfr9 = ['you\'re welcome', 'glad i could help you','my pleasure','i\'m fine thank you']


cmd2 = ['play music', 'play songs', 'play a song', 'open music player']

cmd5 = ['tell me the weather', 'weather', 'what about the weather']



"""
이어폰을 끼고 마이크를 사용해주세요. 작은 소리에도 민감하게 반응하오니 조심해 주세요.
"""
def anim():
    global robot
    global is_being_anim
    global anim_index

    anim = ["anim_pounce_success_02","anim_volume_stage_05"]

    while True:
        if is_being_anim :
            robot.anim.play_animation("{}".format(anim[anim_index]))
            #print("{}".format(anim[anim_index]))
            is_being_anim = False


def rainbowEyes():
    while True:
        if n == 1:
            print("break")
            break

        for j in range(100):
            robot.behavior.set_eye_color(hue=j/100.0, saturation=0.99)
            time.sleep(0.01)

def photo():
    #current_directory = os.path.dirname(os.path.realpath(__file__))
    #image_path = os.path.join(current_directory, "face_images", "chatbot.jpg")

    # Load an image
    image_file = Image.open("chatbot.jpg")

    # Convert the image to the format used by the Screen
    print("Display image on Vector's face...")
    screen_data = anki_vector.screen.convert_image_to_screen_data(image_file)

    duration_s = 360.0
    robot.screen.set_screen_with_image_data(screen_data, duration_s)


def main():
    global robot, n
    global is_being_anim, anim_index

    robot.behavior.set_head_angle(degrees(45.0))
    robot.behavior.set_lift_height(0.0)

    mythread_ = threading.Thread(target=photo)
    mythread_.start()

    robot.behavior.say_text("Let's start Chatting!")

    while True:
        if n == 1:
            print("break")
            break

        now = datetime.datetime.now()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nTell me something...")
            audio = r.listen(source)
            try:
                print("You said : " + r.recognize_google(audio))
            except sr.UnknownValueError:
                #print("Could not understand audio")
                #robot.behavior.say_text("sorry I cannot hear you")
                #engine.say('I didnt get that. Rerun the code')
                #engine.runAndWait()
                continue

        auido_ = str(r.recognize_google(audio))
        is_find = False

        if not is_find:
            for txt in cmd1:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 1

                            webbrowser.open('www.google.com')
                            robot.behavior.say_text("{}".format("ok, open Google"))
                            is_find = True
                            break

        if not is_find:
            for txt in cmd4:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 1

                            webbrowser.open('www.youtube.com')
                            robot.behavior.say_text("{}".format("ok, open youtube"))
                            is_find = True
                            break

        if not is_find:
            for txt in cmd10:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 1

                            webbrowser.open('www.naver.com')
                            robot.behavior.say_text("{}".format("ok, open naver"))
                            is_find = True
                            break

        if not is_find:
            for txt in greetings:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            random_greeting = random.choice(greetings)
                            is_being_anim = True
                            anim_index = 0

                            print("{} : {}".format(whoname, random_greeting))
                            robot.behavior.say_text("{}".format(random_greeting))
                            is_find = True
                            break

        if not is_find:
            for txt in question:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 0

                            print('{} : I\'m fine thank you'.format(whoname))
                            robot.behavior.say_text("I\'m fine thank you")
                            is_find = True
                            break

        if not is_find:
            for txt in var1:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 0
                            reply = random.choice(var2)

                            print('{} : {}'.format(whoname, reply))
                            robot.behavior.say_text("{}".format(reply))
                            is_find = True
                            break

        if not is_find:
            for txt in var3:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 0

                            print('{} : {}'.format(whoname, now.strftime("The time is %H:%M")))
                            robot.behavior.say_text("{}".format(now.strftime("The time is %H:%M")))
                            is_find = True
                            break

        if not is_find:
            for txt in var4:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 0

                            print('{} : I am Vector'.format(whoname))
                            robot.behavior.say_text("{}".format("I am Vector"))
                            is_find = True
                            break

        if not is_find:
            for txt in cmd3:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            jokrep = random.choice(jokes)
                            is_being_anim = True
                            anim_index = 0

                            print('{} : {}'.format(whoname, jokrep))
                            robot.behavior.say_text("{}".format(jokrep))
                            is_find = True
                            break

        if not is_find:
            for txt in cmd6:
                if len(txt) == len(auido_):
                    if txt.find(r.recognize_google(audio)) >= 0:
                        is_find = True
                        robot.behavior.say_text("Ok stop")
                        mixer.music.stop()
                        break

        if not is_find:
            for txt in cmd9:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            is_being_anim = True
                            anim_index = 0
                            re_ = random.choice(repfr9)

                            print('{} : {}'.format(whoname, re_))
                            robot.behavior.say_text("{}".format(re_))
                            is_find = True
                            break

        if not is_find:
            for txt in cmd2:
                if len(txt) == len(auido_):
                    if txt[-3] == auido_[-3]:
                        if txt.find(r.recognize_google(audio)) >= 0:
                            # filename = "sdk_config.ini"
                            # certname1 = "Vector11.cert"
                            # home = str(Path.home())
                            # src = home + '\\' + ".anki_vector" + '\\' #이동할 경로

                            mixer.init()
                            mixer.music.load(
                                "Red Alert 3 Uprising OST - Soviet March 2.mp3")
                            mixer.music.play()
                            is_find = True
                            break

        # if not is_find:
        #     for txt in cmd5:
        #         if len(txt) == len(auido_):
        #             if txt.find(r.recognize_google(audio)) >= 0:
        #                 owm = pyowm.OWM('YOUR_API_KEY')
        #                 observation = owm.weather_at_place('Bangalore, IN')
        #                 observation_list = owm.weather_around_coords(12.972442, 77.580643)
        #                 w = observation.get_weather()
        #                 w.get_wind()
        #                 w.get_humidity()
        #                 w.get_temperature('celsius')
        #                 print(w)
        #                 print(w.get_wind())
        #                 print(w.get_humidity())
        #                 print(w.get_temperature('celsius'))
        #                 engine.say(w.get_wind())
        #                 engine.runAndWait()
        #                 engine.say('humidity')
        #                 engine.runAndWait()
        #                 engine.say(w.get_humidity())
        #                 engine.runAndWait()
        #                 engine.say('temperature')
        #                 engine.runAndWait()
        #                 engine.say(w.get_temperature('celsius'))
        #                 engine.runAndWait()


        if not is_find:
            print("There's no Conversation..")
            robot.behavior.say_text("sorry there's no conversation")

        #else:
            #print("There's no Conversation..")
            #engine.say("please wait")
            #engine.runAndWait()
            #print(wikipedia.summary(r.recognize_google(audio)))
            #engine.say(wikipedia.summary(r.recognize_google(audio)))
            #engine.runAndWait()
            #userInput3 = input("or else search in google")
            #webbrowser.open_new('www.google.com/search?q=' + userInput3)

def stop():
    global robot, n

    n = 1
    print("stop")
    robot.disconnect()

def run():
    global robot, n
    global is_being_anim, anim_index, whoname

    args = anki_vector.util.parse_command_args()
    robot = anki_vector.Robot(args.serial)
    robot.connect()
    is_being_anim = False
    anim_index = 0
    whoname = "Vector"
    n=0

    my_thread = threading.Thread(target=main)
    my_thread2 = threading.Thread(target=anim, args=())
    my_thread3 = threading.Thread(target=rainbowEyes, args=())

    my_thread.start()
    # my_thread2.start()
    # my_thread3.start()

    #main()


if __name__ == '__main__' :
    run()