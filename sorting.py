myList = []
even = 0


while len(myList) < 9:
    try:
        number = int(input("Enter a number: "))
        myList.append(number)
        continue
    except ValueError:
        print('Wrong Input...')

        
for y in myList:
     if y % 2 == 0:
        even +=1
print("Number of even numbers: " ,even)

for y in myList:
    if y % 2 == 0:
    
     count = myList.index(y)
     print("Index [",count,"]: ",y)

#5 6 1 7 2 3 0 4 7 2 
#6 1 3 5 7 9 4 0 2 3

listA = input("Enter 10 numbers for list A: ").split()
listA =[int(num1)for num1 in listA ]

listB = input("Enter 10 numbers for list B: ").split()
listB =[int(num2)for num2 in listB ]

first5 = listA[0:5]
last5 = listB[5:10]

print("First five numbers of list A : ",*first5,sep=' ')
print("Last five numbers of list B: ",*last5, sep=' ')

combined = first5 + last5

print("Combined numbers: ", *combined, sep=' ')

combined.sort()
print("Reversed order: ",*combined, sep=' ')


