from PyQt5 import QtCore
from PyQt5.QtCore import QThread


class Task(QtCore.QThread):

    def __init__(self, model, name):
        QtCore.QThread.__init__(self)
        self.name = name
        self.model = model
        self.running = False
        self.task_result = False

    def msg(self, text):
        self.model.message = text

    def stop(self):
        print('try to stop thread:', self.name)
        self.running = False
        self.wait()

    def pre_run(self, add_to_tasks=True):
        print('start thread:', self.name)
        self.running = True
        if add_to_tasks:
            self.model.running_task_add(self.name, self)

    def post_run(self, remove_from_tasks=True):
        print('stop thread:', self.name)
        self.running = False
        if remove_from_tasks:
            self.model.running_task_remove(self.name)

    def run(self):
        self.pre_run()
        try:
            self.msg('RUN(' + self.name + ')')

            QThread.sleep(5)

            self.msg('STOP(' + self.name + '), Result= ' + str(self.task_result))
        except Exception as e:
            print('ERROR:', e)
        self.post_run()
