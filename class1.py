# Class 1 - Famous Electronic Vechile Company

class tesla:
    def __init__(self,m,p):
        self.model = m
        self.price = p


t1 = tesla("Model-3",6000000)
# print("Car Model:",t1.model)
# print("Car Price:",t1.price)

t2 = tesla("Model-S",20000000)
# print("Car Model:",t2.model)
# print("Car Price:",t2.price)


t3 = tesla("Model-X",5000000)
# print("Car Model:",t3.model)
# print("Car Price:",t3.price)


t4 = tesla("Model-Y",15000000)
# print("Car Model:",t4.model)
# print("Car Price:",t4.price)

t5 = tesla("Cybertruck",5000000)
# print("Car Model:",t5.model)
# print("Car Price:",t5.price)

l_tesla = []
l_tesla.append(t1)
l_tesla.append(t2)
l_tesla.append(t3)
l_tesla.append(t4)
l_tesla.append(t5)

for car in l_tesla:
    print(f"Car Model: {car.model}")
    print(f"Price of Car--> {car.price}")