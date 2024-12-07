import random

class Human:
    def __init__(self, name=None, money=100, glad=50, job=None, car=None, home=None, sat=50):
        self.name = name
        self.money = money
        self.glad = glad
        self.job = job
        self.home = home
        self.car = car
        self.sat = sat

    def get_job(self, job_list):
        self.job = Job(job_list)
        print(f"{self.name} got a job: {self.job.name}. Salary: {self.job.salary}. Responsibilities: {self.job.responsibilities}.")

    def work(self):
        if self.job:
            self.money += self.job.salary
            self.glad -= 10
            print(f"{self.name} worked as a {self.job.name} and earned {self.job.salary}. Money balance: {self.money}. Mood: {self.glad}.")
        else:
            print(f"{self.name} does not have a job!")

    def chill(self):
        self.glad += 20
        self.money -= 10
        print(f"{self.name} is relaxing. Mood: {self.glad}. Money left: {self.money}.")

    def get_car(self, car_list):
        self.car = Car(car_list)
        print(f"{self.name} got a car: {self.car.brand}. Gas level: {self.car.gas}. Condition: {self.car.condition}.")

    def drive(self):
        if self.car:
            if self.car.gas >= self.car.consumption:
                self.car.gas -= self.car.consumption
                self.glad += 5
                print(f"{self.name} drove the car {self.car.brand}. Gas left: {self.car.gas}.")
            else:
                print(f"Not enough gas in the car {self.car.brand}!")
        else:
            print(f"{self.name} does not have a car.")

    def refuel(self):
        if self.car:
            cost = (100 - self.car.gas) * 2
            if self.money >= cost:
                self.money -= cost
                self.car.gas = 100
                print(f"{self.name} refueled the car {self.car.brand}. Gas level: {self.car.gas}. Money left: {self.money}.")
            else:
                print(f"{self.name} does not have enough money to refuel the car.")
        else:
            print(f"{self.name} does not have a car.")

    def repair_car(self):
        if self.car:
            cost = (100 - self.car.condition) * 1.5
            if self.money >= cost:
                self.money -= cost
                self.car.condition = 100
                print(f"{self.name} repaired the car {self.car.brand}. Condition: {self.car.condition}. Money left: {self.money}.")
            else:
                print(f"{self.name} does not have enough money to repair the car.")
        else:
            print(f"{self.name} does not have a car.")

class Job:
    def __init__(self, job_list):
        job_choice = random.choice(list(job_list.keys()))
        self.name = job_choice
        self.salary = job_list[job_choice]["salary"]
        self.responsibilities = job_list[job_choice]["responsibilities"]

class Car:
    def __init__(self, car_list):
        self.brand = random.choice(list(car_list))
        self.gas = car_list[self.brand]["gas"]
        self.condition = car_list[self.brand]["condition"]
        self.consumption = car_list[self.brand]["consumption"]

job_offers = {
    "Programmer": {"salary": 200, "responsibilities": "Developing software"},
    "Driver": {"salary": 100, "responsibilities": "Transporting passengers"},
    "Teacher": {"salary": 150, "responsibilities": "Teaching students"},
    "Manager": {"salary": 180, "responsibilities": "Managing projects"}
}

car_brands = {
    "BMW": {"gas": 100, "condition": 100, "consumption": 6},
    "Lanos": {"gas": 50, "condition": 60, "consumption": 4},
    "Nissan": {"gas": 70, "condition": 120, "consumption": 7},
    "Ferrari": {"gas": 80, "condition": 110, "consumption": 14}
}

human = Human(name="Alex")
human.get_job(job_offers)
human.work()
human.chill()

human.get_car(car_brands)
human.drive()
human.refuel()
human.repair_car()
