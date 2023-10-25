#Sets
#Access
set1 = {"A","B","C"}
set2 = {"W","X","Y"}
list1 = [1,2,3,4,5]


print(set1)
print(len(set1))

print(type(set1))

for x in set1:
    print(x)

print("B" in set1)

#Add set

set1.add("D")
print(set1)

set1.update(set2)
print(set1)

set1.update(list1) #adding sets to list or vice versa
print(set1)

#Removing in sets
set3 = {"A","B","C"}
set3.remove("A") #to delete
print(set3)    
set3.discard("C") #to delete
print(set3)
