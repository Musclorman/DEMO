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
## Class fenetre
###########################################################################

class fenetre ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Exemple d'utilisation de Get() et Set()"), pos = wx.DefaultPosition, size = wx.Size( 396,181 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.infos = wx.StaticText( self, wx.ID_ANY, _(u"Tapez une simple phrase et cliquez sur le bouton"), wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
        self.infos.Wrap( -1 )

        bSizer1.Add( self.infos, 0, wx.ALL|wx.EXPAND, 5 )

        self.Entree = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_NO_VSCROLL )
        self.Entree.SetMaxLength( 20 )
        bSizer1.Add( self.Entree, 0, wx.ALL|wx.EXPAND, 5 )

        self.Sortie = wx.StaticText( self, wx.ID_ANY, _(u"Pas encore de texte"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.Sortie.Wrap( -1 )

        bSizer1.Add( self.Sortie, 0, wx.ALL|wx.EXPAND, 5 )

        self.OK = wx.Button( self, wx.ID_ANY, _(u"Valider"), wx.DefaultPosition, wx.DefaultSize, 0 )

        self.OK.SetBitmap( wx.NullBitmap )
        self.OK.SetBitmapPressed( wx.NullBitmap )
        self.OK.SetBitmapFocus( wx.NullBitmap )
        self.OK.SetBitmapCurrent( wx.NullBitmap )
        bSizer1.Add( self.OK, 0, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.OK.Bind( wx.EVT_BUTTON, self.Clicbouton )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def Clicbouton( self, event ):
        event.Skip()


