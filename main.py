# class Std:
#     a_o_s = 0
#     def __init__(self, name = None,  height= 150)  :
#         self.name = name
#         print("I'm", name)
#         Std.a_o_s += 1
#         self.height = height
#
#     def printer(self):
#
#         self.height += 10
#     def __del__(self):
#         print("Ok go+")
#     def __bool__(self):
#         return self.name ==None
#     def __len__(self):
#         return self.height
#         self.height += 10
#
#
#
#
#
# Sviat = Std()
# Bodya = Std(name = "Bodya")
#
#
#
# print("I'm",Bodya.__len__(),"tall")
# Sviat.printer()
# print("I'm",Sviat.__len__(),"tall")
# Sviat.printer()
#
#
# print("There are ",Sviat.a_o_s, "student")


class Student :
    def __init__(self, name = None, age = None)  :
        self.name = name
        self.age = age
        print("Name:", self.name, "Age:", self.age)
def get_info(self):

    print(Sviat)
Sviat = Student(name="Sviat", age=13)
print(Sviat.get_info())

