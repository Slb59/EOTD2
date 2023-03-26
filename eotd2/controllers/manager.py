from eotd2.models import Manufacture
from eotd2.models import MovePlace, TownPlace, ExterminationZone
from eotd2.models import CityRoad, HandTools, DiceRoad, ProgressRoad

class Manager():
    def __init__(self) -> None:
        self.manufacturezone = Manufacture()
        self.moveplacezone = MovePlace()
        self.townplace = TownPlace()
        self.exterminaticon = ExterminationZone()
        self.city = CityRoad()
        self.hand = HandTools
        self.diceroad = DiceRoad()
        self.progressroad = ProgressRoad()

    def display_map(self):
        print(self.manufacturezone)
        print(self.moveplacezone)
        print(self.townplace)
        self.exterminaticon.add_zombis(2)
        print(self.exterminaticon)
        print(self.city)
        print(self.hand)
        print(self.diceroad)
        print(self.progressroad)

    