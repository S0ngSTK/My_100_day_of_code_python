import random
def add(*args):
    result=0
    for number in args:
        result+= number
    return result
ran = random.randint(1,100)
# print(add(ran,ran,ran,ran))

def calculator(**kwargs):
    print(kwargs)

# calculator(add=5,mam=10)

class Car:
    def __init__(self,**Name):
        self.model = Name.get('model')
        self.make = Name.get('make')

my_car = Car(make='MMM')
print(my_car.make)