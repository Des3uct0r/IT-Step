
class Cat :
    def __init__(self, name , age, color, eyec) :
        self.name = name
        self.age = age
        self.color = color
        self.eyec = eyec
        print("Nice, your cat is ",self.name, " he is ", self.age, " years old, his color is ", self.color, " and his eyes color is ", self.eyec  )

cname = str(input("What is name of the cat?"))
cage = int(input("What age is cats age?"))
ccolor = str(input("What is color of cat? "))
ceyec = str(input("What is color of cats eyes?"))

ccat = Cat(name = cname , age = cage , color = ccolor , eyec = ceyec)