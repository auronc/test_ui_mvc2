from PyQt5.QtCore import QThread
from Task import Task
import subprocess


class TaskBackground(Task):
    def __init__(self, model, name):
        super().__init__(model, name)

    def run(self):
        self.pre_run(False)

        while self.running:
            self.model.dut_exist = self.check_dut()

            QThread.sleep(1)

        self.post_run(False)

    def check_dut(self):
        cmd = 'adb shell ls /'
        try:
            subprocess.check_output(cmd, shell=True)
            return True
        except Exception as e:
            return False
