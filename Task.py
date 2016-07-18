from PyQt5 import QtCore
from PyQt5.QtCore import QThread


class Task(QtCore.QThread):

    def __init__(self, model, name):
        QtCore.QThread.__init__(self)
        self.name = name
        self.model = model
        self.running = False

    def msg(self, text):
        self.model.set_message(text)

    def run(self):
        print('start thread:', self.name)
        self.model.running_task_add(self.name, self)
        self.running = True

        try:
            self.msg('RUN(' + self.name + ')')
            QThread.sleep(5)
            self.msg('STOP(' + self.name + ')')

        except Exception as e:
            print('error code: %i', e.returncode)

        self.running = False
        self.model.running_task_remove(self.name)
        print('stop thread:', self.name)

    def stop(self):
        print('try to stop thread:', self.name)
        self.running = False
        self.wait()