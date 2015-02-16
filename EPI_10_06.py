# Sum the root to leaf paths

from util import *


def sum_path(root):

    def sum_generator(root, cur):
        if not root:
            return 0
        partial = cur * 2 + root.val
        if not root.left and not root.right:
            return partial

        return sum_generator(root.left, partial) + sum_generator(root.right, partial)
    return sum_generator(root, 0)


if __name__ == '__main__':
    print '=== Binary Tree ==='
    values = [0, 1, 0, 0, 1, 1, 0, 1]
    bt = createBinaryTree(values)
    print sum_path(bt)
    printBinarySearchTree(bt)



