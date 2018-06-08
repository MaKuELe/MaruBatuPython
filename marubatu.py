
#マスの状況を表示する関数
def print_list(list_val):
    for i in range(9):
        if (i+1)%3==0:
            print("|"+list_val[i]+"|");
        else:
           print("|"+list_val[i],end="");


class marubatu_data:
    def __init__(self):
        self.square=['1','2','3','4','5','6','7','8',"9"]
        self.mark=["p1","p2"]
        self.input_counter=0

        self.game_message="ゲームを始めます"

    def SetSquare(self,index):
        try:
            self.square[index]=self.mark[self.input_counter%2]
            self.input_counter+=1;
        except ValueError:
            print("マスの範囲外が指定されました。")
            return False

        return True

    def GetSquareAll(self):
        return  self.square;

    def GameResult(self):
        winner=self.CulcWinner()
        if winner!="No Winner":
            return winner
        
        if self.input_counter>9:
            return "Drow"
        
        return "Countinue"

    def CulcWinner(self):
        win_player="No Winner"
        if self.square[0]==self.square[1] and self.square[1]==self.square[2]:
            win_player=(self.square[0]);
        elif self.square[0]==self.square[4] and self.square[4]==self.square[8]:
            win_player=(self.square[0]);
        elif self.square[0]==self.square[3] and self.square[3]==self.square[6]:
            win_player=(self.square[0]);
        elif self.square[1]==self.square[4] and self.square[4]==self.square[8]:
            win_player=(self.square[1]);
        elif self.square[2]==self.square[4] and self.square[4]==self.square[6]:
            win_player=(self.square[2]);
        elif self.square[2]==self.square[5] and self.square[5]==self.square[8]:
            win_player=(self.square[2]);
        elif self.square[3]==self.square[4] and self.square[4]==self.square[5]:
            win_player=(self.square[3]);
        elif self.square[6]==self.square[7] and self.square[7]==self.square[8]:
            win_player=(self.square[6]);
        return win_player

        
def marubatu_game():
    game=marubatu_data()

    while game.GameResult()=="Countinue":
        print_list(game.GetSquareAll())
        forindex=input("1~9:")
        game.SetSquare(int(forindex)-1)
    
    print_list(game.GetSquareAll())
    return game.GameResult()
        