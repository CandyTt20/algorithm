


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next




def find_cycle_start(head):
    slow, fast, pointer_1, pointer_2, length = head, head, head, head, 1
    
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    cur = slow
    while cur.next != slow:
        cur = cur.next
        length += 1
    while length != 0:
        pointer_2 = pointer_2.next
        length -= 1
    while pointer_1 != pointer_2:
        pointer_1 = pointer_1.next
        pointer_2 = pointer_2.next
                
    return pointer_1    
    




def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))



main()



