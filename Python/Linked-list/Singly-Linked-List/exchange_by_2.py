
def traverse(node):
    if node != None:
        print(node.data)
        traverse(node.next)


def exchange(node):
    prev = Node(0)
    prev.next = node
    head = prev
    while((node != None) and (node.next != None)):
        prev.next = node.next
        temp = node.next.next
        node.next.next = node
        node.next = temp
        prev = node
        node = temp
    return head


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
    node = exchange(e1)
    print("After reversing the order of the linked list:")
    traverse(node.next)

if __name__ == "__main__":
    main()
