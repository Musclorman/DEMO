# -*- coding=utf-8 -*-
#/usr/bin/env python3

#On importa la bibliothèque wx ainsi que le fichier généré par wxFormBuilder
import wx
import genwx

#On crée une classe MaFenetre qui hérite de la classe Fenetre générée par wxFormBuilder
class MaFenetre(genwx.fenetre):
    #On utilise __init__ pour initialiser la classe
    def __init__(self, *args, **kwargs):
        #On appelle le constructeur de la classe mère pour ne pas casser le constructeur de la classe
        super().__init__(*args, **kwargs)
    #On définit une méthode Clicbouton qui sera appelée lorsque le bouton sera cliqué
    def Clicbouton(self, event):
        #On affiche le contenu de l'entrée dans la console...
        print(self.Entree.GetValue())
        #... et on met à jour le label de la sortie avec le même contenu
        self.Sortie.SetLabel(self.Entree.GetValue())

#On initialise l'application wxPython via une instance de wx.App
app = wx.App(None)
#On crée une instance de la classe MaFenetre, qui est la fenêtre principale de l'application
fenetre = MaFenetre(None)
#On initialise la fenêtre qui n'a pas de parent
fenetre.Show()
#On prépare l'affichage de la fenêtre
app.MainLoop()
#On entre dans la boucle principale de l'application, qui attend les événements (clics, fermetures de fenêtres, etc.) et les traite

