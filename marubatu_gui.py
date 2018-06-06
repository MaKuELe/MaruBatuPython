import wx
  
  
class CalcFrame(wx.Frame):
    """
    フレームを継承したトップレベルウィンドウクラス
    """
  
    def __init__(self):
          
        super().__init__(None, wx.ID_ANY, '電卓レイアウト', size=(180, 400))
  
        # ステータスバーの初期化
        self.CreateStatusBar()
        self.SetStatusText('https://www.python-izm.com/')
        self.GetStatusBar().SetBackgroundColour(None)
  
        # メニューバーの初期化
        #self.SetMenuBar(CalcMenu())
          
        # 本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)
  
        text_panel = TextPanel(root_panel)
        #cmdbutton_panel = CommandButtonPanel(root_panel)
        calcbutton_panel = CalcButtonPanel(root_panel)
  
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(text_panel, 0, wx.GROW | wx.ALL, border=10)
       # root_layout.Add(cmdbutton_panel, 0, wx.GROW | wx.LEFT | wx.RIGHT, border=20)
        root_layout.Add(calcbutton_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)
        root_layout.Fit(root_panel)
  
  
class CalcMenu(wx.MenuBar):
    """
    CalcFrameにセットするメニューバークラス
    """
  
    def __init__(self):
  
        super().__init__()
          
        menu_file = wx.Menu()
        menu_file.Append(wx.ID_ANY, '保存')
        menu_file.Append(wx.ID_ANY, '終了')
        menu_edit = wx.Menu()
        menu_edit.Append(wx.ID_ANY, 'コピー')
        menu_edit.Append(wx.ID_ANY, 'ペースト')
          
        self.Append(menu_file, 'ファイル')
        self.Append(menu_edit, '編集')
  
  
class TextPanel(wx.Panel):
    """
    画面上部に表示されるテキスト部分
    """
  
    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
          
        calc_text = wx.TextCtrl(self, wx.ID_ANY, style=wx.TE_RIGHT)
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1)
        self.SetSizer(layout)
  
  
class CommandButtonPanel(wx.Panel):
    """
    画面中部に表示されるボタン部分
    """
      
    def __init__(self, parent):
  
        super().__init__(parent, wx.ID_ANY)
  
        button_ce = wx.Button(self, wx.ID_ANY, 'CE')
        button_c  = wx.Button(self, wx.ID_ANY, 'C')
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(button_ce, flag=wx.GROW)
        layout.Add(button_c, flag=wx.GROW)
        self.SetSizer(layout)
  
  
class CalcButtonPanel(wx.Panel):
    """
    画面下部に表示されるボタン部分
    """
    button_t=[]

    def click_button_1(self,event):
        clicked_button=event.GetEventObject()
        clicked_button.SetLabel("A")
#        wx.CommandEvent.GetEventObject

    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
  
        button_collection = ('1','2','3'
        ,'4','5','6'
        ,'7','8','9')
  
        layout = wx.GridSizer(3, 3,0,0)
          
        for i in button_collection:
            self.button_t.append(wx.Button(self, wx.ID_ANY, i,size=(30,30),name=i))
            
        for i in range(0,9):
            self.button_t[i].Bind(wx.EVT_BUTTON,self.click_button_1)
            layout.Add(self.button_t[i], 1, wx.EXPAND)

        self.SetSizer(layout)
        
  

if __name__ == '__main__':
  
    # カスタムフレームを初期化してアプリケーションを開始
    application = wx.App()
    frame = CalcFrame()
    frame.Show()
    application.MainLoop()
