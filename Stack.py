class Stack:
  def __init__(self, size:int):
    self.data = [None]*size
    self.size = size
    self.pointer = 0
    
  def __str__(self):
    return str(self.data[:self.pointer])

    
  def isFull(self):
    if self.size == self.pointer:
      return True
    else:
      return False
      
  def isEmpty(self):
    if self.pointer == 0:
      return True
    else:
      return False
      
  def push(self, to_add):
    if not self.isFull():
      self.data[self.pointer]= to_add
      self.pointer += 1
    else:
      raise Exception("stack overflow error")
      
  def pop(self):
    if not self.isEmpty():
      
      self.pointer -= 1
      return self.data[self.pointer]
    else:
      raise Exception("stack undereflow error")
