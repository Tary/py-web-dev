from MainView import MainView
import wx
import os
from taobao_image_parser import download, parser

class Meditor(MainView):
    def __init__(self):
        MainView.__init__(self, None)
        self.SetTitle(u"淘宝放大图片下载工具")
        self.current_dir = None

    def _setCurrentDir(self, dir):
        self.current_dir = dir
        if dir is None:
            self.m_opendir.Enable(False)
        else:
            self.m_opendir.Enable(True)

    def onDownload(self, event):
        url_text = str(self.m_url.GetValue())

        if url_text is None or len(url_text) == 0:
            self.m_log.SetLabelText(u"没有填网址")
        else:
            try:
                forder_ = parser(url_text, 'c:/OUT_PUT', str(hash(url_text)))
                self._setCurrentDir(forder_)
                print url_text
                if forder_ is not None:
                    self.m_opendir.Show(True)
                    self.m_log.SetLabelText(u"URL: %s\n的资源 输出到C:/OUT_PUT/%s" % (url_text,forder_))
                else:
                    self.m_log.SetLabelText(u"URL: %s的资源\n 输出失败" % (url_text))
            except StandardError, e:
                self.m_log.SetLabelText(u"输出失败\n%s" % e.message)
        event.Skip()

    def onUrlChanged( self, event ):
        self._setCurrentDir(None)
        event.Skip()

    def onOpenDir( self, event ):
        if self.current_dir is not None:
            path = "C:\\OUT_PUT\\%s\\" % self.current_dir
            os.system("explorer.exe %s" % path)
            print path
        event.Skip()

    def onClose(self, event):
        self.Destroy()




if __name__ == '__main__':
    app = wx.App()
    Meditor().Show()
    app.MainLoop() 