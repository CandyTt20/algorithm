class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    # TODO: Write your code here
    if head is None:
        return
    head_reverse = reverse(findMid(head))
    cur, cur_reverse = head, head_reverse
    
    while (cur_reverse.next is not None):
        next, next_reverse = cur.next, cur_reverse.next
        cur.next = cur_reverse
        cur_reverse.next = next
        cur, cur_reverse = next, next_reverse
        

    return


def findMid(head):
    slow, fast = head, head
    while (fast is not None and fast.next is not None):
        slow = slow.next
        fast = fast.next.next
    return slow

def reverse(head):
    prev, cur = None, head
    while cur is not None:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    # head.next.next.next.next.next = Node(12)
    reorder(head)
    head.print_list()
    # reverse(head).print_list()
    # print(findMid(head).value)


main()