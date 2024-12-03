class Human:
    def __init__(self,name):
        self.name = name
class Car:
    def __init__(self,brand):
        self.brand = brand
        self.passangers = []
    def add_pas(self,*args):
        for pas in args:
            self.passangers.append(pas)
    def p_p_n(self):
        if self.passangers != []:
            print(f'Name of {self.brand} passangers:')
            for pas in self.passangers:
                print(pas.name)
        else:
            print(f"There are no passangers in {self.brand}")
gordon = Human("Gordon")
Jake = Human("Jake")
alyx = Human("Alyx")
dr_cliener = Human("Doctor Cliener")
car = Car("Lanos")

car.add_pas(alyx, gordon , Jake, dr_cliener)
car.p_p_n()