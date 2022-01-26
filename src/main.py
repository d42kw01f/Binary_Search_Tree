# This parent class allows to organize codes specially lin the main script which uses BTS and AVL.
class CreateTree:
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class BinarySearchTree(CreateTree):
    def __init__(self, data):
        super().__init__(data)  # Initializing the tree from super class

    def insert_child(self, data):
        if self.root is data:  # Check if data tries to add is already in the BST. If it is the case return nothing
            return

        if self.root > data:  # Check if the root is greater than data
            if self.left_stree:  # If it is the case use, Check left node has any values by calling recursive methods.
                self.left_stree.insert_child(data)
            else:  # Else simply add data to the left_node.
                self.left_stree = BinarySearchTree(data)

        else:  # If data is greater than the root add data to right node like adding data to the left node.
            if self.right_stree:
                self.right_stree.insert_child(data)
            else:
                self.right_stree = BinarySearchTree(data)

    # This is per order traversal function ===> Root => Left => Right
    def _per_order_traversal(self):
        tree_nodes = [self.root]  # Append root to the array

        if self.left_stree:  # If left node exists, Go to it.
            tree_nodes += self.left_stree._per_order_traversal()
        if self.right_stree:  # If Right tree exist, Go to it
            tree_nodes += self.right_stree._per_order_traversal()

        return tree_nodes

    # This function searches any given value in the node and return its object.
    def search_elements(self, val):
        if self.root is val:  # Check if root is the searching value.
            return self  # Then return its object
        if self.root > val:  # If searching value is less than the root, search left subtree
            if self.left_stree:
                return self.left_stree.search_elements(val)
            else:
                return None
        if self.root < val:  # if Searching value is grater than the root, search right subtree
            if self.right_stree:
                return self.right_stree.search_elements(val)
            else:
                return None

    # This function calculates the depth of the subtree rotted at N.
    def sub_tree_depth(self, given_node):
        tree_obj = self.search_elements(given_node)  # Search the given_node using and return its object
        depth_n_node = tree_obj.depth()  # calculating the depth of the subtree which rooted at N
        return depth_n_node

    # This function calculates the depth of a given tree
    def depth(self):
        left_depth = self.left_stree.depth() if self.left_stree else 0
        right_depth = self.right_stree.depth() if self.right_stree else 0
        return max(left_depth, right_depth) + 1

    # This is per order traversal function ===> Left => Right => Root
    def post_order_traversal(self):
        tree_nodes = []

        if self.left_stree:  # If left exit, travel
            tree_nodes += self.left_stree.post_order_traversal()
        if self.right_stree:  # if right exist, travel
            tree_nodes += self.right_stree.post_order_traversal()
        tree_nodes.append(self.root)  # append the root to the array

        return tree_nodes


# This function create the Binary Search Tree.
def construct_bst(given_arr):
    root = BinarySearchTree(given_arr[0])  # Create and Object of BinarySearchTree
    for i in range(1, len(given_arr)):
        root.insert_child(given_arr[i])  # Insert nodes to the BST one by one
    return root


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        arr = [10, 8, 11, 2, 23, 13, 14, 16, 6, 4, 9]
        full_bst = construct_bst(given_arr=arr)
        depth_tree = full_bst.depth()
        print('Full Depth of the Tree', depth_tree)

        n_depth_stree = full_bst.sub_tree_depth(8)
        print(n_depth_stree)

    except TypeError:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
