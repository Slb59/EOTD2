from eotd2.models import Manufacture
from eotd2.models import MovePlace, TownPlace, ExterminationZone
from eotd2.models import CityRoad, HandTools, DiceRoad, ProgressRoad
from eotd2.views import ManagerView

class Manager():
    def __init__(self) -> None:
        self.manufacturezone = Manufacture()
        self.moveplacezone = MovePlace()
        self.townplace = TownPlace()
        self.exterminaticon = ExterminationZone()
        self.city = CityRoad()
        self.hand = HandTools()
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

    def start_game(self):
        self.diceroad.activate()
        managerview = ManagerView(self)
        managerview.display_welcome()
        running = True

        while running:

            if self.city.caro_position == len(self.city.districts):
                managerview.display_win()
                running = False
                break

            answer = managerview.display_menu()
            if answer == managerview.all_menu_choices()[9][0]:
                managerview.display_lost()
                running = False