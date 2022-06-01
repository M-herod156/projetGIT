#-------------------------------------------------------------------------------
# Name: projet
# Purpose:
#
# Author:      Administrateur
#
# Created:     30/05/2022
# Copyright:   (c) Administrateur 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random


#Dictionnaire
voiture={"France":["Renault","Citroen","Dacia","Peugeot","DS Automobiles"],
         "USA":["Cadillac","Chevrolet","Chrysler","Ford","Ford Mustang","Shelby"]}

# Choix du thème
choix=input("choix du thème(France ou USA):")
mots=[random.choice(voiture[choix])]# élément aléatoirement pré-sélectionner dans la liste
mots[:]=mots[0]
print(mots)

entre=input("entre une lettre: ")
if entre not in mots:
    while entre :
        entre=input("entre une lettre: ")
        if entre in mots:
         print(entre)
if entre in mots:
      while entre in mots:
        entre=input("entre une lettre: ")
        if entre in mots:
         print(entre)
'''
c=0
while c <= len(mots):
    c=c+1
    entre=input("entre une lettre: ")
    if entre in mots:
     print(entre)'''

# ---------------------Base de données------------------------------------------

"""
import psycopg2
''' création d'une connexion '''
cnx=psycopg2.connect(host='localhost',port='5432',database='db_greta78',user='postgres',password='postgres')

''' création d'un curseur sur la connexion '''
crs=cnx.cursor()

''' affichage de la version de la base de données'''
crs.execute('select version();')

''' récupération du résultat d'exécution'''
db_version=crs.fetchall()
print('PostgreSQL database version:',db_version)

''' fermeture du cursueur et de la connexion'''
crs.close()
cnx.close()"""








