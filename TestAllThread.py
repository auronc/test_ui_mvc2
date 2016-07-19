from Task import Task


class TestAllThread(Task):
    def __init__(self, model, name):
        super().__init__(model, name)

    def no_dut_or_app_is_closing(self):
        abort = True if not self.model.dut_exist or self.model.app_closing else False
        return abort

    def run(self):
        print('start thread:', self.name)
        self.running = True

        tasks = ['GPS', 'WIFI', "AUDIO"]

        for task_name in tasks:
            if self.no_dut_or_app_is_closing():
                break

            self.task = Task(self.model, task_name)
            self.task.start()
            self.task.wait()

        self.running = False
        print('stop thread:', self.name)
