from abc import ABC, abstractmethod
def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r
class Strategy(ABC):
    @abstractmethod
    def work(self,mass):
        pass
class Context:
    strategy: Strategy
    def chooseStrategy(self,strategy: Strategy = None):
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Base()
    def do_work(self,mass):
        print(self.strategy.work(mass))
class TextStrategy(Strategy):
    def work(self, mass:str):
        return mass,sum(bytearray(mass,'utf-8'))
class Base(Strategy):
    def work(self, mass:list):
        return mass,sum_digits(mass)
procA=Context()
procB=Context()

procA.chooseStrategy(TextStrategy())
procB.chooseStrategy()

procA.do_work('123')
procB.do_work(123)

