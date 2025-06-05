class Solution(object):
    def isSubtree(self, root, subRoot):
        if not root:
            return False

        def match(r, s):
            if not r and not s:
                return True
            if not r or not s:
                return False
            if r.val != s.val:
                return False
            return match(r.left, s.left) and match(r.right, s.right)

        if match(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
