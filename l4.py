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
#
# class Aud:
#     def Audio(self):
#         print("Audio playing")
#
# class Vid:
#     def Video(self):
#         print("Video playing")
#
# class Multi(Aud,Vid):
#     def play(self):
#         super().Video()
#         super().Audio()
#
# pc = Multi()
# pc.play()

class Page:
    def __init__(self, total):
        self.total = total
        self.current = 1

    def show_summary(self):
        if self.current >= 0   and self.current <= 29 :
            print(f"Story: start"
                  f" Pages: {self.current}")
        elif self.current >= 30   and self.current <= 49:
            print(f"Story: tie"
                  f" Pages: {self.current}")
        elif self.current >= 50 and self.current <= 69:
            print(f"Story: middle"
                  f" Pages: {self.current}")
        elif self.current >= 70 and self.current <= 89:
            print(f"Story: climax"
                  f" Pages: {self.current}")
        elif self.current >= 90 and self.current <= 100:
            print(f"Story: end"
                  f" Pages: {self.current}")

class Plot:
    def __init__(self, title):
        self.title = title
        self.summary = "Story starts..."

    def describe(self):
        print(f"{self.title}: {self.summary}")

class Book(Page, Plot):
    def __init__(self, total, title):
        Page.__init__(self, total)
        Plot.__init__(self, title)

    def read(self, pages=1):
        self.current += pages
        if self.current > self.total:
            self.current = self.total
        print(f"Reading {pages} page(s)...")
        self.show_summary()


book = Book(100, "Lorem Ipsum")
book.describe()
book.read(70)


