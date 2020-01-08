couleurs = ["bleu", "vert", "jaune", "blanc", "noir"]
print (couleurs)
print (couleurs[0])
print (couleurs[1:3])
legumes = ["carotte", "pomme de terre", "navet", "oignon", "courgette"]

liste = [couleurs, legumes]
print (liste)
print (liste[0][2])

liste[1].append("tomate")
print (liste)
liste[1].insert(3, "poireau")
print (liste)

legumes.remove("oignon")
print (legumes)

legumes.sort()
print ("Tri : ", legumes)
legumes.reverse()
print ("Tri inverse :", legumes)
del legumes [2]
print (legumes)

print (len(legumes))
print (min(legumes))
print (max(legumes))
legumes.clear()
print ("Après effacement : " , legumes)

legumes = ["carotte", "pomme de terre", "navet", "oignon", "courgette"]
legumes2 = tuple(legumes)
print (legumes2)
print(legumes2.index("carotte"))

personne = {'Nom':'Dupont', 'Prenom':'Jean', 'Age':30, 'Sexe':'Masculin'}
print (personne)
print (personne.keys())
print (personne.values())
print (personne["Age"])
print (personne.get("Prenom"))
personne["Nationnalité"] = "Français"
personne["DateNaissance"] = "2000-12-23"
print (personne)
del personne["Age"]
print (personne)
