class Character:
    def __init__(self, name, max_hp, atk, acc, moves):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.acc = acc
        self.moves = moves
    
    def __str__(self):
        return f"NAME: {self.name}\nHP: {self.hp}/{self.max_hp}\nATK: {self.atk}\nACC: {self.acc}"