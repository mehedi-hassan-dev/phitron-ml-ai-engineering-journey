"""
Problem: Make three classes:
Phone → has model and battery (default 100).

SmartPhone → inherits from Phone and adds operating system.

GamingPhone  → inherits from SmartPhone and adds cooling_system.
 Add a method start_game(name) that prints
   "Playing <name> on <model>".
"""




class Phone:
    def __init__(self, model, battery = 100):
        self.model = model
        self.battery = battery

    def info(self):

        print(f"Phone Model: {self.model}")
        print(f"Battery: {self.battery}%")

class SmartPhone(Phone):

    def __init__(self, model, operating_system, battery = 100):

        super().__init__(model, battery)
        self.operating_system = operating_system

    def show(sef):
        print(f"Operating system: {sef.operating_system}")


class GamingPhone(SmartPhone):

    def __init__(self, model, operating_system, cooling_system, battery = 100):
        super().__init__(model, operating_system, battery)
        self.cooling_system = cooling_system

    def cool_mood(self):
        print(f"Cooling System : {self.cooling_system}")

    def start_game(self, name):
        print(f"Playing {name} On {self.model}")




phon = GamingPhone("Vivo", "Android", "Liquid Cooling")
phon.info()
phon.show()
phon.cool_mood()
phon.start_game('PUBG')

