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
## Class Fenetre
###########################################################################

class Fenetre ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

        self.bouton = wx.Button( self, wx.ID_ANY, _(u"Afficher texte dans console"), wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer1.Add( self.bouton, 0, wx.ALL, 5 )


        self.SetSizer( gSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.bouton.Bind( wx.EVT_BUTTON, self.clicsurlebouton )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def clicsurlebouton( self, event ):
        event.Skip()


