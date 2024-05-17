class Mediator:
    def __init__(self):
        self.colleague1 = Colleague1(self)
        self.colleague2 = Colleague2(self)

    def notify(self, sender, event):
        if sender == self.colleague1:
            print("Colleague1 отправил событие:", event)
            self.colleague2.handle_event(event)
        elif sender == self.colleague2:
            print("Colleague2 отправил событие:", event)
            self.colleague1.handle_event(event)

class Colleague1:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_event(self, event):
        self.mediator.notify(self, event)

    def handle_event(self, event):
        print("Colleague1 обработал событие:", event)

class Colleague2:
    def __init__(self, mediator):
        self.mediator = mediator

    def send_event(self, event):
        self.mediator.notify(self, event)

    def handle_event(self, event):
        print("Colleague2 обработал событие:", event)

# Использование
mediator = Mediator()
mediator.colleague1.send_event("Событие от Colleague1")
mediator.colleague2.send_event("Событие от Colleague2")
