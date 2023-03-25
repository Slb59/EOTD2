import random

class Tool:
    def __init__(self, name, description, image) -> None:
        self.name = name
        self.description = description
        self.image = image
        self.statut = 0 # 0: tool is activate, 1: tool is not activate
        self.enable = 0 # 0: it's not possible to activate the tool, 1: tool can be activate

    def __str__(self) -> str:
        return self.name
    
class DiceTool(Tool):
    def __init__(self, name, description, image) -> None:
        super().__init__(name, description, image)
        self.dices = []

class OrdinaryTool(Tool):
    def __init__(self, name, description, image) -> None:
        super().__init__(name, description, image)

class Market:
    def __init__(self) -> None:
        self.warehouse = [] # list of tools 9 is the max size
        self.stall = [] # list of tools 3 is the max size
        self.statut = 0 # 0 for closed, 1 for open

        self.warehouse.append(
            DiceTool('Boule',
                 '+1 carbnurant et +1 chance if dé=5 est placé',
                 'assets/carte-boule.png')
            )
        
        self.warehouse.append(
            OrdinaryTool('Nourriture',
                 "+1 à n'importe quelle valeur de dés d'action",
                 'assets/carte-nourriture.png')
            )
        
        self.warehouse.append(
            OrdinaryTool('GPS',
                 "Avancer d'une case",
                 'assets/carte-gps.png')
            )
        
        self.warehouse.append(
            DiceTool('Guide de survie',
                 "Gagné un outil si dé=6 est placé",
                 'assets/carte-guide.png')
            )
        
        self.warehouse.append(
            OrdinaryTool('Outil multifonction',
                 "Relance n'importe quel dé d'action",
                 'assets/carte-outil.png')
            )
        
        self.warehouse.append(
            DiceTool('Piège',
                 "-2 apparitions de zombis pour ce tour si 2 dés identiques placés",
                 'assets/carte-piege.png')
            )
        
        self.warehouse.append(
            OrdinaryTool('Sac de riz',
                 "Ajout permanent +1 dé d'action",
                 'assets/carte-riz.png')
            )
        
        self.warehouse.append(
            OrdinaryTool('Scotch',
                 "Tourner n'importe quel dé sur la face opposée",
                 'assets/carte-scotch.png')
            )
        
        self.warehouse.append(
            DiceTool('Kit de survie',
                 "+2 carburant et +1 santé ou +2 santé et +1 carburant."+ 
                "La somme des dés placés = 7",
                 'assets/carte-survie.png')
            )

    def complete_stall(self):
        while len(self.stall) < 3:
            self.stall.append(self.warehouse[random.randint(0,len(self.warehouse)-1)])