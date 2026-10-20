"""
Problem: Make a class MobilePhone with:
model (public)

__battery (private, default 100)
 Add methods:

use() → reduce battery

charge() → increase battery (max 100)

get_battery() → show battery

Show that you can’t access __battery directly.

"""



class MobilePhone:
    def __init__(self, model, battery=100):
        self.model = model
        self.__battery = battery

        print(f"Phone Model: {self.model} ")

    def use(self):

        if self.__battery > 0:
            self.__battery -= 10
        else:
            print("Battery is already Empty")

    def charge(self):

        if self.__battery < 100:
            self.__battery += 10
        else:
            print("Battey is full ")

    def get_battery(self):
        return self.__battery


phon = MobilePhone("Iphone")
print(phon.get_battery())

phon.use()
print(phon.get_battery())

phon.use()
print(phon.get_battery())


phon.charge()
print(phon.get_battery())

