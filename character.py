class Character:
    def __init__(self, hp, atk, acc, moves):
        self.hp = hp
        self.atk = atk
        self.acc = acc
        self.moves = moves
    
    def __str__(self):
        return f"HP: {self.hp}\nATK: {self.atk}\nACC: {self.acc}"