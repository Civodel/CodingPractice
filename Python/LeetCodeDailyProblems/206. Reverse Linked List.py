'''Given the head of a singly linked list, reverse the list, and return the reversed list.'''
from typing import Optional


#Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        previous_node = None
        current_node = head
        next_node = None
        while current_node: #while current node is different from None loop continues
            next_node = current_node.next #takes the next current node in the practical case is the object listnode(2)
            current_node.next = previous_node #switch the link to the previus node wich is none, before this was 2
            previous_node = current_node #previus node takes current value (2)
            current_node = next_node #current node becomes next node (2

        return previous_node#as head of thereversed linked list




head = ListNode(1)
current = head
for i in range(2, 6):
    current.next = ListNode(i)
    current = current.next


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print_linked_list(head)
if __name__ == '__main__':

    reverse_head=print(Solution().reverseList(head))



