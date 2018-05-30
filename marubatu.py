
#マスの状況を表示する関数
def print_list(list_val):
    for i in range(9):
        if (i+1)%3==0:
            print("|"+list_val[i]+"|");
        else:
           print("|"+list_val[i],end="");

#勝利判定をする関数。連座苦する3マスが同じ値だった場合に、3ますを埋めている値を勝利者として表示する。
#現在3マスの持つ値は評価していない。○でも×でもその他の値でも
def winner(list_val):
    if list_val[0]==list_val[1] and list_val[1]==list_val[2]:
        print (" Win:%c" % (list_val[0]))
    elif list_val[0]==list_val[4] and list_val[8]==list_val[9]:
        print (" Win:%c" % (list_val[0]))
    elif list_val[0]==list_val[3] and list_val[3]==list_val[6]:
        print (" Win:%c" % (list_val[0]))
    elif list_val[1]==list_val[4] and list_val[4]==list_val[8]:
        print (" Win:%c" % (list_val[1]))
    elif list_val[2]==list_val[4] and list_val[4]==list_val[6]:
        print (" Win:%c" % (list_val[2]))
    elif list_val[2]==list_val[5] and list_val[5]==list_val[8]:
        print (" Win:%c" % (list_val[2]))
    elif list_val[3]==list_val[4] and list_val[4]==list_val[5]:
        print (" Win:%c" % (list_val[3]))
    elif list_val[6]==list_val[7] and list_val[7]==list_val[8]:
        print (" Win:%c" % (list_val[6]))
    else:
        return "not fin"
    return "fin"

#ゲームのメインループ。9つのマスを埋めるか、連続する3マスを同じ値で生めたプレイヤーが現れた時点で終了する。
def game_main():
    place=['1','2','3','4','5','6','7','8',"9"]
    counter =0
    while counter<9:
        #現状の増すの状態を表示
        print_list(place)

        #○を記すか、×を記すか入力してもらう
        write_val = input("○:1 or ×:2:")

        #マス目を指定してもらう
        #現状0だったら終了。
        place_val = input("to :")
        if place_val[0]=="0":
            exit()

        #マス目を検索
        # 範囲外のマスを指定された場合ValueErrorで処理  
        try:
            target_index=place.index(place_val[0])
        except ValueError:
            print("指定されたマスが見つかりませんでした。")

        try:
            #入力値を ○ × に変換　
            #指定されたマスの値を削除
            #削除した位置に○か×を挿入
            if write_val[0] =="1":
                write="○"    
            elif write_val[0] =="2":
                write="×" 
            else:
                break;
            place.pop(target_index)
            place.insert(target_index,write)
        except :
            #とりあえず例外処理
            print("EXEPTIN")
            continue

        #勝利判定
        if "fin"==winner(place):
            break
        
        #入力回数の加算
        counter+=1
    return 1