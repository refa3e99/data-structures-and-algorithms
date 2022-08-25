from ..Linked_List.linked_list import *
ll = LinkedList()
ll2 = LinkedList()

ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

ll2.insert(7)
ll2.insert(8)
ll2.insert(9)


# ll2.insert(70)
# ll.insert(8)
# ll.insert_after(8, 3)
# ll.insert_before(9, 0)
# ll.insert_before(0, 7)
# ll.insert_after(1, 0)
# print(ll.to_string())
# print(ll2.to_string())
# print(ll.includes(6))
# print(ll.includes(7))

def zipLists(list1, list2):
    a = list1.head
    b = list2.head

    while a != None and b != None:

        c = a.nextNode
        d = b.nextNode


        b.nextNode = c
        a.nextNode = b

        a = c
        b = d
        list2.head = b

    print(list1.to_string())

zipLists(ll, ll2)