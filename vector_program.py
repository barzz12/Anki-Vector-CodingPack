import json
import os
import threading
from pathlib import Path

from IPython.external.qt_for_kernel import QtCore

import hateTouch, text_screen, play_audio, show_photo, camera, pingpong, eyeGame
import remote_control, command_change, Chatbot, accel_balancing

import anki_vector
import random
from anki_vector.events import Events
from anki_vector.user_intent import UserIntent, UserIntentEvent
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QMainWindow, QDesktopWidget, qApp, QAction, \
    QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon

class ThreadClass(QtCore.QThread):
    def __init__(self, parent = None):
        super(ThreadClass,self).__init__(parent)
    def run(self):
        pass

class MyApp(QMainWindow):

    hate = hateTouch.HateTouch()

    def __init__(self):
        super().__init__()
        #self.threadclass = ThreadClass()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setWindowTitle('ANKI Vector SDK Coding')
        #self.move(300, 300) #위젯을 스크린의 x=300px, y=300px의 위치로 이동시킵니다.
        #self.resize(400, 200)#위젯의 크기를 너비 400px, 높이 200px로 조절합니다.

        self.setWindowIcon(QIcon('vector.ico'))
        #self.setGeometry(0, 0, 600, 600)#창의 위치와 크기를 설정합니다. 앞의 두 매개변수는 창의 x, y 위치를 결정하고, 뒤의 두 매개변수는 각각 창의 너비와 높이를 결정합니다.
        self.setFixedSize(600, 620)

        label1 = QLabel('1. 벡터 얼굴 글씨 띄우기', self)
        label1.resize(230,30)
        label1.move(10, 45)
        label1.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label2 = QLabel('2. 벡터 만지거나 들지마', self)
        label2.resize(230,30)
        label2.move(10, 85)
        label2.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label3 = QLabel('3. 벡터 음악 재생', self)
        label3.resize(230, 30)
        label3.move(10, 125)
        label3.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label4 = QLabel('4. 벡터 찍은 사진 보기', self)
        label4.resize(230, 30)
        label4.move(10, 165)
        label4.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label5 = QLabel('5. 벡터 화면 카메라 띄우기', self)
        label5.resize(230, 30)
        label5.move(10, 205)
        label5.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label6 = QLabel('6. 벡터 채팅봇 beta', self)
        label6.resize(230, 30)
        label6.move(10, 245)
        label6.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label7 = QLabel('7. 벡터 명령응답 조작', self)
        label7.resize(230, 30)
        label7.move(10, 285)
        label7.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label8 = QLabel('8. 벡터 직접 조종', self)
        label8.resize(230, 30)
        label8.move(10, 325)
        label8.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label9 = QLabel('9. 벡터 핑퐁', self)
        label9.resize(230, 30)
        label9.move(10, 365)
        label9.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label10 = QLabel('10. 벡터 눈색깔 맞추기', self)
        label10.resize(230, 30)
        label10.move(10, 405)
        label10.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        label11 = QLabel('11. 벡터 수평 유지', self)
        label11.resize(230, 30)
        label11.move(10, 445)
        label11.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        # label12 = QLabel('12. 벡터 지형 뷰어', self)
        # label12.resize(230, 30)
        # label12.move(10, 485)
        # label12.setStyleSheet("background-color:#DDDDDD;color:green;font-size:15px;font-weight:bold")

        #========================================================================

        btn1 = QPushButton('시작', self)
        btn1.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn1.move(250, 45)
        btn1.resize(50,30)
        btn1.clicked.connect(text_screen.run)

        btn2 = QPushButton('시작', self)
        btn2.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn2.move(250, 85)
        btn2.resize(50,30)
        btn2.clicked.connect(lambda : self.btn2_isClicked(True))

        btn2_ = QPushButton('종료', self)
        btn2_.move(310, 85)
        btn2_.resize(50,30)
        btn2_.clicked.connect(lambda : self.btn2_isClicked(False))

        btn3 = QPushButton('시작', self)
        btn3.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn3.move(250, 125)
        btn3.resize(50, 30)
        btn3.clicked.connect(lambda : self.btn3_isClicked(True))

        btn3_ = QPushButton('종료', self)
        btn3_.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn3_.move(310, 125)
        btn3_.resize(50, 30)
        btn3_.clicked.connect(lambda : self.btn3_isClicked(False))

        btn4 = QPushButton('시작', self)
        btn4.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn4.move(250, 165)
        btn4.resize(50, 30)
        btn4.clicked.connect(show_photo.main)

        btn5 = QPushButton('시작', self)
        btn5.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn5.move(250, 205)
        btn5.resize(50, 30)
        btn5.clicked.connect(lambda : self.btn5_isClicked(True))

        btn5_ = QPushButton('종료', self)
        btn5_.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn5_.move(310, 205)
        btn5_.resize(50, 30)
        btn5_.clicked.connect(lambda : self.btn5_isClicked(False))

        btn6 = QPushButton('시작', self)
        btn6.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn6.move(250, 245)
        btn6.resize(50, 30)
        btn6.clicked.connect(lambda : self.btn6_isClicked(True))

        btn6_ = QPushButton('종료', self)
        btn6_.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn6_.move(310, 245)
        btn6_.resize(50, 30)
        btn6_.clicked.connect(lambda : self.btn6_isClicked(False))

        btn7 = QPushButton('시작', self)
        btn7.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn7.move(250, 285)
        btn7.resize(50, 30)
        btn7.clicked.connect(lambda : self.btn7_isClicked(True))

        btn7_ = QPushButton('종료', self)
        btn7_.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn7_.move(310, 285)
        btn7_.resize(50, 30)
        btn7_.clicked.connect(lambda : self.btn7_isClicked(False))

        btn8 = QPushButton('시작', self)
        btn8.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn8.move(250, 325)
        btn8.resize(50, 30)
        btn8.clicked.connect(remote_control.run)

        btn9 = QPushButton('시작', self)
        btn9.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn9.move(250, 365)
        btn9.resize(50, 30)
        btn9.clicked.connect(pingpong.main)

        btn10 = QPushButton('시작', self)
        btn10.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn10.move(250, 405)
        btn10.resize(50, 30)
        btn10.clicked.connect(eyeGame.main)

        btn11 = QPushButton('시작', self)
        btn11.setToolTip('벡터가 <b>text.txt</b>에 써져있는 대사를 합니다.')
        btn11.move(250, 445)
        btn11.resize(50, 30)
        btn11.clicked.connect(accel_balancing.main)


        self.statusBar().reformat()
        self.statusBar().setStyleSheet("color: red; background-color: yellow; font-size:25px;font-weight:bold")
        self.statusBar().showMessage('벡터 자율행동중..')

        exitAction = QAction(QIcon('exit.png'), 'Exit', self)#객체 저장
        exitAction.setShortcut('Ctrl+Q')#단축키
        exitAction.setStatusTip('Exit application')#상태 팁
        exitAction.triggered.connect(qApp.quit)#생성된(triggered) 시그널이 QApplication 위젯의 quit() 메서드에 연결되고, 어플리케이션을 종료시키게 됩니다.

        menubar = self.menuBar()#menuBar() 메서드는 메뉴바를 생성합니다. 이어서 ‘File’ 메뉴를 하나 만들고, 거기에 ‘exitAction’ 동작을 추가합니다.
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')#‘&File’의 앰퍼샌드(ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다. ‘F’ 앞에 앰퍼샌드가 있으므로 ‘Alt+F’가 File 메뉴의 단축키가 됩니다. 만약 ‘i’의 앞에 앰퍼샌드를 넣으면 ‘Alt+I’가 단축키가 됩니다.
        fileMenu.addAction(exitAction)

        self.center()#화면 가운데로
        self.show()


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def btn2_isClicked(self, bool):
        if bool:
            self.statusBar().showMessage('벡터 2번 명령 수행중..')
            self.hate.run()
        else :
            self.statusBar().showMessage('벡터 자율행동중..')
            self.hate.stop()

    def btn3_isClicked(self, bool):
        if bool:
            self.statusBar().showMessage('벡터 3번 명령 수행중..')
            play_audio.run()
        else :
            self.statusBar().showMessage('벡터 자율행동중..')
            play_audio.stop()

    def btn5_isClicked(self, bool):
        if bool:
            self.statusBar().showMessage('벡터 5번 명령 수행중..')
            camera.run()
        else :
            self.statusBar().showMessage('벡터 자율행동중..')
            camera.stop()

    def btn6_isClicked(self, bool):
        if bool:
            self.statusBar().showMessage('벡터 6번 명령 수행중..')
            Chatbot.run()
        else :
            self.statusBar().showMessage('벡터 자율행동중..')
            Chatbot.stop()

    def btn7_isClicked(self, bool):
        if bool:
            self.statusBar().showMessage('벡터 7번 명령 수행중..')
            command_change.run()
        else :
            self.statusBar().showMessage('벡터 자율행동중..')
            command_change.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())