import datetime


class ParentClass(object):
    def __init__(self):
        pass

    def class_function(self, value):
        print("checking wether class_function has been executed",  value)

    def now(self):
        print(datetime.datetime.now())

    def override_class(self):
        print("parent class override_class def is executed")

class ChildClass(ParentClass):
    def __init__(self):
        pass
    def override_class(self):
        print("Child class override is executed")

    def override_test(self):
        self.override_class()
        super(ChildClass, self).override_class()

parent_call = ParentClass()
child_call = ChildClass()

child_call.override_test()
