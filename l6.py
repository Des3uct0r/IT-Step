# try:
#     print("start")
#     print(error)
#     print("end")
# except :
#     print("p error")
# print("work")

# try:
#     print("start")
#     print(10/0)
#     print("end")
# except NameError:
#     print("p error")
# except (ZeroDivisionError, NameError):
#     print("p error")
# else:
#     print("no p")
# print("work")

# try:
#     print("start")
#     print("10/0")
#     print("end")
# except NameError:
#     print("p error")
# except (ZeroDivisionError, NameError):
#     print("p error")
# else:
#     print("no p")
# finally:
#     print("f")
# print("work")

# def chekck(var1=None):
#     if type(var1)!= str:
#         raise TypeError(f"Sorry {type(var1)} isnt str")
#     else :
#         return var1
# num = 123
# chekck(num)

# class Bu(Exception):
#     def __str__(self):
#         return f"Build error"
# def chm(aom,lim):
#     if aom > lim:
#         print("Enough of materials")
#     else :
#         raise Bu(aom)
# mate= 123
# chm(mate, 300)

# class dil(Exception):
#     def __str__(self):
#         return f"Cant / on 0"
# def chm(fn = 0,sn = 0):
#     if  sn == 0:
#         raise dil(sn)
#     else :
#         print(fn / sn)
#
# fn= input("write first num")
# sn= input("write second num")
# chm(fn, sn)
# try :
#     fn = int(input("Fn"))
#     sn =int(input("sn"))
#     res = fn / sn
#     print(res)
# except ZeroDivisionError:
#     print("Error")


# w = ["1", "2", "3"]
# try:
#
#     i = int(input("Index: "))
#     if 0 <= i < len(w):
#         print(w[i])
#     else:
#
#         raise TypeError(f"No index")
# except ValueError:
#     print("Not number")

import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter("always", ImportWarning)
#
#
# warnings.warn("no cade", SyntaxWarning)
# warnings.warn("2no cade", ImportWarning)

result = []


def divider(a, b):
    if a < b:
        raise ValueError("The A cannot smaller than the B.")
    if b > 100:
        raise IndexError("The B cannot be bigger than 100.")
    return a / b


data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(int(key), int(value))
        result.append(res)
    except Exception:
        print(f"Error occurred: {Exception}")

print(result)

