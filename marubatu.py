
place=['1','2','3','4','5','6','7','8',"9"]

def print_list(list_val):
    for i in range(9):
        if (i+1)%3==0:
            print("|"+list_val[i]+"|");
        else:
           print("|"+list_val[i],end="");

def winner(list_val):
    if place[0]==place[1] and place[1]==place[2]:
        print (" Win:%c" % (place[0]))
    elif place[0]==place[4] and place[8]==place[9]:
        print (" Win:%c" % (place[0]))
    elif place[0]==place[3] and place[3]==place[6]:
        print (" Win:%c" % (place[0]))
    elif place[1]==place[4] and place[4]==place[8]:
        print (" Win:%c" % (place[1]))
    elif place[2]==place[4] and place[4]==place[6]:
        print (" Win:%c" % (place[2]))
    elif place[2]==place[5] and place[5]==place[8]:
        print (" Win:%c" % (place[2]))
    elif place[3]==place[4] and place[4]==place[5]:
        print (" Win:%c" % (place[3]))
    elif place[6]==place[7] and place[7]==place[8]:
        print (" Win:%c" % (place[6]))
    else:
        return "not fin"
    return "fin"
            


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
        