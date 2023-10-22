x = 200

def myfunct():
    global x # inserting global means it access the variable as a whole
    x = 300
myfunct()

print(x)
