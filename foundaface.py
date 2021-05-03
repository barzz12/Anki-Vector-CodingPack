import datetime
import time
from anki_vector.util import degrees
from anki_vector.behavior import MIN_HEAD_ANGLE, MAX_HEAD_ANGLE
import random
import threading

import anki_vector
import time


class FoundAFace:
    last_called = datetime.datetime.now()
    functionList = []
    namesCalledOut = []
    waitToStart = 40 # seconds
    noShoutOutToSamePersonFor = 300 # seconds


    def weightedList(self):
        return [
            [self.sayName,8],
            [self.sayBeautiful,2],
            [self.saySoGoodToSeeYou,3]
        ]

    def __init__(self):
        self.functionList = self.randomizeListWithWeight(self.weightedList())

    def takeAction(self,robot,name):
        timeDifference = datetime.datetime.now().timestamp() - self.last_called.timestamp()
        
        # don't perform this before x seconds from startup or the last time it was called
        # if timeDifference < self.waitToStart:
        #     return
        
        # if vector has called out someone, don't call out again, unless its been over x seconds
        #if name not in self.namesCalledOut or timeDifference > self.noShoutOutToSamePersonFor:
        if name not in self.namesCalledOut :
            print("Vector is sending a shoutout to %s" % str(name))
            func = self.chooseRandomFunction(self.functionList)#리스트에 있는 함수들중 하나를 뽑음
            self.functionList = self.reducedFunctionList(self.functionList,func,self)#뽑은 함수를 제외한 리스트를 새로 재저장
            #self.last_called = datetime.datetime.now()
            self.namesCalledOut.append(name)
            print("??")
            (func)(robot,name)

    
    def sayName(self,robot,name):
        robot.conn.request_control(timeout=5.0)
        robot.behavior.say_text("%s! It's me! Vector!" % name).result()
        robot.conn.release_control()

    def sayBeautiful(self,robot,name):
        robot.conn.request_control(timeout=5.0)
        robot.behavior.say_text("%s?" % name).result()
        robot.behavior.set_head_angle(MIN_HEAD_ANGLE)
        robot.behavior.say_text("I think you are?").result()
        time.sleep(0.5)
        robot.behavior.set_head_angle(degrees(35))
        robot.behavior.say_text("beautiful!").result()
        time.sleep(1.0)
        robot.conn.release_control()
    
    def saySoGoodToSeeYou(self,robot,name):
        robot.conn.request_control(timeout=5.0)
        robot.anim.play_animation('anim_knowledgegraph_success_01')
        robot.behavior.say_text("%s! I'm so glad to be your friend!" % name).result()
        robot.anim.play_animation('anim_fistbump_success_01').result()
        robot.conn.release_control()

    def randomizeListWithWeight(self,list):
        # list is a list with an item and a weight for that item
        # it returns a list of the items with the number of items in the newlist determined by the weight
        newList = []
        for item in list:
            func = item[0]
            repeat = item[1]
            for x in range(0, repeat):
                newList.append(func)
        return newList

    def chooseRandomFunction(self,list):
        x = random.randrange(0,len(list))
        return list[x]

    def reducedFunctionList(self,functionList,func,super):
        newList = []
        for listItem in functionList:
            if listItem != func:
                newList.append(listItem)
        if len(newList):
            return newList
        else:
            return self.randomizeListWithWeight(super.weightedList())


FoundAFace = FoundAFace()
i = 0

from anki_vector.util import degrees, distance_mm, speed_mmps
from anki_vector.events import Events


class Status:
    is_on_charger = False
    show_is_on_charger = True
    show_are_motors_moving = False


def main():
    def on_robot_observed_face(robot, event_type, event, evt):
        global i
        print("face {}".format(i))
        i += 1
        if event.name:
            FoundAFace.takeAction(robot, event.name)

    def on_robot_state(robot, event_type, event, evt):
        global Status, i

        if robot.status.is_on_charger & Status.show_is_on_charger:
            if Status.is_on_charger != True:
                print("Vector is currently on the charger.")
                # robot.conn.request_control(timeout=5.0)
                # robot.behavior.set_eye_color(0, 0)
                # robot.say_text("On the charger!")
                # robot.conn.release_control()
                Status.is_on_charger = True
        else:
            if Status.is_on_charger != False:
                print("Vector is running off battery power.")
                Status.is_on_charger = False

        if robot.status.are_motors_moving:
            # print("Vector is on the move. [{}]".format(i))
            pass

    # Start the an async connection with the robot
    with anki_vector.AsyncRobot(enable_face_detection=True, show_viewer=True) as robot:
        # robot.conn.CONTROL_PRIORITY_LEVEL = 1
        robot.conn.request_control(timeout=5.0)
        robot.behavior.say_text("Vector+ 1.0").result()
        # robot.conn.release_control()
        # FoundAFace.takeAction(robot,"jason")

        evt = threading.Event()
        # on_robot_observed_face = functools.partial(on_robot_observed_face, robot)
        robot.events.subscribe(on_robot_observed_face, Events.robot_observed_face, evt)

        # on_robot_state = functools.partial(on_robot_state, robot)
        robot.events.subscribe(on_robot_state, Events.robot_state, evt)

        while True:
            time.sleep(20)
            # robot.conn.request_control(timeout=5.0)
            # time.sleep(0.1)
            # robot.behavior.say_text("Vector+ 1.0").result()
            # robot.conn.release_control()


if __name__ == "__main__":
    main()