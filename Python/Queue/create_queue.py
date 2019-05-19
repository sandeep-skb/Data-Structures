class Queue:
  def __init__(self):
    self.queue = []

  def enqueue(self, data):
    self.queue.append(data)
  
  def dequeue(self):
    self.queue.pop(0)
  
  def rear(self):
    return self.queue[-1]
  
  def front(self):
    return self.queue[0]
  

myqueue = Queue()
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(4)
myqueue.enqueue(5)
myqueue.enqueue(6)
print("front of the queue: ", myqueue.front())
print("rear of the queue: ", myqueue.rear())
myqueue.dequeue()
print()
print("Dequeueing, this will remove the current first element in the queue")
print("front of the queue after dequeue: ", myqueue.front())
