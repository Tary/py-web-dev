from MyDialog import MyDialog
import wx

class Meditor(MyDialog):
	def __init__(self):
		MyDialog.__init__(self, None)
	def OnAAA( self, event ):
		if type(event.EventObject) is wx.Button:
			self.m_staticText.SetLabel(str((event.EventObject.GetLabel())))
		else:
			self.m_staticText.SetLabel(str((event.EventObject.GetSelection())))
		event.Skip()
	def onClose( self, event ):
		self.Destroy()
		
if __name__ == '__main__':
    app = wx.App()
    Meditor().Show()
    app.MainLoop() 