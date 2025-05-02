#/usr/bin/env python3
#-*- coding: utf-8 -*-

import wx
import wx.xrc

import genwx

global compteclic
compteclic= 0

class MaFenetre(genwx.Fenetre):
    def clicsurlebouton(self, event):
        print("clic sur le bouton")
        global compteclic
        compteclic+=1

app = wx.App()
MaFenetre(None).Show()
print("avant MainLoop")
app.MainLoop()
print("apres MainLoop et", compteclic, "clics")

