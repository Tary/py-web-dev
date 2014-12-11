# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainView
###########################################################################

class MainView ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 637,174 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.__staticText1 = wx.StaticText( self, wx.ID_ANY, u"网址", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.__staticText1.Wrap( -1 )
		bSizer2.Add( self.__staticText1, 0, wx.ALL, 6 )
		
		self.m_url = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		bSizer2.Add( self.m_url, 1, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 0, wx.ALL|wx.EXPAND, 0 )
		
		self.m_log = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_log.Wrap( -1 )
		bSizer1.Add( self.m_log, 1, wx.ALL|wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_opendir = wx.Button( self, wx.ID_ANY, u"打开目录", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_opendir.Enable( False )
		
		bSizer3.Add( self.m_opendir, 0, wx.ALL, 5 )
		
		self.m_download = wx.Button( self, wx.ID_ANY, u"下载", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.m_download, 0, wx.ALIGN_RIGHT|wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 0, wx.ALIGN_RIGHT|wx.ALL, 0 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_url.Bind( wx.EVT_TEXT, self.onUrlChanged )
		self.m_opendir.Bind( wx.EVT_BUTTON, self.onOpenDir )
		self.m_download.Bind( wx.EVT_BUTTON, self.onDownload )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def onUrlChanged( self, event ):
		event.Skip()
	
	def onOpenDir( self, event ):
		event.Skip()
	
	def onDownload( self, event ):
		event.Skip()
	

