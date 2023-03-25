import random

class Zombi:
    def __init__(self, name:str, image:str) -> None:
        self.name = name
        self.image = image
        self._actif = False

    def __str__(self) -> str:
        return self.name

class Zombis:
    def __init__(self) -> None:
        self.zombi_spot = []
        self.zombi_spot.append(Zombi('Zombi1','assets/zombi1.png'))
        self.zombi_spot.append(Zombi('Zombi2','assets/zombi2.png'))
        self.zombi_spot.append(Zombi('Zombi3','assets/zombi3.png'))
        self.zombi_spot.append(Zombi('Zombi4','assets/zombi4.png'))
        self.zombi_spot.append(Zombi('Zombi5','assets/zombi5.png'))
        self.zombi_spot.append(Zombi('Zombi6','assets/zombi6.png'))

    def __repr__(self) -> str:
        return str(self.zombi_spot)

    def select(self) -> Zombi:
        return self.zombi_spot[random.randint(0,5)]