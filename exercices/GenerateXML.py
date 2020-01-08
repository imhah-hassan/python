# -*- coding: utf-8 -*-
import xml.etree.cElementTree as xml
from random import randint
from faker import Faker
from faker import Factory

fakerFR = Factory.create('fr_FR')

def monsieur(root, nbEnfants):
    salarie = xml.SubElement(root, "Salarie", Matricule=str(fakerFR.pyint())+str(fakerFR.pyint()))
    nom  = fakerFR.last_name()
    prenom = fakerFR.first_name_male()
    xml.SubElement(salarie, "Nom").text = nom
    xml.SubElement(salarie, "Prenom").text = prenom
    email = nom+'.'+prenom+'@'+fakerFR.domain_name()
    xml.SubElement(salarie, "Email").text =  email
    xml.SubElement(salarie, "Telephone").text = fakerFR.phone_number()
    xml.SubElement(salarie, "Adresse1").text = fakerFR.street_address()
    xml.SubElement(salarie, "Ville").text = fakerFR.city()
    xml.SubElement(salarie, "Poste").text = fakerFR.job()
    xml.SubElement(salarie, "DateNaissance").text = str(fakerFR.date_of_birth(tzinfo=None, minimum_age=30, maximum_age=58))
    xml.SubElement(salarie, "CodePostal").text = fakerFR.postcode()
    xml.SubElement(salarie, "Banque").text = fakerFR.iban()
    xml.SubElement(salarie, "Salaire").text = str(randint(200, 700)*10)+'.00'
    conjoint= xml.SubElement(salarie, "Conjoint")
    xml.SubElement(conjoint, "Nom").text = nom
    prenom = fakerFR.first_name_female()
    xml.SubElement(conjoint, "Prenom").text = prenom
    email = nom+'.'+prenom+'@'+fakerFR.domain_name()
    xml.SubElement(conjoint, "Email").text = email
    xml.SubElement(conjoint, "DateNaissance").text = str(fakerFR.date_of_birth(tzinfo=None, minimum_age=30, maximum_age=58))
    for index in range(0, nbEnfants):
        enfant= xml.SubElement(salarie, "Enfant")
        xml.SubElement(enfant, "Nom").text = nom
        if (nbEnfants%2) == 0:
            xml.SubElement(enfant, "Prenom").text = fakerFR.first_name_female()
        else:
            xml.SubElement(enfant, "Prenom").text = fakerFR.first_name_male()
        xml.SubElement(enfant, "DateNaissance").text = str(fakerFR.date_of_birth(tzinfo=None, minimum_age=2, maximum_age=15))



root = xml.Element("Salaries")
for index in range(0, 15):
    monsieur(root, randint(1, 4))

tree = xml.ElementTree(root)
tree.write('c:\\temp\\employee.xml')

