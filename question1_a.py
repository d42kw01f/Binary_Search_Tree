class CreateTree:
    def __init__(self, data):
        self.root = data
        self.left_node = None
        self.right_node = None


class BinarySearchTree(CreateTree):
    def __init__(self, data):
        super().__init__(data)  # Initializing the Node from super class

    def insert_child(self, data):
        if self.root is data:  # Check if data tries to add is already in the BST. If it is the case return nothing
            return

        if self.root > data:  # Check if the root is greater than data
            if self.left_node:  # If it is the case use, Check left node has any values by calling recursive methods.
                self.left_node.insert_child(data)
            else:  # Else simply add data to the left_node.
                self.left_node = BinarySearchTree(data)

        else:  # If data is greater than the root add data to right node like adding data to the left node.
            if self.right_node:
                self.right_node.insert_child(data)
            else:
                self.right_node = BinarySearchTree(data)

    # This function searches any given value in the node and return its object.
    def search_elements(self, val):
        if self.root is val:  # Check if root is the searching value.
            return self  # Then return its object
        if self.root > val:  # If searching value is less than the root, search left subtree
            if self.left_node:
                return self.left_node.search_elements(val)
            else:
                return None
        if self.root < val:  # if Searching value is grater than the root, search right subtree
            if self.right_node:
                return self.right_node.search_elements(val)
            else:
                return None

    # This function calculates the total number of nodes of the subtree rooted at N
    def modified_per_order(self, root_node):
        the_class = self.search_elements(root_node)  # First search N node in the BST and return its object
        if the_class is not None:
            arr = the_class._per_order_traversal()  # Use per-order traversal method to gets its subtree
            return arr
        return 'Could not find the element'

    # This is per order traversal function ===> Root => Left => Right
    def _per_order_traversal(self):
        elements = [self.root]  # Append root to the array

        if self.left_node:  # If left node exists, Go to it.
            elements += self.left_node._per_order_traversal()
        if self.right_node:  # If Right tree exist, Go to it
            elements += self.right_node._per_order_traversal()

        return elements


def creating_bst(arr):
    root = BinarySearchTree(arr[0])
    for i in range(1, len(arr)):
        root.insert_child(arr[i])
    return root


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
    return [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]


if __name__ == '__main__':
    try:
        the_arr = user_prompt()
        full_bst = creating_bst(the_arr)
        print('\33[32m' + '\n\nAnd Here is the Sorted Array: ' + '\033[0m')
        print(f'\t--> \33[34m{the_arr}\033[0m')
        user_node = int(input('\n\n---> Enter N: '))
        sub_tree = full_bst.modified_per_order(user_node)
        print(sub_tree)
    except TypeError:
        print('\033[91m' + "Error!!!, Hmm Something Went Wrong!!!" + '\033[0m')
