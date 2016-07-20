from TestAllThread import TestAllThread
from TaskBackground import TaskBackground
from TaskListRoot import TaskListRoot

class MainController(object):

    def __init__(self, model):
        self.model = model
        self.task_background = TaskBackground(self.model, 'background')
        self.task_background.start()

    def run_deinit(self):
        self.model.app_closing = True
        self.model.running_task_removeAll()
        self.task_background.stop()

    def run_test(self, test_name):
        if test_name == 'testAll':
            self.test_all = TestAllThread(self.model, 'ALL')
            self.test_all.start()
        else:
            self.task = TaskListRoot(self.model, 'LS')
            self.task.start()
