# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid
import wx.adv

import gettext
_ = gettext.gettext

###########################################################################
## Class fenetre
###########################################################################

class fenetre ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"Tests de wxgets"), pos = wx.DefaultPosition, size = wx.Size( 640,474 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL, name = u"fenetre" )

        self.SetSizeHints( wx.Size( 640,380 ), wx.DefaultSize )

        base = wx.BoxSizer( wx.VERTICAL )

        self.Ptop = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.NB_MULTILINE )
        self.P1 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP1base = wx.BoxSizer( wx.VERTICAL )

        P1radios = wx.BoxSizer( wx.HORIZONTAL )

        self.v__radio1 = wx.RadioButton( self.P1, wx.ID_ANY, _(u"Cliquez"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"radio1" )
        P1radios.Add( self.v__radio1, 0, wx.ALL, 5 )

        self.v__radio2 = wx.RadioButton( self.P1, wx.ID_ANY, _(u"Sur un de"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"radio2" )
        P1radios.Add( self.v__radio2, 0, wx.ALL, 5 )

        self.v__radio3 = wx.RadioButton( self.P1, wx.ID_ANY, _(u"ces jolis"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"radio3" )
        P1radios.Add( self.v__radio3, 0, wx.ALL, 5 )

        self.v__radio4 = wx.RadioButton( self.P1, wx.ID_ANY, _(u"petits boutons"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"radio4" )
        P1radios.Add( self.v__radio4, 0, wx.ALL, 5 )

        self.v__radio5 = wx.RadioButton( self.P1, wx.ID_ANY, _(u"tout rond"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"radio5" )
        P1radios.Add( self.v__radio5, 0, wx.ALL, 5 )


        sizerP1base.Add( P1radios, 1, wx.EXPAND, 5 )

        P1cases = wx.BoxSizer( wx.HORIZONTAL )

        self.v__case1 = wx.CheckBox( self.P1, wx.ID_ANY, _(u"Ces cases"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"case1" )
        P1cases.Add( self.v__case1, 0, wx.ALL, 5 )

        self.v__case2 = wx.CheckBox( self.P1, wx.ID_ANY, _(u"à cocher"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"case2" )
        P1cases.Add( self.v__case2, 0, wx.ALL, 5 )

        self.v__case3 = wx.CheckBox( self.P1, wx.ID_ANY, _(u"sont la"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"case3" )
        P1cases.Add( self.v__case3, 0, wx.ALL, 5 )

        self.v__case4 = wx.CheckBox( self.P1, wx.ID_ANY, _(u"pour que vous"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"case4" )
        P1cases.Add( self.v__case4, 0, wx.ALL, 5 )

        self.v__case5 = wx.CheckBox( self.P1, wx.ID_ANY, _(u"cliquez dessus"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"case5" )
        P1cases.Add( self.v__case5, 0, wx.ALL, 5 )


        sizerP1base.Add( P1cases, 1, wx.EXPAND, 5 )

        P1boutons = wx.BoxSizer( wx.HORIZONTAL )

        self.v__bt1 = wx.ToggleButton( self.P1, wx.ID_ANY, _(u"ces boutons ont"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bt1" )
        P1boutons.Add( self.v__bt1, 0, wx.ALL, 5 )

        self.v__bt2 = wx.ToggleButton( self.P1, wx.ID_ANY, _(u"tendance"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bt2" )
        P1boutons.Add( self.v__bt2, 0, wx.ALL, 5 )

        self.v__bt3 = wx.ToggleButton( self.P1, wx.ID_ANY, _(u"a basculer"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bt3" )
        P1boutons.Add( self.v__bt3, 0, wx.ALL, 5 )

        self.v__bt4 = wx.ToggleButton( self.P1, wx.ID_ANY, _(u"et c'est"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bt4" )
        P1boutons.Add( self.v__bt4, 0, wx.ALL, 5 )

        self.v__bt5 = wx.ToggleButton( self.P1, wx.ID_ANY, _(u"génial"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bt5" )
        P1boutons.Add( self.v__bt5, 0, wx.ALL, 5 )


        sizerP1base.Add( P1boutons, 1, wx.EXPAND, 5 )


        self.P1.SetSizer( sizerP1base )
        self.P1.Layout()
        sizerP1base.Fit( self.P1 )
        self.Ptop.AddPage( self.P1, _(u"Cases a cochers"), True )
        self.P2 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP2base = wx.BoxSizer( wx.VERTICAL )

        self.v__num1 = wx.Slider( self.P2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL, wx.DefaultValidator, u"num1" )
        sizerP2base.Add( self.v__num1, 0, wx.ALL|wx.EXPAND, 5 )

        self.v__num2 = wx.ScrollBar( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SB_HORIZONTAL, wx.DefaultValidator, u"num2" )
        sizerP2base.Add( self.v__num2, 0, wx.ALL|wx.EXPAND, 5 )

        numext = wx.BoxSizer( wx.HORIZONTAL )

        self.v__num3 = wx.SpinCtrl( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 10, 0, u"num3" )
        numext.Add( self.v__num3, 0, wx.ALL|wx.EXPAND, 5 )

        self.v__num4 = wx.SpinCtrlDouble( self.P2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.SP_ARROW_KEYS, 0, 100, 2.000000, 1, u"num4" )
        self.v__num4.SetDigits( 0 )
        numext.Add( self.v__num4, 0, wx.ALL|wx.EXPAND, 5 )

        self.v__num5 = wx.SpinButton( self.P2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0, u"num5" )
        numext.Add( self.v__num5, 0, wx.ALL|wx.EXPAND, 5 )


        sizerP2base.Add( numext, 1, wx.EXPAND, 5 )


        self.P2.SetSizer( sizerP2base )
        self.P2.Layout()
        sizerP2base.Fit( self.P2 )
        self.Ptop.AddPage( self.P2, _(u"Nombres"), False )
        self.P3 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP3base = wx.BoxSizer( wx.VERTICAL )

        v__liste1Choices = [ _(u"Ceci"), _(u"est"), _(u"une"), _(u"simple"), _(u"liste"), _(u"pour"), _(u"s'amuser"), _(u"un peu") ]
        self.v__liste1 = wx.ComboBox( self.P3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, v__liste1Choices, 0, wx.DefaultValidator, u"liste1" )
        self.v__liste1.SetSelection( 0 )
        sizerP3base.Add( self.v__liste1, 0, wx.ALL|wx.EXPAND, 5 )

        v__liste2Choices = [ _(u"Un"), _(u"autre"), _(u"exemple"), _(u"de liste"), _(u"éditable"), _(u"pour tester"), _(u"pleins de"), _(u"trucs"), _(u"différents") ]
        self.v__liste2 = wx.Choice( self.P3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, v__liste2Choices, 0, wx.DefaultValidator, u"liste2" )
        self.v__liste2.SetSelection( 0 )
        sizerP3base.Add( self.v__liste2, 0, wx.ALL|wx.EXPAND, 5 )


        self.P3.SetSizer( sizerP3base )
        self.P3.Layout()
        sizerP3base.Fit( self.P3 )
        self.Ptop.AddPage( self.P3, _(u"Listes"), False )
        self.P4 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP4base = wx.GridSizer( 0, 1, 0, 0 )

        self.v__texte = wx.TextCtrl( self.P4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE, wx.DefaultValidator, u"texte" )
        self.v__texte.SetMaxLength( 1000 )
        sizerP4base.Add( self.v__texte, 0, wx.ALL|wx.EXPAND, 5 )


        self.P4.SetSizer( sizerP4base )
        self.P4.Layout()
        sizerP4base.Fit( self.P4 )
        self.Ptop.AddPage( self.P4, _(u"Texte"), False )
        self.P5 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP5base = wx.GridSizer( 0, 2, 0, 0 )

        self.v__tree = wx.TreeCtrl( self.P5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE|wx.TR_EDIT_LABELS|wx.TR_ROW_LINES, wx.DefaultValidator, u"tree" )
        sizerP5base.Add( self.v__tree, 0, wx.ALL|wx.EXPAND, 5 )

        self.v__grid = wx.grid.Grid( self.P5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0, u"grid" )

        # Grid
        self.v__grid.CreateGrid( 3, 3 )
        self.v__grid.EnableEditing( True )
        self.v__grid.EnableGridLines( True )
        self.v__grid.SetGridLineColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.v__grid.EnableDragGridSize( True )
        self.v__grid.SetMargins( 0, 0 )

        # Columns
        self.v__grid.AutoSizeColumns()
        self.v__grid.EnableDragColMove( True )
        self.v__grid.EnableDragColSize( True )
        self.v__grid.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Rows
        self.v__grid.AutoSizeRows()
        self.v__grid.EnableDragRowSize( True )
        self.v__grid.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

        # Label Appearance

        # Cell Defaults
        self.v__grid.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
        sizerP5base.Add( self.v__grid, 0, wx.ALL|wx.EXPAND, 5 )


        self.P5.SetSizer( sizerP5base )
        self.P5.Layout()
        sizerP5base.Fit( self.P5 )
        self.Ptop.AddPage( self.P5, _(u"arbre et tableau"), False )
        self.P6 = wx.Panel( self.Ptop, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        sizerP6base = wx.WrapSizer( wx.VERTICAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.v__date = wx.adv.DatePickerCtrl( self.P6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.DP_DEFAULT, wx.DefaultValidator, u"date" )
        sizerP6base.Add( self.v__date, 0, wx.ALL, 5 )

        self.v__heure = wx.adv.TimePickerCtrl( self.P6, wx.ID_ANY, wx.DefaultDateTime, wx.DefaultPosition, wx.Size( 100,-1 ), wx.adv.TP_DEFAULT, wx.DefaultValidator, u"heure" )
        sizerP6base.Add( self.v__heure, 0, wx.ALL, 5 )

        self.v__fontp = wx.FontPickerCtrl( self.P6, wx.ID_ANY, wx.NullFont, wx.DefaultPosition, wx.Size( 200,-1 ), wx.FNTP_DEFAULT_STYLE|wx.FNTP_FONTDESC_AS_LABEL|wx.FNTP_USEFONT_FOR_LABEL|wx.FNTP_USE_TEXTCTRL, wx.DefaultValidator, u"fontp" )
        self.v__fontp.SetMaxPointSize( 100 )
        sizerP6base.Add( self.v__fontp, 0, wx.ALL, 5 )

        self.v__colorp = wx.ColourPickerCtrl( self.P6, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE|wx.CLRP_SHOW_LABEL|wx.CLRP_USE_TEXTCTRL, wx.DefaultValidator, u"colorp" )
        sizerP6base.Add( self.v__colorp, 0, wx.ALL, 5 )

        self.v__dirp = wx.DirPickerCtrl( self.P6, wx.ID_ANY, wx.EmptyString, _(u"Select a folder"), wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE|wx.DIRP_USE_TEXTCTRL, wx.DefaultValidator, u"dirp" )
        sizerP6base.Add( self.v__dirp, 0, wx.ALL, 5 )

        self.v__filep = wx.FilePickerCtrl( self.P6, wx.ID_ANY, wx.EmptyString, _(u"Select a file"), _(u"*.*"), wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_OPEN|wx.FLP_USE_TEXTCTRL, wx.DefaultValidator, u"filep" )
        sizerP6base.Add( self.v__filep, 0, wx.ALL, 5 )


        self.P6.SetSizer( sizerP6base )
        self.P6.Layout()
        sizerP6base.Fit( self.P6 )
        self.Ptop.AddPage( self.P6, _(u"Date/heure et selecteurs "), False )

        base.Add( self.Ptop, 1, wx.ALL|wx.EXPAND, 5 )

        self.Pbot = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.get = wx.Panel( self.Pbot, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        getpanbase = wx.BoxSizer( wx.VERTICAL )

        self.getselectcontrole = wx.adv.BitmapComboBox( self.get, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, [], 0, wx.DefaultValidator, u"getselectcontrole" )
        self.getselectcontrole.SetMinSize( wx.Size( -1,32 ) )

        getpanbase.Add( self.getselectcontrole, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )

        getpanext = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.bgetobj = wx.Button( self.get, wx.ID_ANY, _(u"objet"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetobj" )
        getpanext.Add( self.bgetobj, 0, wx.ALL, 5 )

        self.bgetid = wx.Button( self.get, wx.ID_ANY, _(u"Id"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetid" )
        getpanext.Add( self.bgetid, 0, wx.ALL, 5 )

        self.bgetname = wx.Button( self.get, wx.ID_ANY, _(u"name"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetname" )
        getpanext.Add( self.bgetname, 0, wx.ALL, 5 )

        self.bgetlabel = wx.Button( self.get, wx.ID_ANY, _(u"Label"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetlabel" )
        getpanext.Add( self.bgetlabel, 0, wx.ALL, 5 )

        self.bgetvalue = wx.Button( self.get, wx.ID_ANY, _(u"Value"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetvalue" )
        getpanext.Add( self.bgetvalue, 0, wx.ALL, 5 )

        self.bgetsel = wx.Button( self.get, wx.ID_ANY, _(u"Selection"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetsel" )
        getpanext.Add( self.bgetsel, 0, wx.ALL, 5 )

        self.bgetenable = wx.Button( self.get, wx.ID_ANY, _(u"Enabled"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetenable" )
        getpanext.Add( self.bgetenable, 0, wx.ALL, 5 )

        self.bgetdisable = wx.Button( self.get, wx.ID_ANY, _(u"hide"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bgetdisable" )
        getpanext.Add( self.bgetdisable, 0, wx.ALL, 5 )


        getpanbase.Add( getpanext, 1, wx.EXPAND, 5 )

        self.getbar = wx.Gauge( self.get, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.getbar.SetValue( 0 )
        getpanbase.Add( self.getbar, 0, wx.ALL|wx.EXPAND, 5 )

        self.getcode = wx.TextCtrl( self.get, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"getcode" )
        getpanbase.Add( self.getcode, 0, wx.ALL|wx.EXPAND, 5 )


        self.get.SetSizer( getpanbase )
        self.get.Layout()
        getpanbase.Fit( self.get )
        self.Pbot.AddPage( self.get, _(u"get"), False )
        self.set = wx.Panel( self.Pbot, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        setpanbase = wx.BoxSizer( wx.VERTICAL )

        self.setselectcontrole = wx.adv.BitmapComboBox( self.set, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, [], 0, wx.DefaultValidator, u"setselectcontrole" )
        self.setselectcontrole.SetMinSize( wx.Size( -1,32 ) )

        setpanbase.Add( self.setselectcontrole, 0, wx.EXPAND|wx.FIXED_MINSIZE, 5 )

        setpanext = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

        self.bsetlabel = wx.Button( self.set, wx.ID_ANY, _(u"Label"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetlabel" )
        setpanext.Add( self.bsetlabel, 0, wx.ALL, 5 )

        self.bsetvalue = wx.Button( self.set, wx.ID_ANY, _(u"Value"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetvalue" )
        setpanext.Add( self.bsetvalue, 0, wx.ALL, 5 )

        self.bsetsel = wx.Button( self.set, wx.ID_ANY, _(u"Selection"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetsel" )
        setpanext.Add( self.bsetsel, 0, wx.ALL, 5 )

        self.bseten = wx.Button( self.set, wx.ID_ANY, _(u"Enable"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bseten" )
        setpanext.Add( self.bseten, 0, wx.ALL, 5 )

        self.bsetdis = wx.Button( self.set, wx.ID_ANY, _(u"Disable"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetdis" )
        setpanext.Add( self.bsetdis, 0, wx.ALL, 5 )

        self.bsethide = wx.Button( self.set, wx.ID_ANY, _(u"hide"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsethide" )
        setpanext.Add( self.bsethide, 0, wx.ALL, 5 )

        self.bsetshow = wx.Button( self.set, wx.ID_ANY, _(u"Show"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetshow" )
        setpanext.Add( self.bsetshow, 0, wx.ALL, 5 )

        self.bsetseparation = wx.StaticLine( self.set, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_VERTICAL, u"bsetseparation" )
        setpanext.Add( self.bsetseparation, 0, wx.ALL|wx.EXPAND|wx.RESERVE_SPACE_EVEN_IF_HIDDEN, 10 )

        self.bsetslabeldefvalspe = wx.StaticText( self.set, wx.ID_ANY, _(u"Definir valeurs spéciales"), wx.DefaultPosition, wx.DefaultSize, 0, u"bsetslabeldefvalspe" )
        self.bsetslabeldefvalspe.Wrap( -1 )

        setpanext.Add( self.bsetslabeldefvalspe, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

        self.bsetvnone = wx.Button( self.set, wx.ID_ANY, _(u"None"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetvnone" )
        setpanext.Add( self.bsetvnone, 0, wx.ALL, 5 )

        self.bsetvtrue = wx.Button( self.set, wx.ID_ANY, _(u"True"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetvtrue" )
        setpanext.Add( self.bsetvtrue, 0, wx.ALL, 5 )

        self.bsetvfalse = wx.Button( self.set, wx.ID_ANY, _(u"False"), wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"bsetvfalse" )
        setpanext.Add( self.bsetvfalse, 0, wx.ALL, 5 )


        setpanbase.Add( setpanext, 1, wx.EXPAND, 5 )

        self.setcode = wx.TextCtrl( self.set, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0, wx.DefaultValidator, u"setcode" )
        setpanbase.Add( self.setcode, 0, wx.ALL|wx.EXPAND, 5 )


        self.set.SetSizer( setpanbase )
        self.set.Layout()
        setpanbase.Fit( self.set )
        self.Pbot.AddPage( self.set, _(u"set"), False )
        self.infosquit = wx.Panel( self.Pbot, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        infosquitbase = wx.BoxSizer( wx.VERTICAL )

        self.infotexte = wx.StaticText( self.infosquit, wx.ID_ANY, _(u"Cette démo permet de tester différents effets de bout de codes sur différents wxget suivant leurs états via de simples boutons.\namusez-vous avec ce qui se trouve en haut de la fenêtre et cliquez sur les boutons contenus dans les onglets get et set a coté de cet onglet.\nAstuces: si vous avez lancé cette application avec un terminal ouvert vous verrez les erreurs, infos et bout de codes utilisés lorsque vous cliquerez surt les boutons des onglets get et set."), wx.DefaultPosition, wx.Size( 500,100 ), 0, u"infotexte" )
        self.infotexte.Wrap( -1 )

        infosquitbase.Add( self.infotexte, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE|wx.SHAPED, 5 )

        self.boutonquitter = wx.Button( self.infosquit, wx.ID_ANY, _(u"Quitter"), wx.Point( 10,200 ), wx.Size( 500,-1 ), 0, wx.DefaultValidator, u"boutonquitter" )
        self.boutonquitter.SetMinSize( wx.Size( 200,-1 ) )

        infosquitbase.Add( self.boutonquitter, 0, wx.ALL|wx.EXPAND, 5 )


        self.infosquit.SetSizer( infosquitbase )
        self.infosquit.Layout()
        infosquitbase.Fit( self.infosquit )
        self.Pbot.AddPage( self.infosquit, _(u"Infos et quitter"), True )

        base.Add( self.Pbot, 1, wx.ALL|wx.EXPAND, 5 )


        self.SetSizer( base )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_CLOSE, self.OnClose )
        self.bgetobj.Bind( wx.EVT_BUTTON, self.clicbgetobj )
        self.bgetid.Bind( wx.EVT_BUTTON, self.clicbgetid )
        self.bgetname.Bind( wx.EVT_BUTTON, self.clicbgetname )
        self.bgetlabel.Bind( wx.EVT_BUTTON, self.clicbgetlabel )
        self.bgetvalue.Bind( wx.EVT_BUTTON, self.clicbgetvalue )
        self.bgetsel.Bind( wx.EVT_BUTTON, self.clicbgetsel )
        self.bgetenable.Bind( wx.EVT_BUTTON, self.clicbgetenabled )
        self.bgetdisable.Bind( wx.EVT_BUTTON, self.clicbgetdisable )
        self.getcode.Bind( wx.EVT_TEXT, self.chiffreverbarre )
        self.bsetlabel.Bind( wx.EVT_BUTTON, self.clicbsetlabel )
        self.bsetvalue.Bind( wx.EVT_BUTTON, self.clicbsetvalue )
        self.bsetsel.Bind( wx.EVT_BUTTON, self.clicbsetsel )
        self.bseten.Bind( wx.EVT_BUTTON, self.clicbseten )
        self.bsetdis.Bind( wx.EVT_BUTTON, self.clicbsetdis )
        self.bsethide.Bind( wx.EVT_BUTTON, self.clicbsethide )
        self.bsetshow.Bind( wx.EVT_BUTTON, self.clicbsetshow )
        self.bsetvnone.Bind( wx.EVT_BUTTON, self.clicbsetvnone )
        self.bsetvtrue.Bind( wx.EVT_BUTTON, self.clicbsetvtrue )
        self.bsetvfalse.Bind( wx.EVT_BUTTON, self.clicbsetvfalse )
        self.boutonquitter.Bind( wx.EVT_BUTTON, self.clicsurboutonquitter )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def OnClose( self, event ):
        event.Skip()

    def clicbgetobj( self, event ):
        event.Skip()

    def clicbgetid( self, event ):
        event.Skip()

    def clicbgetname( self, event ):
        event.Skip()

    def clicbgetlabel( self, event ):
        event.Skip()

    def clicbgetvalue( self, event ):
        event.Skip()

    def clicbgetsel( self, event ):
        event.Skip()

    def clicbgetenabled( self, event ):
        event.Skip()

    def clicbgetdisable( self, event ):
        event.Skip()

    def chiffreverbarre( self, event ):
        event.Skip()

    def clicbsetlabel( self, event ):
        event.Skip()

    def clicbsetvalue( self, event ):
        event.Skip()

    def clicbsetsel( self, event ):
        event.Skip()

    def clicbseten( self, event ):
        event.Skip()

    def clicbsetdis( self, event ):
        event.Skip()

    def clicbsethide( self, event ):
        event.Skip()

    def clicbsetshow( self, event ):
        event.Skip()

    def clicbsetvnone( self, event ):
        event.Skip()

    def clicbsetvtrue( self, event ):
        event.Skip()

    def clicbsetvfalse( self, event ):
        event.Skip()

    def clicsurboutonquitter( self, event ):
        event.Skip()


