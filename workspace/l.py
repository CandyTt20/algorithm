class node(object):
    def __init__(self, val, next=None):

        self.val = val
        self.next = next


x = node(5)
print(x.val)
x = node(6)
print(x.val)
for i in range(0, 10):
    print(i)
