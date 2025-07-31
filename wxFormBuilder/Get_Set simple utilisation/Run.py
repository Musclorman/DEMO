# -*- coding=utf-8 -*-
#/usr/bin/env python3


import wx
import genwx

class MaFenetre(genwx.fenetre):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def Clicbouton(self, event):
        print(self.Entree.GetValue())
        self.Sortie.SetLabel(self.Entree.GetValue())
app = wx.App(None)
fenetre = MaFenetre(None)
fenetre.Show()
app.MainLoop()
