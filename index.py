from Pages.Classes.Classe_Pokedex import Pokedex
from Pages.BDD.BDDAttaque import *

pokedex = Pokedex()

pokedex.ajout("Florizarre",3,"G1")
pokedex.ajout("Bulbizarre",1,"G1")
pokedex.ajout("Herbizarre",2,"G1")
pokedex.ajout("Méga-Herbizarre",3.1,"Mega")
pokedex.ajout("Salamèche",4,"G1")
pokedex.ajout("Reptincel",5,"G1")
pokedex.ajout("Dracaufeu",6,"G1")
pokedex.ajout("Germignon",152,"G2")
pokedex.ajout("GFlorizarre",3.2,"Gigamax")
pokedex.ajout("Shaymin",492,"G4",[100, 100, 100, 100, 100, 100],[Croissance, Feuille_Magik, Vampigraine, Synthese,Doux_Parfum,Calinerie, Soucigraine, Champ_Herbu, Eco_Sphere,Doux_Baiser, Voeu_Soin,Fulmigraine],"./Pokémon_img/G4/Shaymin.png","Plante",None,"Médic Nature",None,None,0.2,2.1)
pokedex.ajout("Miaouss",52,"G1")
pokedex.ajout("Miaouss d'Alola",52,"G7")