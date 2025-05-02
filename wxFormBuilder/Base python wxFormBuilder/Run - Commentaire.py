# -*- coding=utf-8 -*-
#/usr/bin/env python3

#Solution simple mais pas tres elegante pour compter le nombre de clics sur un bouton dans une fenetre wxPython

#On importe les modules necessaires
import wx
import wx.xrc

#On importe le fichier de code genere par wxFormBuilder
#Il faut que le fichier genwx.py soit dans le meme repertoire que ce script
import genwx

#On crée la variable compteclic pour compter le nombre de clics sur le bouton et on l'initialise à 0
compteclic= 0

#On crée une classe MaFenetre qui hérite de la classe Fenetre générée par wxFormBuilder
class MaFenetre(genwx.Fenetre):
    #On crée une méthode clicsurlebouton qui sera appelée lorsque l'on clique sur le bouton
    def clicsurlebouton(self, event):
        #On affiche un message dans la console pour indiquer que le bouton a été cliqué
        print("clic sur le bouton")
        #On utilise le mot-clé global pour indiquer que l'on veut utiliser la variable compteclic définie en dehors de la méthode}
        global compteclic
        #On incrémente le compteur de clics
        compteclic+=1

#On initialise l'application wxPython via une instance de wx.App
app = wx.App()
#On crée une instance de la classe MaFenetre, qui est la fenêtre principale de l'application et on passe None en paramètre pour indiquer que l'on ne veut pas de fenêtre parent
MaFenetre(None).Show()

#On affiche un message dans la console pour indiquer que l'on va entrer dans la boucle principale de l'application
print("avant MainLoop")
#On entre dans la boucle principale de l'application, qui attend les événements (clics, fermetures de fenêtres, etc.) et les traite
app.MainLoop()
#On affiche un message dans la console pour indiquer que l'on est sorti de la boucle principale de l'application et on affiche le nombre de clics sur le bouton
print("apres MainLoop et", compteclic, "clics")

