# ml = [1 ,2,3]
# iterator = iter(ml)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# class Counter:
#     def __init__(self, maxnum):
#         self.i = 0
#         self.maxnum = maxnum
#     def __iter__(self):
#         self.i = 0
#         return self
#     def __next__(self):
#         if self.i < self.maxnum:
#             self.i += 1
#             return self.i
#         elif self.i >= self.maxnum:
#             raise StopIteration
#         return self.i
# c= Counter(5)
# for elem in c:
#     print(elem)
#
#
# print(c.__next__())
# print(c.__iter__())
# print(next(c))
# print(iter(c))
# print(next(c))

# def raise_to(md,n):
#     i=0
#     for _ in range(md):
#         yield n**i
#         i+=1
# res = raise_to(5,500)
# print(res)
# for _ in res:
#     print(_)



class N:
    def __init__(self, num=0):
        self.current = num
    def __iter__(self):
        return self
    def __next__(self):
        if self.current % 2 != 0:
            self.current += 1
        if self.current > 10:
            raise StopIteration
        result = self.current
        self.current += 2
        return result
even_numbers = N(num=1)

for number in even_numbers:
    print(number)

