# Lowest Common Ancestor - Part 1
# Without parent pointer

# Lowest Common Ancestor - Part 2
# With parent pointer

from util import *


# lca without parent pointer

def lca1(root, a, b):
    if not root:
        return None
    if root in (a, b):
        return root
    left = lca1(root.left, a, b)
    right = lca1(root.right, a, b)
    if left and right:
        return root
    if left or right:
        return left if left else right
    return None

# lca with parent pointer

# 1 - Hash Table O(h) space complexity

# def lca_p2(root, a, b):

# 2 - OR Calculate depth and tandem


if __name__ == '__main__':
    print '=== Binary Tree ==='
    values = [0, 1, 2, 3, -1, 4, -1]
    bt = createBinaryTree(values)
    one, two = bt.right.left, bt.right
    print one.val, two.val
    print "LCA: ", lca1(bt, one, two).val
    # print "looking for: ", find_node_bt(bt, bt.left)
    # print "looking for: ", find_node_bt(bt, TreeNode(1))

    printBinarySearchTree(bt)

    print '\n'
    print '=== Binary Search Tree ==='

    values = [4, 5, 5, 7, 2, 1, 3]
    bst = createBinarySearchTree(values)
    print bst.left.left.val, bst.left.right.val
    print "LCA: ", lca1(bst, bst.left.left, bst.left.right).val
    print bst.left.val, bst.right.val
    print "LCA: ", lca1(bst, bst.right, bst.left).val

    printBinarySearchTree(bst)

    # print '\n'
    # print '=== Binary Search Tree (Not Balanced) ==='

    # values = [3, 5, 5, 7, 4, 1, 2]
    # bst = createBinarySearchTreeNotBalanced(values)
    # printBinarySearchTree(bst)

    # print '\n'
    # print '=== Complete Binary Search Tree ==='

    # values = [1, 2, 3, 4, 5, 6, 7, 8]
    # bst = createCompleteBinarySearchTree(values)
    # printBinarySearchTree(bst)





