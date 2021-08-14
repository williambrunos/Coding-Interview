class listNode:
  def __init__(self, val = 0, next = None):
    self.val = val 
    self.next = next
    
  def print_list(head = None):
    if head != None:
      aux = head 
      while aux != None:
        print(aux.val)
        aux = aux.next