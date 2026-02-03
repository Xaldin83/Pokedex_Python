import tkinter as tk

class Page_Pokedex:
    def __init__(self,  name = "", number = 0, generation = ""):

        self.name = name
        self.number = number
        self.generation = generation


class Pokedex:
    def __init__(self):
        self.liste = []

    def ajout(self,  name = "", number = 0, generation = ""):
        self.liste+=[Page_Pokedex(name,number,generation)]
    
    def tri_number(self):
        n=len(self.liste)
        i=0
        while(i<n-2):
            mini = i
            j=i+1
            while(j<n-1):
                if(self.liste[j].number<self.liste[mini].number):
                    mini = j
                j+=1
            self.liste[mini],self.liste[i]=self.liste[i],self.liste[mini]
            i+=1
    
    def affichage_generation(self,generation,listbox):
        listbox.delete(0, listbox.size()-1)
        self.tri_number()
        for i in self.liste:
            if(i.generation==generation):
                listbox.insert(tk.END, i.name)

    def affichage_general(self,listbox):
        listbox.delete(0, listbox.size()-1)
        self.tri_number()
        for i in self.liste:
            listbox.insert(tk.END, i.name)
