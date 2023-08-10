def add(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum

print(add(1,2,3,4,5,6))


def calculate(n, **kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw) -> None:
        self.make = kw.get("make") # you can use 'get' and if there is no value there it will just return none
        self.model = kw.get("model")
        self.color = kw.get("color")
        

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)


def all_aboard(a, *args, **kw): 
    print(a, args, kw)
 
all_aboard(4, 7, 3, 0, x=10, y=64)
