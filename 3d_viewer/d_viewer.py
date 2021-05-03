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
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""3d Viewer example, with remote control.

This is an example of how you can use the 3D viewer with a program, and the
3D Viewer and controls will work automatically.
"""
import multiprocessing
import time

import anki_vector

def main():
    global robot
    global n
    n=0

    args = anki_vector.util.parse_command_args()
    with anki_vector.Robot(args.serial,
                           show_viewer=True,
                           show_3d_viewer=True,
                           enable_face_detection=True,
                           enable_custom_object_detection=True,
                           enable_nav_map_feed=True)  as robot :
        print("Starting 3D Viewer. Use Ctrl+C to quit.")
        try:
            robot.conn.request_control()
            robot.conn.release_control()
            while True:
                while True:
                    if n == 1:
                        print("break")
                        break
                time.sleep(0.5)

        except KeyboardInterrupt:
            pass

def stop():
    global robot
    global n
    n=1

def run():
    print("3424")
    multiprocessing.freeze_support()
    main()

if __name__ == "__main__":
    run()
