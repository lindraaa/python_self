def string_test():
    count = 0
    uppercase = 0
    lowercase = 0
    special = 0

    string1 = str(input("Enter a character: "))
    print("Original String: ",string1)
    
    string2 = string1.replace(" ", "")

    for x in string2 :
        if x.isupper():
            uppercase = uppercase+ + 1
        elif x.islower():
            lowercase = lowercase + 1
        elif x.isdigit():
            count = count + 1
        else:
            special = special + 1 



    print("No. of Upper Case Characters: ",uppercase)
    print("No. of Lower Case Characters: ",lowercase)
    print("No. of Integers: ",count)
    print("No. of Special Characters: ",special)

string_test()
