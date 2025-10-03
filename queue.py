queue = []

queue.append('g')
queue.append('f')
queue.append('g')

print("Initial queue")
print(queue)

print("Elements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("Queue after removing elements")
print(queue)
