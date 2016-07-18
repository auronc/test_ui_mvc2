from PyQt5 import QtCore
from Task import Task


class TestAllThread(QtCore.QThread):

    def __init__(self, model):
        QtCore.QThread.__init__(self)
        self.model = model

    def run(self):
        tasks = ['GPS', 'WIFI', "AUDIO"]

        for task in tasks:
            self.task = Task(self.model, task)
            self.task.start()
            self.task.wait()
