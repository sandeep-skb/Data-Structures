#Implement a binary heap:

class MaxHeap:
  def __init__(self):
    self.heap = []
    self.count = 0
  
  def parent(self, i):
    if (i-1)//2 >= 0:
      return ((i-1)//2)
    else:
      return -1
  
  def left_child(self, i):
    if (2*i+1) < self.count:
      return (2*i+1)
    else:
      return -1

  def right_child(self, i):
    if (2*i+2) < self.count:
      return (2*i+2)
    else:
      return -1


  def insert(self, k):
    self.heap.append(k)
    self.count += 1
    self.percolateUP(self.count-1)
  
  def percolateUP(self, i):
    p_idx = self.parent(i)
    if p_idx == -1:
      return

    if self.heap[p_idx] < self.heap[i]:
      temp = self.heap[i]
      self.heap[i] = self.heap[p_idx]
      self.heap[p_idx] = temp
      self.percolateUP(p_idx)


  def deleteMax(self):
    if self.count == 0:
      return -1
    data = self.heap[0]
    if self.count >= 1:
      self.heap[0] = self.heap[-1]
      self.heap.pop()
      self.count -= 1
      self.percolateDown(0)
    
    return data

  def percolateDown(self, i):
    if self.count == 0:
      return
    r_idx = self.right_child(i)
    l_idx = self.left_child(i)
    max_id = i

    if (r_idx != -1 and self.heap[i] < self.heap[r_idx]):
      max_id = r_idx
    else:
      max_id = i

    if (l_idx != -1 and self.heap[max_id] < self.heap[l_idx]):
      max_id = l_idx
   
    if (max_id != i):
      temp = self.heap[max_id]
      self.heap[max_id] = self.heap[i]
      self.heap[i] = temp
      self.percolateDown(max_id)   

#Driver code
def main():
  max_heap = MaxHeap()
  max_heap.insert(31)
  max_heap.insert(10)
  max_heap.insert(21)
  max_heap.insert(9)
  max_heap.insert(8)
  max_heap.insert(12)
  max_heap.insert(18)
  max_heap.insert(3)
  max_heap.insert(2)
  max_heap.insert(7)
  
  print(max_heap.heap)
  print()

  print("Deleting Max")
  max_heap.deleteMax()
  print(max_heap.heap)


if __name__ == "__main__":
  main()
