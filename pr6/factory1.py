class WindowFactory:
    @classmethod
    def create_window(cls, name):
        return cls.Window(name)
    @classmethod
    def create_button(cls, name):
        return cls.Button(name)
class MacOsFactory(WindowFactory):
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = ''
            self.style = 'Mac Os window style'
        def add_button(self, btn):
            self.button+=(str(btn.name))+' '+str(btn.style)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Apple hater button style'
class LinuxFactory(WindowFactory):
    class Window:
        def __init__(self, name):
            self.name = name
            self.button = ''
            self.style = 'Kali hacker style'
        def add_button(self, btn):
            self.button+=(str(btn.name))+' '+str(btn.style)
        def show(self):
            print( '{} - {} and {}'.format(self.name, self.style, self.button))
    class Button:
        def __init__(self, name):
            self.name = name
            self.style = 'Kali button style'
def create_dialog(factory):
    wind = factory.create_window('Form1')
    button = factory.create_button('Button1')
    wind.add_button(button)
    return wind
linux = create_dialog(LinuxFactory)
linux.show()
ms=create_dialog(MacOsFactory)
ms.show()