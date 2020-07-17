#* The stack class
class Stack:
    #* The constructor
    def __init__(self):
        self.stack = [] #* Making the stack a 1-D array
    #* The push method
    def push(self, data):
        self.stack.append(data) #* Appending data to the stack
        return data
    #* The pop method
    def pop(self):
        data = self.stack[-1]
        del(self.stack[-1]) #* Removing the last item from the stack
        return data
    #* The peek method
    def peek(self):
        data = self.stack[-1]
        return data
    #* Checking if the stack is empty
    def is_empty(self):
        return self.stack == []
    #* Getting the size of the stack
    def size(self):
        length = len(self.stack)
        return length

#* Making an instance of the stack
stack = Stack()
#* Running operations on it
stack.push(3)
stack.push(2)
stack.push(1)
print(f"Stack size : {stack.size()}")
print(f"Popped item : {stack.pop()}")
print(f"Peeked item : {stack.peek()}")
print(f"Pushed item : {stack.push(3)}")
print(f"Whole stack : {stack.stack}")
#* Removing all the items through iterating
for x in range(stack.size()):
    print("Iterating... Deleted")
    stack.pop()
print(f"Now the stack size is : {stack.size()}")
print(f"Is the stack empty? {stack.is_empty()}")