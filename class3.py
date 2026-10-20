# class 3 --> Actor  


class Actors:
    def __init__(self,n,fm):
        self.name = n
        self.favmovie = fm

A1 = Actors("Ranveer Singh","Dhurandhar-2")
# print(A1.name)
# print(A1.favmovie)

A2 = Actors("Ranbeer Kapoor","Animal")
# print(A2.name)
# print(A2.favmovie)


A3 = Actors("Rajnikant","Shivaji The Boss")
# print(A3.name)
# print(A3.favmovie)


A4 = Actors("Sushant Singh Rajput","Chichoore")
# print(A4.name)
# print(A4.favmovie)


A5 = Actors("Allu Arjun","Pushpa-2")
# print(A5.name)
# print(A5.favmovie)

l_actors = []
l_actors.append(A1)
l_actors.append(A2)
l_actors.append(A3)
l_actors.append(A4)
l_actors.append(A5)

for actors in l_actors:
    print(f"Actor Name: {actors.name}")
    print(f"Favourate Movie---> {actors.favmovie}")