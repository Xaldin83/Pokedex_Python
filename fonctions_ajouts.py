def ajout_index(name):
    file=open(f"index.txt","a",encoding='utf-8')
    file.write(f"""\n{name}""")
    file.close()


def ajout_pkm(name,number,stat,type1,type2,skill1,skill2,skill3,height,weight,generation,capacity):
    link = f"./Pokémon_img/{generation}/{name}.png"
    file=open(f"./index.py","a",encoding='utf-8')
    file.write(f"""pokedex.ajout("{name}",{number},"{generation}]",{stat},[{capacity}],"{link}","{type1}","{type2}","{skill1}","{skill2}","{skill3}",{height},{weight})""")
    file.close()

def modif_pkm(name,number,stat,type1,type2,skill1,skill2,skill3,height,weight,generation,capacity):
    link = f"./Pokémon_img/{generation}/{name}.png"
    with open("./index.py", "r",encoding='utf-8') as fp:
        lines = fp.readlines()

    with open("./index.py", "w", encoding='utf-8') as fp:
        for line in lines:
            if line.strip("\n") != f"{name}":
                fp.write(line)
    file=open(f"./index.py","a",encoding='utf-8')
    file.write(f"""pokedex.ajout("{name}",{number},"{generation}]",{stat},[{capacity}],"{link}","{type1}","{type2}","{skill1}","{skill2}","{skill3}",{height},{weight})""")
    file.close()