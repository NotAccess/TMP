class Service:
    def __init__(self, dependency):
        self.dependency = dependency

    def do_something(self):
        self.dependency.do_stuff()

class Dependency:
    def __init__(self,task) -> None:
        self.task=task
    def do_stuff(self):
        print(self.task)

log_dependency = Dependency('Печать логов')
service = Service(log_dependency)
service.do_something()
work_dependency= Dependency('Работа')
service2=Service(work_dependency)
service2.do_something()
