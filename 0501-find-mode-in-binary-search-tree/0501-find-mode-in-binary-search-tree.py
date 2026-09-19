# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans = {}
        mode = []
        queue = deque()
        if root is None:
            return None
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.val not in ans:
                ans[node.val] = 1
            else:
                ans[node.val]+=1
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        max_freq = max(ans.values())
        for key,values in ans.items():
            if values == max_freq:
                mode.append(key)
        return mode

