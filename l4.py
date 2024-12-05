# class Hum:
#     height = 170
#     def __init__(self):
#         self.height = 150
# class Student(Hum):
#     def __init__(self):
#         print(self.height)
#         super().__init__()
#         print(self.height)
#     pass
# class Worker(Hum):
#     pass
#
# nick = Student()



# class Shape:
#     def __init__(self):
#
#         self.color = "black"
#     def area(self):
#         pass
# class Circle(Shape):
#
#     def __init__(self,rad=10,):
#         super().__init__()
#
#
#         self.rad=rad
#     def areaa(self):
#         return 3.14*self.rad **2
#
#
# lorem = Circle(10)
# print(lorem.areaa())
# print(lorem.rad)
# class Cpu:
#     def Audio(self):
#         self.b = print("A. playing")
#
# class Gpu:
#     def Video(self):
#         self.a = print("V. playing")
#
# class Multi(Gpu,Cpu):
#     def play(self):
#         super().Video()
#         super().Audio()
#         print(self.a,self.b)
#
# pc = Multi()
# pc.play()

class Aud:
    def Audio(self):
        print("Audio playing")

class Vid:
    def Video(self):
        print("Video playing")

class Multi(Aud,Vid):
    def play(self):
        super().Video()
        super().Audio()

pc = Multi()
pc.play()

