'''
Time and Memory complexity analysis

-->Time complexity<--

* For constructing the binary tree total cost is numbers of nodes "n"
so overall time complexity O(n)

* For getting the paths to root node of two given nodes is equal to the numbers of 
nodes to the root, In worst case it will be height of the tree O(h)+O(h)

* and selecting least common node between two Stacks cost would be in worst case O(h), where
h height of the tree

-> Overall time complexity in worst case is O(n)

-->Space/Memory<--

* For constructing the binary tree total Space complexity in worst case in O(n)
where n is number of nodes of the tree
* and Space complexity of storing values to Stack is propotional to height of the tree 
in worst case so we can consider O(h)

-> Overall Space complexity of this problem is O(n) in worst case


'''


from collections import deque


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


# This function returns all of the nodes from target node to the root node

def pathToRoot(Node):

    paths = deque()

    currentNode = Node

    while currentNode.parent:
        paths.append(currentNode.value)
        currentNode = currentNode.parent
    paths.append(currentNode.value)

    return paths


def lca(node1, node2):

    # Getting paths of two given nodes

    paths_of_node1 = pathToRoot(node1)
    paths_of_node2 = pathToRoot(node2)

    # Finding out the least common value between two paths

    lca_of_two = None
    while paths_of_node1 and paths_of_node2:
        pop1 = paths_of_node1.pop()
        pop2 = paths_of_node2.pop()

        if pop1 == pop2:
            lca_of_two = pop1
        else:
            break
    return lca_of_two


# inserting nodes

n1 = Node(1, None)
n2 = Node(2, n1)
n3 = Node(3, n1)
n4 = Node(4, n2)
n5 = Node(5, n2)
n6 = Node(6, n3)
n7 = Node(7, n3)
n8 = Node(8, n4)
n9 = Node(9, n4)

# result = lca(n3, n7)
# print(result)
