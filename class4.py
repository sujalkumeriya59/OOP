# Famous Reality Show on Telivision


class Reality_show:
    def __init__(self,n,h):
        self.name = n
        self.host = h

R1 = Reality_show("India's Got Latent","Samay Raina")
# print(R1.name)
# print(R1.host)


R2 = Reality_show("KBC","Amitabh Bacchan")
# print(R2.name)
# print(R2.host)


R3 = Reality_show("BigBoss","Salamn Khan")
# print(R3.name)
# print(R3.host)


R4 = Reality_show("Khatraon ke Khiladi","Rohit Shetty")
# print(R4.name)
# print(R4.host)

R5 = Reality_show("Comedy Nights with Kapil","Kapil Sharma")
# print(R5.name)
# print(R5.host)


l_show = []
l_show.append(R1)
l_show.append(R2)
l_show.append(R3)
l_show.append(R4)
l_show.append(R5)


for real_show in l_show:
    print(f"Reality Show name: {real_show.name}")
    print(f"Host name--> {real_show.host}")