# Tea shop class


class Tea_shop:
    def __init__(self,n,tp):
        self.name = n
        self.tea_price = tp

T1 = Tea_shop("ChaiGpt",15)
# print(T1.name)
# print(T1.tea_price)



T2 = Tea_shop("Graduate Chai",12)
# print(T2.name)
# print(T2.tea_price)


T3 = Tea_shop("Amrutalaya",10)
# print(T3.name)
# print(T3.tea_price)


T4 = Tea_shop("ChaiVerse",20)
# print(T4.name)
# print(T4.tea_price)

T5 = Tea_shop("Kadak Chai",15)
# print(T5.name)
# print(T5.tea_price)


l_tshop = []
l_tshop.append(T1)
l_tshop.append(T2)
l_tshop.append(T3)
l_tshop.append(T4)
l_tshop.append(T5)

for shop in l_tshop:
    print(f"Shop Name:{shop.name}")
    print(f"Tea Price--> ${shop.tea_price}")