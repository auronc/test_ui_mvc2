from Task import Task
import subprocess


class TaskListRoot(Task):

    def __init__(self, model, name):
        super().__init__(model, name)

    def run(self):
        self.pre_run()
        try:
            self.msg('RUN(' + self.name + ')')

            cmd = 'adb shell ls /'
            output = subprocess.check_output(cmd, shell=True).decode("utf-8")
            self.msg(output)

            self.msg('STOP(' + self.name + ')')
        except Exception as e:
            print('ERROR:', e)
        self.post_run()
