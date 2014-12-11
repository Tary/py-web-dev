import wx

class CheckBoxFrame(wx.Frame):
	
		
	def __init__(self):
		wx.Frame.__init__(self, None, -1, 'Checkbox Example', size=(300, 200))
		panel = wx.Panel(self, -1)
		self.check = wx.CheckBox(panel, -1, u"我很萌哒 *^_^*", (100, 60), (150, 20))
		self.check.Bind(wx.EVT_CHECKBOX, self.OnCheck)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.tip = wx.StaticText(panel, -1, u"诚实点哈, 不然关不掉",(140, 130))
		self.tip.Show(False)
		
	def OnCheck(self, event):
		if self.check.GetValue():
			self.tip.Show(False)
		else:
			self.tip.Show(True)
	def OnClose(self, event):
		if self.check.GetValue():
			self.Destroy()
		else:
			self.tip.Show(True)


if __name__ == '__main__':
    app = wx.App()
    CheckBoxFrame().Show()
    app.MainLoop()  

