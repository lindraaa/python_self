x = lambda a, b ,c  : a+b+c
print(x(1,2,3))





def myfunction (x):
    return lambda n : n *x 

double = myfunction(2)

print("hi", double(11))


product = lambda a, b=1 , c=2 :a+b+c
print(product(3))
