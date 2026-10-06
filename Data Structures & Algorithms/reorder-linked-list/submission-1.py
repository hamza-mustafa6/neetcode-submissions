# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #slow and fast pointers to find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #reverse 2nd half
        prev = None
        curr = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        #prev is head of reversed linkedlist

        slow.next=None

        right = prev
        left = head

        while right:
            temp_l= left.next
            temp_r = right.next
            left.next = right
            right.next = temp_l

            left = temp_l
            right = temp_r

            

        # 1 -> 2 -> 3  4 <- 5 


        #1 -> 5 -> 2
        #
        
