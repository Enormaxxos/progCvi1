seznam = [('kočka', 'Anička'), ('pes', 'Petr'), ('želva', 'Marie'), ('andulka', 'Boženka'), ('veverka', 'Tereza'), ('datel', 'Marek'), ('orel', 'Josef'), ('noserožec', 'Damián'), ('beruška', 'Magdaléna'), ('ropucha', 'Běla'), ('kačer', 'Bohumír'), ('kůň', 'Martin'), ('kohout', 'Benedikt'), ('hroch', 'Bohouš'), ('želva', 'Apolena')] 
newDict = dict()

for unit in seznam:
    newDict[unit[0]] = unit[1]

for key,val in newDict.items():
    print(f"{key} ma jmeno {val}.")
