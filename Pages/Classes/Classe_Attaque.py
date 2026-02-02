class Capacity:
    
    def __init__(self, name="", type=None, pp=0, power=None, accuracy=None, category = ""):
        '''
        Définition d'une attaque
        name (un char)
        type (un char)
        pp (un int)
        power (un int (si existe))
        accuracy (un int (si existe))
        category (un char)
        '''

        self.name = name
        self.type = type
        self.pp_max = pp
        self.pp = pp
        self.power = power
        self.accuracy = accuracy
        self.category = category

    def display(self):
        return f"{self.name} | {self.type} | {self.category}"