import random
from distutils.command.clean import clean


class Hum:
    def __init__(self,name=None,money = 100 ,glad = 50, job= None, car= None, home=None, sat=50):
        self.name = name
        self.money= money
        self.glad = glad
        self.job = job
        self.home = home
    def g_h(self):
        pass
    def g_c(self):
        pass
    def g_j(self):
        pass
    def eat(self):
        pass
    def work(self):
        pass
    def shopping(self):
        pass
    def chill(self):
        pass
    def rep_c(self):
        pass
    def cleam_h(self):
        pass
b_o_d = {
    "BMV":{"gaz":100,"chp":100,"cons":6},
    "Lanos":{"gaz":50,"chp":60,"cons":4},
    "Nissan":{"gaz":70,"chp":120,"cons":7},
    "Ferrari":{"gaz":80,"chp":110,"cons":14}
}
class Car:
    def __init__(self,brand_list):
        self.brand = random.choice(list(brand_list))
        self.gaz = brand_list[self.brand]["gaz"]
        self.chp = brand_list[self.brand]["chp"]
        self.cons = brand_list[self.brand]["cons"]
brand = Car(b_o_d)