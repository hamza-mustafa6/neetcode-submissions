# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        bfs_queue = deque()
        bfs_queue.append(root)

        level = 0
        while bfs_queue:
            for i in range(len(bfs_queue)):
                curr = bfs_queue.popleft()
                if curr.left:
                    bfs_queue.append(curr.left)
                if curr.right:
                    bfs_queue.append(curr.right)
            level+=1 
        return level