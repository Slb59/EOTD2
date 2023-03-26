class Track:
    def __init__(self) -> None:
        self.health = 10
        self.petrol = 4
        self.luck = 2

    def __str__(self) -> str:
        return f"GAZOIL={self.petrol} CHANCE={self.luck} SANTE={self.health}"
