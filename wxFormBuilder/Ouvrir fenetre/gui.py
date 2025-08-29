# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class FenBase
###########################################################################

class FenBase ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Fenêtre de base"), pos = wx.DefaultPosition, size = wx.Size( 356,173 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.BoutonOuvrir = wx.Button( self, wx.ID_ANY, _(u"Ouvrir nouvelle fenêtre "), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.BoutonOuvrir.SetDefault()
        bSizer1.Add( self.BoutonOuvrir, 0, wx.ALL, 5 )

        self.BoutonFermer = wx.Button( self, wx.ID_ANY, _(u"Fermer"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.BoutonFermer, 0, wx.ALL, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.BoutonOuvrir.Bind( wx.EVT_BUTTON, self.ouvre )
        self.BoutonFermer.Bind( wx.EVT_BUTTON, self.ferme )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def ouvre( self, event ):
        event.Skip()

    def ferme( self, event ):
        event.Skip()


###########################################################################
## Class FenOuv
###########################################################################

class FenOuv ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Nouvelle fenêtre"), pos = wx.Point( 10,10 ), size = wx.Size( 185,106 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer2 = wx.BoxSizer( wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, _(u"Vous avez bien ouvert la nouvelle fenêtre"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.BoutonFermer = wx.Button( self, wx.ID_ANY, _(u"Fermer"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.BoutonFermer, 0, wx.ALL, 5 )


        self.SetSizer( bSizer2 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.apresferme )
        self.BoutonFermer.Bind( wx.EVT_BUTTON, self.ferme )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def apresferme( self, event ):
        event.Skip()

    def ferme( self, event ):
        event.Skip()


