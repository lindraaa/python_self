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

#loop sets
set4 = {1,2,3,4,5}
set5 = {"A","B","C"}
for x in set4:
    print(x)

#join sets

set6 = set4.union(set5) 
print(set6)

set4.update(set5)
print(set4)

set7 = {1,2,3,4,5}
set8 ={1,7,6,8}

set7.intersection_update(set8)
print(set7)

