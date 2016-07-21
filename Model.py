
class Model(object):

    def __init__(self):
        self.__update_funcs = []
        self.__message = ''

        self.__app_closing = False
        self.__dut_exist = False
        self.__running_tasks = {}

        self.__ui_sender = None
        self.__test_result = ()

    def running_task_add(self, task_name, task):
        self.__running_tasks[task_name] = task

    def running_task_remove(self, task_name):
        self.__running_tasks.pop(task_name, None)

    def running_task_removeAll(self):
        l = list(self.__running_tasks)
        for name in l:
            self.__running_tasks[name].stop()

    @property
    def app_closing(self):
        return self.__app_closing

    @app_closing.setter
    def app_closing(self, value):
        self.__app_closing = value

    def pick_message(self):
        msg = self.__message
        self.__message = ''
        return msg

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, msg):
        self.__message = msg
        self.announce_update()

    @property
    def dut_exist(self):
        return self.__dut_exist

    @dut_exist.setter
    def dut_exist(self, exist_status):
        self.__dut_exist = exist_status
        self.announce_update()

    def is_testing(self):
        number = len(self.__running_tasks)
        testing = True if number > 0 else False
        return testing

    def prepare_test(self, sender):
        self.__ui_sender = sender

    def set_test_result(self, is_pass, note):
        self.__test_result = self.__ui_sender, is_pass, note

    def pick_test_result(self):
        result = self.__test_result
        self.__test_result = ()
        return result

    def subscribe_update_func(self, func):
        if func not in self.__update_funcs:
            self.__update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self.__update_funcs:
            self.__update_funcs.remove(func)

    def announce_update(self):
        for func in self.__update_funcs:
            func()
