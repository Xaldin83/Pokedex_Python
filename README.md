# 📖 Pokédex — Application de gestion Python / Tkinter

Une application de bureau Pokédex complète, développée en Python avec une interface graphique Tkinter. Elle permet de consulter, ajouter, modifier et supprimer des Pokémon, avec affichage de leurs statistiques, types, talents et attaques.

---

## 🖥️ Aperçu des fonctionnalités

- 📋 **Consulter** la liste complète des Pokémon enregistrés
- 🔎 **Filtrer** par génération
- 📄 **Afficher** la fiche détaillée d'un Pokémon (image, types, talents, taille, poids, stats, attaques)
- ➕ **Ajouter** un nouveau Pokémon au Pokédex
- ✏️ **Modifier** les données d'un Pokémon existant
- 🗑️ **Supprimer** un Pokémon du Pokédex

---

## 🗂️ Structure du projet

```
📦 Projet
├── Lanceur.py                  # Point d'entrée de l'application
├── Fonctions/
│   ├── main.py                 # Page principale (liste + recherche)
│   ├── Global_page.py          # Fiche détaillée d'un Pokémon
│   ├── rajout.py               # Formulaire d'ajout d'un Pokémon
│   ├── modification.py         # Formulaire de modification
│   ├── fonctions_ajouts.py     # Fonctions de lecture/écriture des fichiers
│   ├── index.py                # Données du Pokédex (liste de tous les Pokémon)
│   └── index.txt               # Liste des noms enregistrés (un par ligne)
├── Classes/
│   ├── Classe_Pokemon.py       # Classe Pokemon
│   ├── Classe_Pokedex.py       # Classes Pokedex et Page_Pokedex
│   ├── Classe_Attaque.py       # Classe Capacity (attaque)
│   └── BDDAttaque.py           # Base de données de toutes les attaques
├── Pokémon_img/
│   └── G1/                     # Images PNG des Pokémon, organisées par génération
│       └── Bulbizarre.png
└── Type/
    └── Miniature <Type>.png    # Icônes des types (ex: Miniature Plante.png)
```

---

## ⚙️ Architecture — Classes principales

### `Capacity` *(Classe_Attaque.py / BDDAttaque.py)*
Représente une attaque Pokémon.

| Attribut | Type | Description |
|---|---|---|
| `name` | str | Nom de l'attaque |
| `type` | str | Type de l'attaque |
| `pp` / `pp_max` | int | Points de pouvoir |
| `power` | int \| None | Puissance (None si sans dégâts) |
| `accuracy` | int \| None | Précision en % |
| `category` | str | `"Physique"`, `"Special"` ou `"Statut"` |

> `BDDAttaque.py` contient **l'intégralité des attaques** de la génération 1 jusqu'aux jeux les plus récents (plus de 500 attaques référencées).

---

### `Pokemon` *(Classe_Pokemon.py)*
Représente un Pokémon avec toutes ses données.

| Attribut | Type | Description |
|---|---|---|
| `name` | str | Nom du Pokémon |
| `number` | int | Numéro dans le Pokédex national |
| `stat` | list[int] | `[PV, ATK, DEF, ATK_S, DEF_S, VIT]` |
| `capacity` | list[Capacity] | Liste des attaques |
| `img` | str | Chemin vers l'image PNG |
| `type1` / `type2` | str / None | Types du Pokémon |
| `skill1/2/3` | str / None | Talents (jusqu'à 3, les 2e et 3e peuvent être `None`) |
| `height` / `weight` | float | Taille (m) et poids (kg) |
| `generation` | str | Ex : `"G1"`, `"G2"`, ... |

**Méthodes :**
- `list_capacity(listbox)` — affiche les attaques dans un widget Tkinter
- `list_stat(listbox)` — affiche les statistiques dans un widget Tkinter
- `afficher()` — affiche toutes les données dans la console

---

### `Pokedex` et `Page_Pokedex` *(Classe_Pokedex.py)*

`Page_Pokedex` encapsule un `Pokemon` avec ses métadonnées d'entrée de Pokédex.

`Pokedex` gère la collection complète :
- `ajout(...)` — ajoute une entrée
- `tri_number()` — trie par numéro de Pokédex (tri par sélection)
- `affichage_general(listbox)` — affiche tous les Pokémon dans une Listbox
- `affichage_generation(generation, listbox)` — filtre par génération
- `found_pages(name)` — retourne l'objet `Pokemon` correspondant à un nom

---

## 🚀 Installation & lancement

### Prérequis

```bash
pip install pillow
```

> `tkinter` est inclus avec Python. `Pillow` est requis pour l'affichage des images.

### Lancer l'application

```bash
python Lanceur.py
```

---

## 📝 Ajouter un Pokémon manuellement

Pour ajouter un Pokémon directement dans `index.py`, utilisez la méthode `pokedex.ajout()` :

```python
pokedex.ajout(
    "Bulbizarre",                      # Nom
    1,                                 # Numéro Pokédex
    "G1",                              # Génération
    [45, 49, 49, 65, 65, 45],          # Stats [PV, ATK, DEF, ATK_S, DEF_S, VIT]
    [Charge, Rugissement, Fouet_Lianes, ...],  # Liste d'attaques (depuis BDDAttaque)
    "./Pokémon_img/G1/Bulbizarre.png", # Chemin image
    "Plante",                          # Type 1
    "Poison",                          # Type 2 (None si mono-type)
    "Engrais",                         # Talent 1
    None,                              # Talent 2 (optionnel)
    "Chlorophylle",                    # Talent caché (optionnel)
    0.7,                               # Taille (m)
    6.9                                # Poids (kg)
)
```

Il faut aussi ajouter son nom dans `index.txt` (un nom par ligne).

---

## 🖼️ Organisation des ressources

- **Images Pokémon** : `./Pokémon_img/<Génération>/<Nom>.png`
  Ex : `./Pokémon_img/G1/Bulbizarre.png`
- **Icônes de types** : `./Type/Miniature <Type>.png`
  Ex : `./Type/Miniature Plante.png`

Les 18 types disponibles sont : Acier, Combat, Dragon, Eau, Electrik, Fée, Feu, Glace, Insecte, Normal, Plante, Poison, Psy, Roche, Sol, Spectre, Ténèbres, Vol.

---

## ⚠️ Notes et limitations connues

- Le projet utilise `os.system("python ...")` pour naviguer entre les fenêtres. Chaque changement de page relance un nouveau processus Python, ce qui peut être lent sur certaines machines.
- Les données du Pokédex sont stockées directement dans `index.py` sous forme de code Python généré dynamiquement par `fonctions_ajouts.py`.
- Les images doivent impérativement correspondre au chemin `./Pokémon_img/<génération>/<nom>.png` pour que l'ajout soit validé.
