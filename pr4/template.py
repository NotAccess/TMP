from abc import ABC, abstractmethod
import sys

class algorithm(ABC):
    def work(self):
        self.mandatory_step()
        self.first_step()
        self.second_step()
        self.optional_step()
    def mandatory_step(self):
        this_method_name = sys._getframe().f_code.co_name
        print("{}.{}".format(self.__class__.__name__, this_method_name))
    @abstractmethod
    def first_step(self):pass
    @abstractmethod
    def second_step(self):pass
    def optional_step(self):
        print('Work is done')
class algA(algorithm):
    def first_step(self):
        print ('Work with algA, step1')
    def second_step(self):
        print('Work with algA, step2')
class algB(algorithm):
    def first_step(self):
        print ('Work with algB, step1')
    def second_step(self):
        print('Work with algB, step2')
    def optional_step(self):
        print('Work by proc B never ends!')
a=algA()
a.work()
b=algB()
b.work()