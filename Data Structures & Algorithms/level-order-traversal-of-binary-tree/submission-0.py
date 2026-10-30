# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #checking the level_size at the start ensures we can dequeue one level at a time.

        if not root:
            return []
        q = deque([root])
        level_order = []

        while q:
            level_size = len(q)
            temp_list = []
            for _ in range(level_size):
                curr = q.popleft()
                temp_list.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level_order.append(temp_list)
        return level_order