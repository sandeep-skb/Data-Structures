## Stack

class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, data):
    self.stack.append(data)
  
  def isEmpty(self):
    if len(self.stack) == 0:
      return True
    else:
      return False
  
  def pop(self):
    if self.isEmpty():
      print("Stack is empty, cannot pop. Please check implementation")
      return
    
    return self.stack.pop()


  def peek(self):
    if self.isEmpty():
      print("Stack is empty, cannot pop. Please check implementation")
      return

    return self.stack[len(self.stack)-1]    


mystack = Stack()
mystack.push(2)
mystack.push(3)
mystack.push(4)

print(mystack.peek())
print(mystack.pop())
print(mystack.pop())
print(mystack.isEmpty())
