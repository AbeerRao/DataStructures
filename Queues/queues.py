#* The queue class
class Queue:
    #* The constructor
    def __init__(self):
        self.queue = []
    #? Is the queue empty
    #* Method
    def is_empty(self):
        if self.queue == []:
            return True
        else:
            return False
    #* Enqueue method
    def enqueue(self, data):
        self.queue.append(data)
        return data
    #* Dequeue method
    def dequeue(self):
        if self.sizeQ() != 0:
            data = self.queue[0]
            del(self.queue[0])
            return data
        else:
            return -1
    #* The peek function
    def peek(self):
        return self.queue[0]
    #* The size method
    def sizeQ(self):
        return len(self.queue)

#* Making an instance
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(15)
print(f"Current queue: {queue.queue}")
print(f"Enqueued item: {queue.enqueue(5)}")
print(f"Dequeued item: {queue.dequeue()}")
print(f"The size of the queue: {queue.sizeQ()}")
#* Removing all the itmes through iteration
for x in range(queue.sizeQ()):
    print("Iterating... Removed")
    queue.dequeue()
print(f"The size of the queue: {queue.sizeQ()}")
print(f"Is the queue empty? {queue.is_empty()}")