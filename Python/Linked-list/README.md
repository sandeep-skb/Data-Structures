Linked-List in PYTHON

A linked list is a datatype which contains data elements which may or may not reside in contigous memory addresses. It is for this reason linked list are very powerful than arrays which have an absolute requirement of contigous memory allocation. Linked lists are also of dynamic size.
Since the linked list elements are not in contigous memory addresses, it needs to store the address of the next data along with the current data value. This entity which stores data and the address of the next data element is called a  "Node".
In native python library there is no Node datatype and as this is the basic building block of the linked list we have to build this first.
[Node.py](https://github.com/sandeep-skb/Data-Structures/blob/master/Python/Linked-list/create_node.py)

Next using this Node we can create a singly linked list and traverse through the list.

[Singly LinkedList](https://github.com/sandeep-skb/Data-Structures/blob/master/Python/Linked-list/singly_linked_list.py)
