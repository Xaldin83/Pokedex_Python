import tkinter as tk

class Pokemon:
    def __init__(self, name = "", number = 0, stat = [], capacity=[], img = "", type1 = "",type2 = None, skill1 = "", skill2 ="", skill3 = None, height = 0, weight = 0):
        """
        Docstring pour __init__
        :param name: name du pokémon, en str.
        :param number: Numéro du pokémon dans le pokedex national, un int.
        :param stat: Liste d'entier, d'une taille de 6, représentant chaque stat dans l'ordre suivant [PV,Attaque, Défense, Attaque Spéciale, Défense Spéciale, Vitesse]
        :param capacity: Liste des capacity du pokémon, à déterminer, plus tard, si une classe est nécessaire
        :param img: chemin d'accès à l'image du pokémon.
        :param type1: Premier type du pokémon, une chaine de caractère.
        :param type2: Second type du pokémon, peut ne pas exister, dans ce cas, on laisse None.
        """
        self.name = name
        self.number = number
        self.stat = stat
        self.capacity = capacity
        self.type1 = type1
        self.type2 = type2
        self.img = img
        self.skill1 = skill1
        self.skill2 = skill2
        self.skil31 = skill3
        self.height = height
        self.weight = weight

    def list_capacity(self,listbox):
        """
        Docstring pour list_capacity
    
        :param listbox: nom de la listbox utiliser pour afficher les attaques, via du tkinter.
        """
        for i in self.capacity:
            listbox.insert(tk.END, f"{i.display()}")

    def list_stat(self,listbox):
        """
        Docstring pour list_stat
        
        :param listbox: nom de la listbox utiliser pour afficher les attaques, via du tkinter.
        """

        listbox.insert(tk.END, f"PV : {self.stat [0]}")
        listbox.insert(tk.END, f"ATK : {self.stat [1]}")
        listbox.insert(tk.END, f"DEF : {self.stat [2]}")
        listbox.insert(tk.END, f"ATK_S : {self.stat [3]}")
        listbox.insert(tk.END, f"DEF_S : {self.stat [4]}")
        listbox.insert(tk.END, f"VIt : {self.stat [5]}")