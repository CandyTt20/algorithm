class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mid = self.find_mid(head)
        if mid[1].next is None:
            head_reverse = self.reverse(mid[0])
            while head is not None:
                if head.val != head_reverse.val:
                    return False
                head_reverse = head_reverse.next
                head = head.next
        else:
            head_reverse = self.reverse(mid[0].next)
            mid[0].next = None
            while head is not None:
                if head.val != head_reverse.val:
                    return False
                head_reverse = head_reverse.next
                head = head.next

        return True

    def find_mid(self, head):
        slow, fast = head, head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow, fast

    def reverse(self, head):
        pre, cur = None, head
        while cur is not None:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
# s


head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(2)
# head.next.next.next = ListNode(1)
x = Solution()
# y=x.reverse(head)
# print(y.val)
# print(y.next.val)
print(x.isPalindrome(head))
