# Class 2  - Famous IPL Team

class CSK:
    def __init__(self,r,j,nn):
        self.role = r
        self.jerseyno = j
        self.nickname = nn


# print("""Whistle Podu! 
#         CSK 5 times Champions lead by 
#         GOAT Mahi!
#     """)

print(f"Thala For A Reason!!!")

c1 = CSK("Captain",7,"Thala")

# print(f"NickName of player: {c1.nickname}")
# print(f"Role: {c1.role}")
# print(f"Jersey No: {c1.jerseyno}")

# print("  Other Players Info     ")

c2 = CSK("Vice-Captain",3,"Chinna Thala")
# print(f"NickName of player:{c2.nickname}")
# print(f"Role: {c2.role}")
# print(f"Jersey No: {c2.jerseyno}")

c3 = CSK("Allrounder",8,"Cricket Thalapthy")
# print(f"NickName of player:{c3.nickname}")
# print(f"Role: {c3.role}")
# print(f"Jersey No: {c3.jerseyno}")


c4 = CSK("Spin-Bowler",99,"Ashwin Anna")
# print(f"NickName of player:{c4.nickname}")
# print(f"Role: {c4.role}")
# print(f"Jersey No: {c4.jerseyno}")


c5 = CSK("Batsman",9,"Mitchh")

# print(f"NickName of player:{c5.nickname}")
# print(f"Role: {c5.role}")
# print(f"Jersey No: {c5.jerseyno}")


players = []
players.append(c1)
players.append(c2)
players.append(c3)
players.append(c4)
players.append(c5)


for kings in players:
    print(f"Player Nickname: {kings.nickname}")
    print(f"Role of player <--->  *{kings.role}*")