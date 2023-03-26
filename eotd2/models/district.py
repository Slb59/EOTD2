class District:
    def __init__(self, nb:int, event=False, istown = False, ishospital = False) -> None:
        self.nb_of_zombis = nb
        self.event = event
        self.istown = istown
        self.ishospital = ishospital

    def __str__(self) -> str:
        result = f"{self.nb_of_zombis} zombis"
        result += f"{' * ' if self.event else ''}"
        result += f"{' ^|| ' if self.istown else ''}"
        result += f"{'YOU ARE SAFE' if self.ishospital else ''}"
        return result