# -*- coding=utf-8 -*-
#/usr/bin/env python3

import wx
import wx.xrc
import wx.grid
import wx.adv


import gettext
_ = gettext.gettext

import gui



def parcourirwidgets(parent):
    for child in parent.GetChildren():
        print(f"""{child}
    Type: {type(child)}, Name: {child.GetName()}, ID: {child.GetId()}, Label: {child.GetLabel() if hasattr(child, 'GetLabel') else 'N/A'}""")
        parcourirwidgets(child)


listewget = ["radio1", "radio2", "radio3",
            "radio4", "radio5",
            "case1", "case2", "case3", "case4", "case5",
            "bt1", "bt2", "bt3", "bt4", "bt5",
            "num1", "num2", "num3", "num4", "num5",
            "liste1", "liste2", "texte", "tree", "grid",
            "date", "heure", "fontp", "colorp", "dirp", "filep"]


class appli(gui.fenetre):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("Affichage de la liste des widgets a des fin d'analyse :")
        parcourirwidgets(self)
        print("Fin de la liste des widgets\n\n\n")
        sc = self.setcode
        gc = self.getcode
        sl = self.setselectcontrole
        gl = self.getselectcontrole
        for i in listewget:
            j=self.FindWindowByName(i)
            sl.Append(j.GetName() + " - " + j.GetLabel())
            gl.Append(j.GetName() + " - " + j.GetLabel())


    def clicsurboutonquitter( self, event ):
        print("Clic sur le bouton quitter")
        self.Close()


    def clicbgetobj( self, event ):
        print("Clic sur le bouton getobj")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n))
            print(">>> "+ n.GetName() + "")
            print(str(n)+"\n")


    def clicbgetid( self, event ):
        print("Clic sur le bouton getId")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.GetId()))
            print(">>> "+ n.GetName() + ".GetId()")
            print(str(n.GetId())+"\n")

    def clicbgetname( self, event ):
        print("Clic sur le bouton GetName")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.GetName()))
            print(">>> "+ n.GetName() + ".getName()")
            print(str(n.GetName())+"\n")


    def clicbgetlabel( self, event ):
        print("Clic sur le bouton GetLabel")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.GetLabel()))
            print(">>> "+ n.GetName() + ".GetLabel()")
            print(str(n.GetLabel())+"\n")


    def clicbgetvalue( self, event ):
        print("Clic sur le bouton getValue")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.GetValue()))
            print(">>> "+ n.GetName() + ".GetValue()")
            print(str(n.GetValue())+"\n")

    def clicbgetsel( self, event ):
        print("Clic sur le bouton getsel")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.GetSelection()))
            print(">>> "+ n.GetName() + ".GetSelection()")
            print(str(n.GetSelection())+"\n")

    def clicbgetenabled( self, event ):
        print("Clic sur le bouton GetEnabled")
        i= self.getselectcontrole.GetSelection()
        if i<0:
            self.getcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            self.getcode.SetValue(str(n.IsEnabled()))
            print(">>> "+ n.GetName() + ".IsEnabled()")
            print(str(n.IsEnabled())+"\n")


    def clicbsetlabel( self, event ):
        print("Clic sur le bouton setlabel")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            l=str(self.setcode.GetValue())
            if i == "None":
                n.SetLabel(None)
            if l == "True" or l == "False":
                n.SetLabel(bool(l))
            try:
                n.SetLabel(int(l))
            except:
                n.SetLabel(l)
            print(">>> "+ n.GetName() + ".SetLabel()")
            print(str(n.GetLabel())+"\n")


    def clicbsetvalue( self, event ):
        print("Clic sur le bouton setvalue")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            l=str(self.setcode.GetValue())
            if l == "True" or l == "False":
                n.SetValue(bool(l))
            try:
                n.SetValue(int(l))
            except:
                n.SetValue(l)
            print(">>> "+ n.GetName() + ".SetValue()")
            print(str(n.GetValue())+"\n")


    def clicbsetsel( self, event ):
        print("Clic sur le bouton setsel")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            l=str(self.setcode.GetValue())
            if l == "True" or l == "False":
                n.SetValue(bool(l))
            if i == "None":
                n.SetValue(None)
            try:
                n.SetSelection(list(l))
            except:
                n.SetSelection(int(l))
            print(">>> "+ n.GetName() + ".SetSelection()")
            print(str(n.GetSelection())+"\n")


    def clicbseten( self, event ):
        print("Clic sur le bouton seten")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            n.Enable()
            print(">>> "+ n.GetName() + ".Enable()")
            print(str("Activable"+"\n"))


    def clicbsetdis( self, event ):
        print("Clic sur le bouton setdis")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            n.Disable()
            print(">>> "+ n.GetName() + ".Disable()")
            print(str("Non activable"+"\n"))




    def clicbsethide( self, event ):
        print("Clic sur le bouton sethide")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            n.Hide()
            print(">>> "+ n.GetName() + ".Hide()")
            print(str("Caché"+"\n"))


    def clicbsetshow( self, event ):
        print("Clic sur le bouton setshow")
        i= self.setselectcontrole.GetSelection()
        if i<0:
            self.setcode.SetValue("Aucun controle selectionne")
            print("Aucun controle selectionne")
        else:
            n=self.FindWindowByName(listewget[i])
            n.Show()
            print(">>> "+ n.GetName() + ".Show()")
            print(str("Affiché"+"\n"))


    def clicbsetvnone( self, event ):
        print("Clic sur le bouton setvnone")
        self.setcode.SetValue("None")
        print("Valeur sur None")


    def clicbsetvtrue( self, event ):
        print("Clic sur le bouton setvtrue")
        self.setcode.SetValue("True")
        print("Valeur sur True")


    def clicbsetvfalse( self, event ):
        print("Clic sur le bouton setvfalse")
        self.setcode.SetValue("False")
        print("Valeur sur False")


    def OnClose( self, event ):
        print("Fermeture de l'application")
        self.Destroy()

    def chiffreverbarre( self, event ):
        try:
            num=int(self.getcode.GetValue())
            if 0<=num<=100:
                    print("Valeur entre 0 et 100 - met a jours la barre de progression")
                    self.getbar.SetValue(num)
        except:
            pass










app = wx.App(None)
fenetre = appli(None)
fenetre.Show()
app.MainLoop()
