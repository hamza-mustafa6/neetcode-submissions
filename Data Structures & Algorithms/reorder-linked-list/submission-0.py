# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        index_map = {}
        map_head = head
        index = 0
        while map_head:
            index_map[index] = map_head
            index+=1
            map_head = map_head.next

        left = 0
        right = index - 1

        while left < right:
            index_map[left].next = index_map[right] 
            left+=1
            if left>= right:
                break
            index_map[right].next = index_map[left]
            right-=1 
        index_map[left].next = None

