class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


    def work(self):
        print("%s started there first day of work." % self.name , "your job is %s" % self.job)


class Programmer(object):
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job


    def code(self):
        print("%s has finally finish his game" % self.name)


person = Employee("Jeff", 23, "food market")
person2 = Programmer("Tom", 34, "Code Company")