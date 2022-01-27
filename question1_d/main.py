import os
import binary_tree_search as bst


# This function create the Binary Search Tree.
def construct_bst(given_arr):
    root = bst.BinarySearchTree(given_arr[0])  # Create and Object of BinarySearchTree
    for i in range(1, len(given_arr)):
        root.insert_child(given_arr[i])  # Insert nodes to the BST one by one
    return root


# This function will clear the terminal once it's called.
def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


def user_prompt():
    arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
    user_int = [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
    print(
        '\33[93m' + '\nNOTE: BST only works with distinct values. Thus, Duplicates values. They will be automatically removed.' + '\33[0m')
    return list(dict.fromkeys(user_int))


def user_options():
    clear_console()
    print(
        '1.) Per-load a sequence of integers to build a BST\n2.) Manually enter integer values/keys, one by one to build a BST\n3.) Exit')
    try:
        user_choice = int(input('Enter your option here: '))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        return user_options()
    if user_choice == 1:
        user_arr = [54, 80, 64, 19, 34, 78, 22, 13, 20, 102, 91, 44, 84, 50, 46, 47, 49, 45]
    elif user_choice == 2:
        user_arr = user_prompt()
    else:
        exit()
    # noinspection PyUnboundLocalVariable
    return user_arr


def input_int():
    try:
        the_int = int(input('Enter Search Value: '))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
    # noinspection PyUnboundLocalVariable
    return the_int


def main_menu(obj_bst):
    clear_console()
    print(""" 
    1.\tPrint the per-order, in-order and post-order of the BST, in sequence
    2.\tPrint all leaf nodes of the BST, and all non-leaf nodes
    3.\tPrint the total number of nodes of a sub-tree 
    4.\tPrint the depth of a node in the BST
    5.\tPrint the depth of a subtree rooted at a particular node
    6.\tInsert a new inter key into the BST
    7.\tDelete an integer key from the BST
    8.\tExit
    """)
    try:
        menu_choice = int(input('Enter your option here: '))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        main_menu(obj_bst)
    # noinspection PyUnboundLocalVariable
    match menu_choice:
        case 1:
            per_order = obj_bst.per_order_traversal()
            in_order = obj_bst.in_order_traversal()
            post_order = obj_bst.post_order_traversal()
            print('===' * 30)
            print('per-order traversal : \n\t{}'.format(per_order))
            print('in-order traversal : \n\t{}'.format(in_order))
            print('post-order traversal : \n\t{}'.format(post_order))
            print('===' * 30)

        case 2:
            leafs, non_leafs = obj_bst.leaf_node_checker()
            print('===' * 30)
            print('Leaf Nodes are: \n\t{}'.format(leafs))
            print('Non-Leaf Nodes are: \n\t{}'.format(non_leafs))
            print('===' * 30)

        case 3:
            print('===' * 30)
            node_n = input_int()
            stree = obj_bst.sub_tree_nodes(root_node=node_n)
            print(f'number of nodes of {node_n} subtree')
            if stree:
                print(stree)
                return
            print('\t' + '\33[41m' + f'ERROR: Node {node_n} not found!' + '\33[0m')
            print('===' * 30)

        case 4:
            print('===' * 30)
            node_n = input_int()
            node_depth = obj_bst.depth(node_n)
            if node_depth != 0:
                print(node_depth)
                return
            print('\t' + '\33[41m' + f'ERROR: Node {node_n} not found!' + '\33[0m')
            print('===' * 30)

        case 5:
            print('===' * 30)
            node_n = input_int()
            print(f'depth of {node_n} in the BST is: ')
            stree_depth = obj_bst.sub_tree_depth(given_node=node_n)
            if stree_depth:
                print('\t', stree_depth)
                return
            print('t' + '\33[41m' + f'ERROR: Node {node_n} not found!' + '\33[0m')
            print('===' * 30)

        case 6:
            print('===' * 30)
            insert_int = input_int()
            obj_bst.insert_child(insert_int)
            print('Successfully inserted element in to the tree')
            print('===' * 30)

        case 7:
            print('===' * 30)
            print('Under Construction')

        case 8:
            exit()


if __name__ == '__main__':
    seq_int = user_options()
    print()
    print('===' * 30)
    print('sequence of integers for BST would be: \n\t{}'.format(seq_int))
    print('===' * 30)
    input('\nPress Enter to continue...')
    full_bst = construct_bst(seq_int)
    while True:
        main_menu(full_bst)
        input('\n\tPress Enter to continue...')
