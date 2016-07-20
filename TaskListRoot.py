from Task import Task
import subprocess


class TaskListRoot(Task):

    def __init__(self, model, name):
        super().__init__(model, name)

    def run(self):
        print('start thread:', self.name)
        self.model.running_task_add(self.name, self)
        self.running = True

        try:
            self.msg('RUN(' + self.name + ')')

            cmd = 'adb shell ls /'
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")
            self.msg(output)

            self.msg('STOP(' + self.name + ')')

        except Exception as e:
            print('ERROR:', e)

        self.running = False
        self.model.running_task_remove(self.name)
        print('stop thread:', self.name)
