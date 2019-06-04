# Reversing a linked list.
def traverse(node):
    if node != None:
        print(node.data)
        traverse(node.next)


def reverse(node):
    prev = None
    while(node != None):
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    return prev


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    e1 = Node(1)
    e2 = Node(2)
    e1.next = e2
    e3 = Node(3)
    e2.next = e3
    e4 = Node(4)
    e3.next = e4
    e5 = Node(5)
    e4.next = e5

    print("Original order of the linked list:")
    traverse(e1)
    print()
    node = reverse(e1)
    print("After reversing the order of the linked list:")
    traverse(node)

if __name__ == "__main__":
    main()
