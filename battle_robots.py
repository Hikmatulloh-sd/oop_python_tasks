from random import randint

class Robot:
    def __init__(self,name,attack_power,health=100):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    # Атакуем противника )
    def attack(self,opponent):
        self.attack_power += randint(2,8) # Увеличиваем силу рандомно при каждом атаке 
        opponent.health -= self.attack_power
        # Информатция об атаке 
        print(f"{self.name} Атаковал {opponent.name} с ущербам -{self.attack_power}")
        print(f"Здаровья {opponent.name} {opponent.health}\n")

    def is_defated(self):
        return True if self.health <= 0 else False


optimus_praim = Robot("Optimus Praim",5,)
alfa_trion = Robot("Alfa Trion",5)

while True:
    alfa_trion.attack(optimus_praim)
    if optimus_praim.is_defated():
        break

    optimus_praim.attack(alfa_trion)
    if alfa_trion.is_defated():
        break
    
if optimus_praim.is_defated():
    print(alfa_trion.name,"победил")
else:
    print(optimus_praim.name,"победил")