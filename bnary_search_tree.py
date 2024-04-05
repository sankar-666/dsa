class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if data > root.data:
            root.right = self._insert(root.right, data)
        elif data < root.data:
            root.left = self._insert(root.left, data)
        return root

    def contains(self, key):
        return self._contains(self.root, key)
    
    def _contains(self, root, key):
        if root is None:
            return False
        if  root.data == key:
            return True
        if key <  root.data:
            return self._contains(root.left, key)
        return self._contains(root.right, key)
    
    # left, root, right
    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    
    def _inorder_traversal(self, root, result):
        if root: 
            self._inorder_traversal(root.left, result)
            result.append(root.data)
            self._inorder_traversal(root.right, result)

    # root, left, right
    def preorder_traversal(self):
        result  = []
        self._preorder_traversal(self.root, result)
        return result
    
    def _preorder_traversal(self, root, result):
        if root:
            result.append(root.data)
            self._preorder_traversal(root.left, result)
            self._preorder_traversal(root.right, result)

    # left, right, root
    def postorder_traversal(self):
        result  = []
        self._postorder_traversal(self.root, result)
        return result
    
    def _postorder_traversal(self, root, result):
        if root:
            self._postorder_traversal(root.left, result)
            self._postorder_traversal(root.right, result)
            result.append(root.data)


    def delete(self, data):
        self.root = self._delete(self.root, data)

    def _delete(self, node, data):
        if node is None:
            return  node
        
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_value = self.find_min(node)
                node.data = min_value
                node.right = self._delete(node.right, min_value)
        return node
            
    def find_min(self, node):
        while node.left:
            node = node.left
        return node
    
    @staticmethod
    def multiple_sum(*args):
        sum = 0
        for i in args:
            sum+=i
        return sum
    
    # def close_value(self, data):
    #     return self._close_value(self.root, None, data)

    # def _close_value(self, current_node, parent_node, data):
    #     if current_node is None:
    #         return current_node
        
    #     if data < current_node.data:
    #         return self._close_value(current_node.left, current_node, data)
    #     elif data > current_node.data:
    #         return self._close_value(current_node.right, current_node, data)
    #     else: 
    #         if current_node.left is not None and current_node.right is not None:
    #             left_shift = abs(data - current_node.left.data)
    #             right_shift = abs(data - current_node.right.data)
    #             parent_shift = abs(data - parent_node.data)
    #             if left_shift <= right_shift and left_shift <= parent_shift:
    #                 return current_node.left.data
    #             elif right_shift <= left_shift and right_shift <= parent_shift:
    #                 return current_node.right.data
    #             else:
    #                 return parent_node.data
    #         elif current_node.left is None and current_node.right is not None:
    #             right_shift = abs(data - current_node.right.data)
    #             parent_shift = abs(data - parent_node.data)
    #             if right_shift <= parent_shift:
    #                 return current_node.right.data
    #             else:
    #                 return parent_node.data
    #         elif current_node.right is None and current_node.left is not None:
    #             left_shift = abs(data - current_node.left.data)
    #             parent_shift = abs(data - parent_node.data)
    #             if left_shift <= parent_shift:
    #                 return current_node.left.data
    #             else:
    #                 return parent_node.data
    #         else:
    #             return parent_node.data
            

    def closest_value(self, data):
        return self._closest_value(self.root, data)

    def _closest_value(self, current_node, data):
        if current_node is None:
            return None
        
        closest = current_node.data
        
        while current_node:
            if current_node.data == data:
                return current_node.data
            if abs(current_node.data - data) < abs(closest - data):
                closest = current_node.data
            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        return closest



bst = BinarySearchTree()

bst.insert(10)
bst.insert(8)
bst.insert(11)
bst.insert(4)
bst.insert(9)

print(bst.inorder_traversal())
# print(bst.preorder_traversal())
# print(bst.postorder_traversal())

print(bst.closest_value(5))