# -*- coding=utf-8 -*-
#/usr/bin/env python3

import wx
import wx.xrc

import genwx

class MaFenetre(genwx.Fenetre):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.combien_de_clics = 0
        
    def clicsurlebouton(self, event):
        print("clic sur le bouton")
        self.combien_de_clics += 1


app = wx.App()
fenetre = MaFenetre(None)
fenetre.Show()
print("avant MainLoop")
app.MainLoop()
print(f"apres MainLoop et {fenetre.combien_de_clics} clics")
