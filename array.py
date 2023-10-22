#arrays DATALSGO
import os

f_array = [10, 12,20,22,30,32,40,42,50,52]
while True:
    os.system("cls")
    
    print("[a] Add an element <at the end> ")
    print("[b] Insert an element <on specific index>" )
    print("[c] Edit an element <on specific index")

    x = input("Enter the letter of your choice: ")

    if x == "a":
        os.system("cls")
        y = input("Enter the new element: ")
        f_array.append(y)
        print("The new list of the elements are the following:")
        for i in f_array:
            print(i)
       
        tg = input("Try again? [y][n]: ")
        while tg.lower() not in ("y","n"):
             tg = input("Try again? [y][n]: ")
        if tg == "n":
            os.system("cls")
            break
    elif(x =="b"):
        y = int(input("Enter the element to be inserted: "))
        z = int(input("Enter the position of inserted element: "))
        f_array.insert(z,y)
        print("The new list of the elements are the following:")
        for i in f_array:
            print(i)

        tg = input("Try again? [y][n]: ")
        while tg.lower() not in ("y","n"):
             tg = input("Try again? [y][n]: ")
        if tg == "n":
            os.system("cls")
            break

    elif(x=="c"):
        y = int(input("Enter the index position to be edit: "))
        z =int(input("Enter the new value: "))

        f_array.insert(y,z)
        f_array.pop(y+1)
        print("The new list of the elements are the following:")
        for i in f_array:
            print(i)
        
        tg = input("Try again? [y][n]: ")
        while tg.lower() not in ("y","n"):
             tg = input("Try again? [y][n]: ")
        if tg == "n":
            os.system("cls")
            break
        
        
