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
    while True:
        try:
            arr_elem = int(input('\x1b[6;30;42m' + '---> Number of Elements in the Array:' + '\x1b[0m' + ' '))
            user_int = [int(input(f"\tEnter Elem {ArrNum}: ")) for ArrNum in range(arr_elem)]
            break
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
    print(
        '\33[93m' + '\nNOTE: BST only works with distinct values. Thus, Duplicates values. They will be automatically removed.' + '\33[0m')
    return list(dict.fromkeys(user_int))


def program_exit():
    try:
        print('\t\t\t\U0001F600 Thanks for using this\n\t\t\tLive Long and Prosper \U0001F596')
    except:
        print('Thanks')
    exit()


def user_options():
    clear_console()

    print('''  
██████╗░░██████╗████████╗░░░░░░████████╗██████╗░███████╗███████╗
██╔══██╗██╔════╝╚══██╔══╝░░░░░░╚══██╔══╝██╔══██╗██╔════╝██╔════╝
██████╦╝╚█████╗░░░░██║░░░█████╗░░░██║░░░██████╔╝█████╗░░█████╗░░
██╔══██╗░╚═══██╗░░░██║░░░╚════╝░░░██║░░░██╔══██╗██╔══╝░░██╔══╝░░
██████╦╝██████╔╝░░░██║░░░░░░░░░░░░██║░░░██║░░██║███████╗███████╗
╚═════╝░╚═════╝░░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝
                                        name: Dakshitha Perera
                                        ecu ID - 10519381
        ''')
    print('\33[94m' + '===' * 30 + '\33[0m')
    print(
        '1.) Per-load a sequence of integers to build a BST\n'
        '2.) Manually enter integer values/keys, one by one to build a BST\n3.) Exit')
    print('\33[94m' + '===' * 30 + '\33[0m')

    try:
        user_choice = int(input('\33[93m' + 'Enter your option here: ' + '\33[0m'))
    except ValueError:
        print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
        input('\tPress Enter to continue...')
        return user_options()
    if user_choice == 1:
        user_arr = [54, 80, 64, 19, 34, 78, 22, 13, 20, 102, 91, 44, 84, 50, 46, 47, 49, 45]
    elif user_choice == 2:
        user_arr = user_prompt()
    else:
        program_exit()
    # noinspection PyUnboundLocalVariable
    return user_arr


def input_int(verb):
    while True:
        try:
            the_int = int(input('\33[93m' + f'Enter {verb} Value: ' + '\33[0m'))
            return the_int
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')


def main_menu(obj_bst):
    clear_console()
    while True:
        print('\33[94m' + '===' * 30 + '\33[0m')
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
        print('\33[94m' + '===' * 30 + '\33[0m')

        try:
            menu_choice = int(input('Enter your option here: '))
            break
        except ValueError:
            print('\33[41m' + '\n\tERROR: Input is invalid!!!' + '\33[0m')
            input('\tPress Enter to continue...')
    # noinspection PyUnboundLocalVariable
    print('\33[92m' + '===' * 30 + '\33[0m')
    match menu_choice:
        case 1:
            per_order = obj_bst.per_order_traversal()
            in_order = obj_bst.in_order_traversal()
            post_order = obj_bst.post_order_traversal()
            print('per-order traversal : \n\t{}'.format(per_order))
            print('in-order traversal : \n\t{}'.format(in_order))
            print('post-order traversal : \n\t{}'.format(post_order))

        case 2:
            leafs, non_leafs = obj_bst.leaf_node_checker()
            print('Leaf Nodes are: \n\t{}'.format(leafs))
            print('Non-Leaf Nodes are: \n\t{}'.format(non_leafs))

        case 3:
            node_n = input_int('Search')
            stree = obj_bst.sub_tree_nodes(root_node=node_n)
            if stree:
                print('\t' + '\33[45m' + f'FOUND: Node {node_n} found!' + '\33[0m')
                print('Total number of trees of nodes of the subtree are: {}'.format(len(stree)))
                print('\33[92m' + '===' * 30 + '\33[0m')
                return
            print('\t' + '\33[91m\U0001F641' + f'SORRY: I Could not find {node_n} node' + '\33[0m')

        case 4:
            node_n = input_int('Search')
            node_depth = obj_bst.depth(node_n)
            if node_depth != 0:
                print('\t' + '\33[45m' + f'FOUND: Node {node_n} found!' + '\33[0m')
                print('depth of the {} in the BST: {}'.format(node_n, node_depth))
                print('\33[92m' + '===' * 30 + '\33[0m')
                return
            print('\t' + '\33[91m\U0001F641' + f'SORRY: I Could not find {node_n} node' + '\33[0m')

        case 5:
            node_n = input_int('Search')

            stree_depth = obj_bst.sub_tree_depth(given_node=node_n)
            if stree_depth:
                print('\t' + '\33[45m' + f'FOUND: Node {node_n} found!' + '\33[0m')
                print(f'depth of {node_n} in the BST is: {stree_depth}')
                print('\33[92m' + '===' * 30 + '\33[0m')
                return
            print('\t' + '\33[91m\U0001F641' + f'SORRY: I Could not find {node_n} node' + '\33[0m')

        case 6:
            insert_int = input_int('Insert')
            search_results = obj_bst.search_elements(insert_int)
            if search_results is None:
                obj_bst.insert_child(insert_int)
                print(f'\n\33[32m \U0001F44D Elz: Successfully inserted the {insert_int} in to the tree\33[0m\n')
                obj_bst.display_bst_tree(obj_bst, '', False)
            else:
                print(f'\t\33[91m\U0001F641 SORRY: I cannot insert it\n '
                      f'\tCuz, {insert_int} node is already in the BST\33[0m')

        case 7:
            del_node = input_int('Delete')
            search_result = obj_bst.search_elements(del_node)
            if search_result is not None:
                del_tree = obj_bst.delete_node(del_node)
                print(f'\n\33[32m \U0001F44D Elz: Successfully deleted the {del_node} from the Tree\33[0m\n')
                del_tree.display_bst_tree(del_tree, '', False)
            else:
                print(f'\t\33[91m\U0001F641 SORRY: I cannot delete it\n '
                      f'\tCuz, {del_node} node is not in the BST\33[0m')

        case 8:
            program_exit()
    print('\33[92m' + '===' * 30 + '\33[0m')


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
