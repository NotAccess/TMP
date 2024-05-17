class Pizza:
    def __init__(self, builder):
        self.size = builder.size
        self.cheese = builder.cheese
        self.pepperoni = builder.pepperoni
        self.mushrooms = builder.mushrooms

    def __str__(self):
        return f"Pizza: size={self.size}, cheese={self.cheese}, pepperoni={self.pepperoni}, mushrooms={self.mushrooms}"

class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False

    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def build(self):
        return Pizza(self)

# Использование
pizza_peperoni = PizzaBuilder(12).add_cheese().add_pepperoni().build()
print(pizza_peperoni)
pizza_ot_chief=PizzaBuilder(30).add_cheese().add_mushrooms().add_pepperoni().build()
print(pizza_ot_chief)
