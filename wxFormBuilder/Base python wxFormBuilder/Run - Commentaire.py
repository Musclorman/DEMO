# -*- coding=utf-8 -*-
#/usr/bin/env python3

#Solution améliorée et plus propre

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
        global compteclic
        compteclic+=1

app = wx.App()
MaFenetre(None).Show()
print("avant MainLoop")
app.MainLoop()
print("apres MainLoop et", compteclic, "clics")

