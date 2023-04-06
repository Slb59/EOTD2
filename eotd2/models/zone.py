import random
from eotd2.models import Zombis
from .district import District
from .track import Track

class ActivationZone:
    def __init__(self) -> None:
        self.statut = 0 # 0 if inactif, 1 if activate zone
        
    @property    
    def state(self):
        return 'Active' if self.statut else 'Inactive'

class TownPlace(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.petrol_die = None
        self.health_die = None
        self.luck_die = None

    def __str__(self) -> str:
        result = f"En ville ({self.state}): carburant={self.petrol_die}, "
        result += f"santé={self.health_die}, chance={self.luck_die}"
        return result

class ExterminationZone(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.zombis = []
        self.dice = []
        self.zombis_spots = Zombis()

    def __str__(self) -> str:
        result = f"Extermination ({self.state}): " 
        result += f"Défense = {self.dice} "
        result += f"Zombis = "
        result += ', '.join(f"{zombi}" for zombi in self.zombis)
        result += f" Zombis_spot = "
        result += ', '.join(f"{zombi}" for zombi in self.zombis_spots)
        return result
    
    def add_zombis(self, nb:int):
        for _ in range(nb):
            if len(self.zombis_spots)>0:
                self.zombis.append(self.zombis_spots.select())

class DiceRoad(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.nb_of_dice = 4
        self.enable = 0
        self.dice = []

    def __str__(self) -> str:
        result = f"PISTE DE DES [{'ACTIVE' if self.enable else 'INACTIVE'}]"
        result += ': ' + str(self.dice)
        return result
    
    def activate(self):
        self.enable = 1

    def throwdice(self):
        self.dice=[]
        for i in range(self.nb_of_dice):
            self.dice[i] = random.randint(1,6)

class HandTools(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.tools = []

    def __str__(self) -> str:
        result = f"MAIN:" + str(self.tools)
        return result

class Manufacture(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.position = 0
        self.die = None

    def __str__(self) -> str:
        return f'Fabrication ({self.state}) : position={self.position} die={self.die}'    

class MovePlace(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.dice = []

    def __str__(self) -> str:
        return f'Deplacement ({self.state}: {self.dice})'

class CityRoad(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.districts = []
        self.caro_position = 0

        self.districts.append(District(2))
        self.districts.append(District(1))
        self.districts.append(District(1))
        self.districts.append(District(0, True))
        self.districts.append(District(1))
        self.districts.append(District(1))
        self.districts.append(District(2))
        self.districts.append(District(2))
        self.districts.append(District(2))
        self.districts.append(District(3, istown=True))
        self.districts.append(District(3, istown=True))
        self.districts.append(District(1))
        self.districts.append(District(0,True))
        self.districts.append(District(1))
        self.districts.append(District(2))
        self.districts.append(District(3, istown=True))
        self.districts.append(District(3, istown=True))
        self.districts.append(District(2))
        self.districts.append(District(1,True))
        self.districts.append(District(1))
        self.districts.append(District(2))
        self.districts.append(District(3, istown=True))
        self.districts.append(District(4, istown=True))
        self.districts.append(District(4))
        self.districts.append(District(4))
        self.districts.append(District(4,True))
        self.districts.append(District(4))
        self.districts.append(District(0,ishospital=True))
        
    def __str__(self) -> str:
        result=f"PELOUSE, position={self.caro_position}: {self.districts[self.caro_position-1]}" + '\n'
        for i in range(self.caro_position, len(self.districts)-1):
            result += f"{self.districts[i]} -> "
        return result

class ProgressRoad(ActivationZone):
    def __init__(self) -> None:
        super().__init__()
        self.track = Track()

    def __str__(self) -> str:
        return f"JAUGES DE CONTROLE: {self.track}"


