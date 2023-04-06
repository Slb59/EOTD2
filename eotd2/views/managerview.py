import questionary
# from eotd2.controllers import Manager

class ManagerView:
    def __init__(self, manager) -> None:
        self.manager = manager

    def all_menu_choices(self) -> dict:
        return {
            1:["Afficher le plateau",True],
            2:["Lancer les dés",self.manager.diceroad.statut],
            3:["Relancer 1 dé",self.manager.progressroad.track.luck > 0],
            4:["Ajouter un dé en zone fabrication",self.manager.manufacturezone.statut],
            5:["Ajouter un dé en zone ville-santé",self.manager.townplace.statut],
            6:["Ajouter un dé en zone ville-chance",self.manager.townplace.statut],
            7:["Ajouter un dé en zone ville-extermination",self.manager.townplace.statut],
            8:["Activer une carte outil",self.manager.hand.statut],
            9:["Quitter le jeu",True]
            }

    def menu_choices(self) -> list:
        choices = []
        for elem in self.all_menu_choices().values():
            if elem[1]:
                choices.append(elem[0])
        return choices

    def display_lost(self):
        print("Vous avez été dévoré par une horde de zombis affamés !!!".upper())      
    
    def display_welcome(self):
        text = "ESCAPE OF THE DEAD 2"
        print(len(text) * '-')
        print(text)
        print(len(text) * '-')
        print("Rejoins l'hospital au plus vite !")

    def display_win(self):
        print("Vous avez atteint l'hôspital, vous êtes sauvé !!!".upper())

    def display_menu(self):
        print('')
        print(50 * '-')
        answer = questionary.select(
            "Que souhaitez-vous faire ?",
            choices=self.menu_choices()
        ).ask()
        return answer