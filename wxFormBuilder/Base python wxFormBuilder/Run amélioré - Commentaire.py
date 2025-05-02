# -*- coding=utf-8 -*-
#/usr/bin/env python3

#Solution moyenneement simple mais elegante pour compter le nombre de clics sur un bouton dans une fenetre wxPython

#On importe les modules necessaires
import wx
import wx.xrc

#On importe le fichier de code genere par wxFormBuilder
#Il faut que le fichier genwx.py soit dans le meme repertoire que ce script
import genwx

#On crée une classe MaFenetre qui hérite de la classe Fenetre générée par wxFormBuilder
class MaFenetre(genwx.Fenetre):
    #On utilise __init__ pour initialiser la classe et créer un compteur de clics
    def __init__(self, *args, **kwargs):
        #Pour ne pas casser le constructeur de la classe mère, on appelle le constructeur de la classe mère avec les arguments passés
        super().__init__(*args, **kwargs)
        #On crée la variable globale compbien_de_clics pour compter le nombre de clics sur le bouton et on l'initialise à 0
        self.combien_de_clics = 0
    #On remplace le virtual event clicsurlebouton du fichier genwx.py par une méthode du même nom
    def clicsurlebouton(self, event):
        #On affiche un message dans la console pour indiquer que le bouton a été cliqué
        print("clic sur le bouton")
        #On utilise le mot-clé self pour indiquer que l'on veut utiliser la variable compteclic définie dans la classe et on lui ajoute 1
        self.combien_de_clics += 1

#On initialise l'application wxPython via une instance de wx.App
app = wx.App()
#On crée une instance de la classe MaFenetre, qui est la fenêtre principale de l'application et on passe None en paramètre pour indiquer que l'on ne veut pas de fenêtre parent. Elle prendra en charge le compteur de clics
fenetre = MaFenetre(None)
#On affiche la fenêtre
fenetre.Show()

#On affiche un message dans la console pour indiquer que l'on va entrer dans la boucle principale de l'application
print("avant MainLoop")
#On entre dans la boucle principale de l'application, qui attend les événements (clics, fermetures de fenêtres, etc.) et les traite
app.MainLoop()
#On affiche un message dans la console pour indiquer que l'on est sorti de la boucle principale de l'application et on affiche le nombre de clics sur le bouton grace a la variable de la classe et a un F-string
print(f"apres MainLoop et {fenetre.combien_de_clics} clics")
