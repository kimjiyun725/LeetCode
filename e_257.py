# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def binaryTreePaths(self, root):
    ans = []
    curr_path = []
    self.btHelper(root, curr_path, ans)
    
    return ans

def btHelper(self, root, curr_path, ans):
    
    curr_path.append(str(root.val))
    if not root.left and not root.right:
        ans.append('->'.join(curr_path))
    else:
        if root.left:
            self.btHelper(root.left, curr_path, ans)
        if root.right:
            self.btHelper(root.right, curr_path, ans)
        
    del curr_path[len(curr_path)-1]

# https://leetcode.com/problems/binary-tree-paths/
# Time Complexity: O(n) where n = amount of nodes in the binary tree
# Space Complexity: O((n+1)/2) aka O(logn) where n = amount of nodes in the binary tree
# and (n+1)/2 = amount of leaves in a complete binary tree which is the worst case scenario
