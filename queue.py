from queue import Queue

queue = []

queue.append("1")
queue.append("2")
queue.append("3")
queue.append("4")


item = queue.pop(0)
for x in queue:
    print(x)
