# Базовый компонент
class Component:
    def operation(self):
        pass

# Лист (лист дерева)
class Leaf(Component):
    def __init__(self,task) -> None:
        self.task=task
    def operation(self):
        print(f"Leaf:{self.task}")

# Контейнер (узел дерева)
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print("Composite: Выполнение операции")
        for child in self.children:
            child.operation()

# Использование компоновщика
leaf1 = Leaf('Работа с вордом')
leaf2 = Leaf('Работа с 1С')
leaf3 = Leaf('Работа с PostgreSQL')
composite = Composite()

composite.add(leaf1)
composite.add(leaf2)
composite.add(leaf3)

composite.operation()
