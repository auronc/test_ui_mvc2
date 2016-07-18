from TestAllThread import TestAllThread
from TaskBackground import TaskBackground
from Task import Task

class MainController(object):

    def __init__(self, model):
        self.model = model
        self.task_background = TaskBackground(self.model, 'background')
        self.task_background.start()

    def run_deinit(self):
        self.model.running_task_removeAll()
        self.task_background.stop()

    def run_test(self, test_name):
        if test_name == 'testAll':
            self.test_all = TestAllThread(self.model)
            self.test_all.start()
        else:
            self.task = Task(self.model, 'GPS')
            self.task.start()