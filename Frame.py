#Boa:Frame:Frame1

import wx
import wx.lib.buttons
import kern


def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1GAUGE, wxID_FRAME1GENBUTTON1, wxID_FRAME1GENBUTTON2, 
 wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(246, 413), size=wx.Size(511, 216),
              style=wx.DEFAULT_FRAME_STYLE, title=u'changing')
        self.SetClientSize(wx.Size(495, 177))
        self.SetForegroundColour(wx.Colour(102, 246, 207))
        self.SetBackgroundColour(wx.Colour(102, 246, 207))

        self.gauge = wx.Gauge(id=wxID_FRAME1GAUGE, name='gauge', parent=self,
              pos=wx.Point(8, 112), range=100, size=wx.Size(480, 28),
              style=wx.GA_HORIZONTAL)
        self.gauge.SetForegroundColour(wx.Colour(102, 204, 102))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'process', name='staticText2', parent=self,
              pos=wx.Point(16, 152), size=wx.Size(41, 14), style=0)
        self.staticText2.SetBackgroundColour(wx.Colour(102, 249, 204))
        self.staticText2.SetForegroundColour(wx.Colour(1, 12, 9))

        self.genButton1 = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON1,
              label=u'to pdf', name='genButton1', parent=self, pos=wx.Point(48,
              40), size=wx.Size(79, 26), style=0)
        self.genButton1.SetBackgroundColour(wx.Colour(0, 102, 0))
        self.genButton1.SetForegroundColour(wx.Colour(0, 0, 0))
        self.genButton1.Bind(wx.EVT_BUTTON, self.convert,
              id=wxID_FRAME1GENBUTTON1)

        self.genButton2 = wx.lib.buttons.GenButton(id=wxID_FRAME1GENBUTTON2,
              label=u'about', name='genButton2', parent=self, pos=wx.Point(368,
              40), size=wx.Size(79, 26), style=0)
        self.genButton2.SetBackgroundColour(wx.Colour(0, 102, 0))
        self.genButton2.SetForegroundColour(wx.Colour(0, 0, 0))
        self.genButton2.Bind(wx.EVT_BUTTON, self.about,
              id=wxID_FRAME1GENBUTTON2)

    def __init__(self, parent):
        self._address=None
        self._filelist=[]
        self._threads=[]
        self._i=0
        self._init_ctrls(parent)

    def OnMainButton1Button(self, event):
        event.Skip()


    def about(self, event):
		dlg = wx.MessageDialog(None, u"Stephen for elaine", 
		u"about", wx.YES_NO | wx.ICON_QUESTION)
		if dlg.ShowModal() == wx.ID_YES:
			dlg.Destroy()
		event.Skip()
        
    def updatewindow(self,num):  
        self.gauge.SetValue(num)
        
    def convert(self, event):
        dialog = wx.DirDialog(None, 'Choose a directory: ',
                              style = wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
                self._address=dialog.GetPath()
        dialog.Destroy()
        kern.get_file(self._address,self._filelist)
        event.Skip()
        l=len(self._filelist)
        c = kern.canvas.Canvas('result.pdf', pagesize = kern.landscape(kern.A4))
        (w, h) = kern.landscape(kern.A4)
        for i in range(l):
            f=self._filelist[i]
            c.drawImage(f, 0, 0, w, h)
            c.save()
            self.updatewindow((i*100)/l)
        self.updatewindow(100)
        self.complete()
        event.Skip()
        
    def complete(self):
        dlg = wx.MessageDialog(None, u"mission complete", u"congratulations", wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            dlg.Destroy()
    

