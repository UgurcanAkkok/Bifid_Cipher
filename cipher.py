#!/usr/bin/python
## A encryption algorithm
table_letter ="ABCDEFGHIKLMNOPQRSTUVWXYZ"
table_coordinate = [[1,1],[1,2],[1,3],[1,4],[1,5],[2,1],[2,2],[2,3],[2,4],[2,5],[3,1],[3,2],[3,3],[3,4],[3,5],[4,1],[4,2],[4,3],[4,4],[4,5],[5,1],[5,2],[5,3],[5,4],[5,5]]
while True:
    print("Do you want to encrypt or decrypt?")
    option = input("(e/d/quit)\n>")

    if option == "e":
        etext = input("Enter the text you want to encrypt. \n>")
        #print(etext)
        letters = []
        for l in etext[:]:
            letters.append(l.upper())
            #print(l)
        letters = letters
        coor = []
        for i in letters:
            coor.append(table_coordinate[table_letter.index(i)])
        print("coor=",coor)
        x_coor = []
        y_coor = []
        for x in coor:
            x_coor.append(x[0])
        for y in coor:
            y_coor.append(y[1])
        print("x and y coor =",x_coor,"\n",y_coor)
        new_coor = [] 

        for x in x_coor:
            new_coor.append(x)
        for y in y_coor:
            new_coor.append(y)

        temp_coors = []
        c = 0
        print("new coor1=",new_coor)
        for i in range(int(len(new_coor)/2)):
            temp_coors.append([new_coor[c],new_coor[c+1]])
            c +=2
        new_coor = temp_coors
        print("new coor2=",new_coor)  
        encrypted= [table_letter[table_coordinate.index(i)] for i in new_coor]
        encrypted_text = "".join(i for i in encrypted)
        print("encrypted = ",encrypted_text)
        
    elif option =="d":
        dtext = input("Enter the text you want to decrypt. \n>")
        dtext = dtext.upper()
        dcoor = []
        for ch in dtext:
            dcoor.append(table_coordinate[table_letter.index(ch)])
        new_coor= []
        for c in dcoor:
            new_coor.append(c[0])
            new_coor.append(c[1])
        #print(new_coor)
        temp_coor = []
        for i in range(int(len(new_coor) / 2 )): 
            temp_coor.append([new_coor[i],new_coor[i + int(len(new_coor)/2)]])
        
        new_coor = temp_coor
        #print(dcoor)
        #print(new_coor)
        decrypted = [table_letter[table_coordinate.index(i)] for i in new_coor]
    
        decrypted_text = "".join(i for i in decrypted)
        print("decrypted text:",decrypted_text)
    elif option == "quit" or option == "q":
        break
    else:
        print("Try with lower case e or d")
        pass
    
    
