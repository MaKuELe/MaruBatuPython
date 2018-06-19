import wx
import marubatu
  
class MarubatuApp(wx.App):
    
    #game
    #STRA="CCC"
    def OnInit(self): 
        self.STRA="ABC"
        self.game=marubatu.marubatu_data()
        self.main_flame=MarubatuFrame()
        self.main_flame.Show()
        return True

    #=marubatu.marubatu_data()
    def setSTRA(self):
        print ("%s"%self.STRA)
        self.STRA="BBB"
        print ("%s"%self.STRA)

    def GetGameData2(self):
        return game
  
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

class MarubatuFrame(wx.Frame):
    """
    フレームを継承したトップレベルウィンドウクラス
    """
  
    def __init__(self):
          
        super().__init__(None, wx.ID_ANY, '○×ゲーム', size=(180, 400))
  
        # ステータスバーの初期化
        #self.CreateStatusBar()
        #self.GetStatusBar().SetBackgroundColour(None)
  
        # メニューバーの初期化
        #self.SetMenuBar(CalcMenu())
          
        # 本体部分の構築
        root_panel = wx.Panel(self, wx.ID_ANY)
  
        message_panel = TextPanel(root_panel)
        square_button_panel = CalcButtonPanel(root_panel)
  
        root_layout = wx.BoxSizer(wx.VERTICAL)
        root_layout.Add(message_panel, 0, wx.GROW | wx.ALL, border=10)
        root_layout.Add(square_button_panel, 0, wx.GROW | wx.ALL, border=10)
        root_panel.SetSizer(root_layout)


      #  root_layout.Fit(root_panel)
  

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
        app=wx.GetApp()
        app.game
     
        calc_text = wx.StaticText(self, wx.ID_ANY, style=wx.TE_RIGHT,label=app.game.GetMessage())
        layout = wx.BoxSizer(wx.HORIZONTAL)
        layout.Add(calc_text, 1,flag=wx.GROW)
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
    
    player_mark=("○","×");
    def on_click_button_1(self,event):
        clicked_button=event.GetEventObject()
        app=wx.GetApp()

        if(clicked_button.GetLabel()=="○" and clicked_button.GetLabel()=="×"):
            return False
        
        target_index=int(clicked_button.GetName())
        if False==app.game.SetSquare(target_index):
            return False
            
        new_label=app.game.GetSquareAt(target_index)

        
        clicked_button.SetLabel(new_label[1])

        sq=app.game.GetSquareAll()
        for i in range(0,9):    
            print("%s"%sq[i])

        result=app.game.GameResult()
        if result=="Drow":
            print("Drow")
            exit()
        elif result=="Countinue":
            print("Cont")
            pass
        else:
            print ("End")
            exit()

       

    def __init__(self, parent):
      
        super().__init__(parent, wx.ID_ANY)
  
        button_collection = ('1','2','3'
        ,'4','5','6'
        ,'7','8','9')
  
        layout = wx.GridSizer(3, 3,0,0)
        
        for i in range(0,9):
            self.button_t.append(wx.Button(self, wx.ID_ANY, str(i+1),size=(30,30),name=str(i)))
           
        for i in range(0,9):
            self.button_t[i].Bind(wx.EVT_BUTTON,self.on_click_button_1)
            layout.Add(self.button_t[i], 1, wx.EXPAND)

        self.SetSizer(layout)
        self.counter=0;


if __name__ == '__main__':
  
    # カスタムフレームを初期化してアプリケーションを開始
    application = MarubatuApp()
   # frame = MarubatuFrame()
 #   application.main_flame.Show()
#    frame.Show()
    application.MainLoop()
