# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # 1 - > 2 -> 3 -> 4 -> 2 -> 3 -> 4... 
        id_map = {}
        pointer = head
        while pointer:
            if id(pointer) in id_map:
                return True
            id_map[id(pointer)] = id(pointer.next)
            pointer = pointer.next
        return False