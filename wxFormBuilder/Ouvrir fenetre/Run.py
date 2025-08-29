# -*- coding=utf-8 -*-
#/usr/bin/env python3


import wx
import gui

class FBase (gui.FenBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def ouvre(self, event):
        fo = FOuv(parent=self)
        self.Disable()
        fo.Show()
    def ferme(self, event):
        self.Close()
class FOuv (gui.FenOuv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def ferme(self, event):
        self.Close()
    def apresferme(self, event):
        self.GetParent().Enable()
        self.Destroy()



app = wx.App(None)
fenetre = FBase(None)
fenetre.Show()
app.MainLoop()