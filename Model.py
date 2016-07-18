
class Model(object):

    def __init__(self):
        self.__update_funcs = []
        self.__message = ''

        self.__dut_exist = False
        self.__running_tasks = {}

    def running_task_add(self, task_name, task):
        self.__running_tasks[task_name] = task

    def running_task_remove(self, task_name):
        self.__running_tasks.pop(task_name, None)

    def running_task_removeAll(self):
        l = list(self.__running_tasks)
        for name in l:
            self.__running_tasks[name].stop()

    def pick_message(self):
        msg = self.__message
        self.__message = ''
        return msg

    def set_message(self, msg):
        self.__message = msg
        self.announce_update()

    def is_dut_exist(self):
        return self.__dut_exist

    def set_dut_status(self, exist_status):
        self.__dut_exist = exist_status
        self.announce_update()

    def is_testing(self):
        number = len(self.__running_tasks)
        testing = True if number > 0 else False
        return testing

    def subscribe_update_func(self, func):
        if func not in self.__update_funcs:
            self.__update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self.__update_funcs:
            self.__update_funcs.remove(func)

    def announce_update(self):
        for func in self.__update_funcs:
            func()
