class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
def insert_node(head, node):
    if node.value > head.value:
        if head.right is None:
            head.right = node
        else:
            insert_node(head.right, node)
    elif node.value < head.value:
        if head.left is None:
            head.left = node
        else:
            insert_node(head.left, node)

def lowest_common(head, m, n):
    if head is None:
        return None
    if head.value > m and head.value > n:
        return lowest_common(head.left, m, n)
    if head.value < m and head.value < n:
        return lowest_common(head.right, m, n)
    return head.value

n_nodes = int(input())
nodes = list(map(int, input().split()))
arr = input().split()
m1 = int(arr[0])
n1 = int(arr[1])
if m1 not in nodes or n1 not in nodes:
    print(-1)
else:
    head= Node(nodes[0])
    for index in range(1, n_nodes):
        node = Node(nodes[index])
        insert_node(head, node)
    value = lowest_common(head, m1, n1)
    print(value)
