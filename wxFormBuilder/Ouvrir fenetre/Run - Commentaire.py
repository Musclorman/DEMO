# -*- coding=utf-8 -*-
#/usr/bin/env python3

#On importa la bibliothèque wx ainsi que le fichier généré par wxFormBuilder
import wx
import gui

#On crée une classe FBase qui hérite de la classe FenBase générée par wxFormBuilder
class FBase (gui.FenBase):
    #On utilise __init__ pour initialiser la classe
    def __init__(self, *args, **kwargs):
        #On appelle le constructeur de la classe mère
        super().__init__(*args, **kwargs)
    def ouvre(self, event):
        #On crée une instance de la classe FOuv:
        fo = FOuv(parent=self)
        #On désactive la fenêtre actuelle
        self.Disable()
        #On affiche la nouvelle fenêtre
        fo.Show()
    #On crée une méthode ferme qui sera appelée lors du clic sur le bouton "Fermer"
    def ferme(self, event):
        #Cela fait la même action que clique sur le bouton Fermer (x)dans la barre de titre. Par défault cela ferme la fenêtre
        self.Close()

#On crée une classe FOuv qui hérite de la classe FenOuv générée par wxFormBuilder
class FOuv (gui.FenOuv):
    #On utilise __init__ pour initialiser la classe
    def __init__(self, *args, **kwargs):
        #On appelle le constructeur de la classe mère
        super().__init__(*args, **kwargs)
     #Si on clique sur le bouton "Fermer", on appelle la méthode ferme
    def ferme(self, event):
        #Cela fait la même action que clique sur le bouton Fermer (x)dans la barre de titre mais il y a un problème car la fenêtre principale reste désactivée
        self.Close()
    #On crée une méthode apresferme qui sera appelée après la fermeture de la fenêtre et qui remplira la méthode par défaut OnClose
    def apresferme(self, event):
        #On réactive la fenêtre parente
        self.GetParent().Enable()
        #On détruit (ferme) la fenêtre courante car l'action de fermeture par défaut ne le fait pas vu qu'on l'a remplacé par une autre
        self.Destroy()

#On crée une instance de la classe wx.App qui est obligatoire pour toute application wxPython
app = wx.App(None)
#On crée une instance de la fenêtre principale
fenetre = FBase(None)
#On affiche la fenêtre principale
fenetre.Show()
#On lance la boucle principale de l'application
app.MainLoop()
