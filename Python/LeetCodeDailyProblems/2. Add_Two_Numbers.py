# Definition for singly-linked list.{
'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.'''
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2 ) :
        # Initialize a dummy node and a current pointer
        dummy = ListNode()
        curr = dummy
        # Initialize carry to 0
        carry = 0

        # Traverse both linked lists until we reach the end of both
        while l1 or l2 or carry:
            # Obtain the values of the current nodes in l1 and l2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of values along with the carry
            val = val1 + val2 + carry

            # Update carry for the next iteration
            carry = val // 10

            # Calculate the new digit to be added to the result
            val = val % 10

            # Create a new node with the calculated digit and update the current pointer
            curr.next = ListNode(val)

            # Move to the next nodes in both l1 and l2
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        # Return the next node of the dummy node, which is the head of the resulting linked list
        return dummy.next
