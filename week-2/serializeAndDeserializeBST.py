# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    def preorder(self, root):
        encode = ''
        stack, curr = [], root
        while stack or (curr is not None):
            if curr is not None:
                stack.append(curr)
                encode += str(curr.val) + ' '
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right
        return encode
    
    def decode(self, data, currMin, currMax):
        if data and currMin<data[0]<currMax:
            root = TreeNode(data.popleft())
            root.left = self.decode(data, currMin, root.val)
            root.right = self.decode(data, root.val, currMax)
            return root
    
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        encoded = self.preorder(root)
        return ' '.join(encoded.split())
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        data = deque(list(map(int, data.split())))
        return self.decode(data, float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans