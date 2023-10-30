def recurs(num):
    if num == 0:
        return
    else:
        print(num)
        recurs(num-1)


recurs(5)

