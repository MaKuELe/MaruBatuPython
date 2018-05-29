def print_list(list_val):
    for i in range(9):
        if (i+1)%3==0:
            print("|"+list_val[i]+"|");
        else:
           print("|"+list_val[i],end="");

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

def game_main():
    place=['1','2','3','4','5','6','7','8',"9"]
    counter =0
    while counter<9:
        print_list(place)

        write_val = input("○:1 or ×:2:")

        place_val = input("to :")
        if place_val[0]=="0":
            exit()
                    
        try:
            target_index=place.index(place_val[0])
        except ValueError:
            print("指定されたマスが見つかりませんでした。")
            continue
        try:
            if write_val[0] =="1":
                write="○"    
            elif write_val[0] =="2":
                write="×" 
            else:
                break;
            place.pop(target_index)
            place.insert(target_index,write)
        except :
            print("EXEPTIN")
            continue

        if "fin"==winner(place):
            break
        
        counter+=1
    return 1