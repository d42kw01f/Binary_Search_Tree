# This parent class allows to organize codes specially lin the main script which uses BTS and AVL.
class CreateTree:
    def __init__(self, data):
        self.root = data
        self.left_stree = None
        self.right_stree = None


class BinarySearchTree(CreateTree):
    def __init__(self, data):
        super().__init__(data)  # Initializing the Node from super class

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

    def leaf_node_checker(self, leaf_nodes=None, non_leaf_nodes=None):
        if leaf_nodes is None:
            leaf_nodes = []
        if non_leaf_nodes is None:
            non_leaf_nodes = []

        if self.left_stree:
            self.left_stree.leaf_node_checker(leaf_nodes, non_leaf_nodes)

        if self.right_stree is None and self.left_stree is None:
            leaf_nodes.append(self.root)
        else:
            non_leaf_nodes.append(self.root)

        if self.right_stree:
            self.right_stree.leaf_node_checker(leaf_nodes, non_leaf_nodes)

        return leaf_nodes, non_leaf_nodes

    # This is per order traversal function ===> Root => Left => Right
    def _per_order_traversal(self):
        tree_nodes = [self.root]  # Append root to the array

        if self.left_stree:  # If left node exists, Go to it.
            tree_nodes += self.left_stree._per_order_traversal()
        if self.right_stree:  # If Right tree exist, Go to it
            tree_nodes += self.right_stree._per_order_traversal()

        return tree_nodes


def creating_bst(given_arr):
    root = BinarySearchTree(given_arr[0])
    for i in range(1, len(given_arr)):
        root.insert_child(given_arr[i])
    return root


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        arr = [10, 8, 11, 2, 23, 13, 14, 16, 6, 4, 9]
        full_bst = creating_bst(given_arr=arr)
        leaf, non_leaf = full_bst.leaf_node_checker()
        print('Leaf Node: {}\nNon Leaf Nodes: {}'.format(leaf, non_leaf))
        # print(in_arr)

    except TypeError:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
