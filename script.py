class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def get_data(self):
        return self.data

    def __repr__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        def _insert(root, data):
            if root is None:
                return Node(data)

            if data < root.data:
                root.left = _insert(root.left, data)
            if data > root.data:
                root.right = _insert(root.right, data)
            return root

        self.root = _insert(self.root, data)

    def find_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


    def delete(self, data):
        def _delete(root, data):
            if root is None:
                return root

            if data < root.data:
                root.left = _delete(root.left, data)
            elif data > root.data:
                root.right = _delete(root.right, data)
            else:
                if root.left is None:
                    return root.right
                if root.right is None:
                    return root.left

                temp = self.find_min_value_node(root.right)
                root.data = temp.data
                root.right = _delete(root.right, temp.data)

            return root

        self.root = _delete(self.root, data)

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)
        print(f"Node {node.data}: left = {left_height}, right = {right_height}")
        return 1 + max(left_height, right_height)



    def inorder(self):
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data, end=" ")
                _inorder(node.right)

        _inorder(self.root)
        print()

    def preorder(self):
        def _preorder(node):
            if node:
                print(node.data,  end=" ")
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)
        print()

    def postorder(self):
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.data, end=" ")
        _postorder(self.root)
        print()

btree = BinaryTree()

btree.insert(2)
btree.insert(1)
btree.insert(3)
btree.inorder()
btree.preorder()
btree.postorder()
btree.delete(3)
btree.inorder()
print(btree.height(btree.root))