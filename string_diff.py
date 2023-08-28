def string_test():
    count = 0
    uppercase = 0
    lowercase = 0
    
    string1 = input("Enter a character: ")
    print("Original String: ",string1)
    
    for x in string1:
        if x.isupper():
            uppercase = uppercase +1
    print("No. of Upper Case Characters: ",uppercase)

    for y in string1:
        if y.islower():
            lowercase = lowercase + 1 
    print("No. of Lower Case Characters: ",lowercase)
    
    for i in string1:
        if(i.isdigit()):
              count = count +1
    
    print("No. of Integers: ",count)


string_test()
