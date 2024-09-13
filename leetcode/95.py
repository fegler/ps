# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {} 
        for i in range(1, n+1):
            dp[(i, i)] = [TreeNode(i)]
        def recur(start, end):
            if (start, end) in dp:
                return dp[(start, end)]

            ret = []
            for i in range(start,end+1): ## root node
                left_trees, right_trees = [], []
                if i != start:
                    left_trees += recur(start, i-1)
                if i != end:
                    right_trees += recur(i+1, end)
                if i == start:
                    for r in right_trees:
                        root_node = TreeNode(i, right=r)
                        ret.append(root_node)
                else:
                    for l in left_trees:
                        if i == end:

                            root_node = TreeNode(i, left=l)
                            ret.append(root_node)
                        else:
                            for r in right_trees:
                                root_node = TreeNode(i, left=l, right=r)
                                ret.append(root_node)
            dp[(start, end)] = ret 
            return ret
        return recur(1, n)