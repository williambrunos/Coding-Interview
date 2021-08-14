'''
LEETCODE

Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
              aux = head
              v = []
              while aux != None:
                v.append(aux.val)
                aux = aux.next

              size = len(v)
              if n >= 1 and size > 1:
                if ((n <= size) and (n > 0)):
                  aux = head
                  prev = aux
                  if((size-n) != 0):
                    for count in range(size - n):
                        prev = aux 
                        aux = aux.next
                    prev.next = aux.next
                  else:
                    aux = aux.next
                    head = aux

                  return head
                else:
                  return None
              else:
                return None