import sys


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

    # =====================================Traversal Functions =============================================================

    # This is per order traversal function ===> Root => Left => Right
    def per_order_traversal(self):
        tree_nodes = [self.root]  # Append root to the array

        if self.left_stree:  # If left node exists, Go to it.
            tree_nodes += self.left_stree.per_order_traversal()
        if self.right_stree:  # If Right tree exist, Go to it
            tree_nodes += self.right_stree.per_order_traversal()

        return tree_nodes

    #  This is in order traversal function ===> Left => Root => Right
    def in_order_traversal(self):
        tree_nodes = []

        if self.left_stree:  # If left tree exist, vist
            tree_nodes += self.left_stree.in_order_traversal()

        tree_nodes.append(self.root)  # Append root to the array

        if self.right_stree:  # If left tree exist, vist
            tree_nodes += self.right_stree.in_order_traversal()

        return tree_nodes

    # This is per order traversal function ===> Left => Right => Root
    def post_order_traversal(self):
        tree_nodes = []

        if self.left_stree:  # If left exit, travel
            tree_nodes += self.left_stree.post_order_traversal()
        if self.right_stree:  # if right exist, travel
            tree_nodes += self.right_stree.post_order_traversal()
        tree_nodes.append(self.root)  # append the root to the array

        return tree_nodes

    # ===============================Leaf and Non-Leafs ====================================================================
    # This function should be changed before submitting.
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

    # ==================================================================================================
    # This function deletes a given node from the tree
    def delete_node(self, del_node):
        if self.root == del_node:
            if self.right_stree and self.left_stree:
                # First, this retrieve the successor node and its parent
                [parent_min, min_node] = self.right_stree._find_min_node(self)
                # splice out the successor
                if parent_min.left == min_node:
                    parent_min.left = min_node.right
                else:
                    parent_min.right = min_node.right
                # reset the left and right children of the successor
                min_node.left = self.left_stree
                min_node.right = self.right_stree
                return min_node
            else:
                if self.left_stree:
                    return self.left_stree  # promote the left subtree
                else:
                    return self.right_stree  # promote the right subtree
        else:
            if self.root > del_node:  # key should be in the left subtree
                if self.left_stree:
                    self.left_stree = self.left_stree.delete_node(del_node)
            else:  # key should be in the right subtree
                if self.right_stree:
                    self.right_stree = self.right_stree.delete_node(del_node)

        return self

    # This function returns the minimum node and its parent.
    def _find_min_node(self, parent):
        if self.left_stree:
            return self.left_stree._find_min_node(self)
        else:
            return [parent, self]

    # This function calculates the total number of nodes of the subtree rooted at N
    def sub_tree_nodes(self, root_node):
        tree_obj = self.search_elements(root_node)  # First search N node in the BST and return its object
        if tree_obj is not None:
            arr = tree_obj.per_order_traversal()  # Use per-order traversal method to gets its subtree
            return arr
        return None

    # This function calculates the depth of the subtree rotted at N.
    def sub_tree_depth(self, given_node):
        tree_obj = self.search_elements(given_node)  # Search the given_node using and return its object
        if tree_obj:
            depth_n_node = tree_obj.depth()  # calculating the depth of the subtree which rooted at N
            return depth_n_node
        return None

    # This function calculates the depth of a given tree
    def depth(self, node=None, depth=1):
        if node is not None:
            if self.root == node:
                return depth
        left_depth = self.left_stree.depth(node, depth + 1) if self.left_stree else 0
        right_depth = self.right_stree.depth(node, depth + 1) if self.right_stree else 0
        if node is not None:
            return max(left_depth, right_depth)
        return max(left_depth, right_depth) + 1

    # This function display the created BST tree
    def display_bst_tree(self, currPtr, indent, left):
        if currPtr is not None:
            sys.stdout.write(indent)
            if left:
                sys.stdout.write("R--->")
                indent += "     "
            else:
                sys.stdout.write("L--->")
                indent += "|     "
            print(currPtr.root)
            self.display_bst_tree(currPtr.left_stree, indent, False)
            self.display_bst_tree(currPtr.right_stree, indent, True)
