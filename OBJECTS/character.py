class Character:
    def __init__(self, name, level, xp, gold, max_hp, atk, acc, moves, defence=0, boss=False):
        self.name = name
        self.level = level
        self.xp = xp
        self.gold = gold
        self.max_hp = max_hp
        self.hp = max_hp
        self.atk = atk
        self.acc = acc
        self.moves = moves
        self.debuffs = []
        self.defence = defence
        self.boss = boss
    
    def __str__(self):
        return f"NAME: {self.name.title()}\nHP: {self.hp}/{self.max_hp}\nLEVEL: {self.level}\nGOLD: {self.gold}\nATK: {self.atk}\nDEF: {self.defence}\nACC: {self.acc}\n"
