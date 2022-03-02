# Créé par Celhryn, le 02/03/2022 en Python 3.7
import pyautogui
from time import sleep
import random

pyautogui.alert("Si tu joues à ce jeu c'est que t'es vraiment con.")

print("Le principe du jeu est simple : Faire rouler le chargeur d'un six-coups avec un nombre de balle entre 1 et 6 avant de tirer sur sa tempe.")
print("Si le tir vous tue, vous avez perdu")

try :
    ndb = int(input("Choisis un nombre de balles entre 1 et 6 : "))

    if ndb > 6 :
      pyautogui.alert("Le nombre de balles est incorrect")

    elif ndb <= 6 and ndb >= 1 :
        pyautogui.alert("Partie lancée avecle nombre de balles choisi")
        print("Vous faites rouler le chargeur")
        delay = 5
        for i in range(5):
            sleep(1)
            print(delay, "...")
            delay = delay - 1
        result = random.randint(1,ndb + 1)
        if result == 1 :
            pyautogui.alert("Victoire")
        else :
            pyautogui.alert("WASTED")

    else :
        pyautogui.alert("Le nombre de balles est incorrect")
except :
    pyautogui.alert("Le nombre de balles est incorrect")