class Btree(object):
    def __init__(self, x, lchild=None, rchild=None):
        self.x = x
        self.lchild = lchild
        self.rchild = rchild

    def travel(self):
        root = self
        if root is None:
            return
        li = [root]
        while li:
            cur = li.pop(0) 
            print(cur.x, end=' ')
            if cur.lchild is not None:
                li.append(cur.lchild)
            if cur.rchild is not None:  
                li.append(cur.rchild)

    def preorder(self, root):
        # 递归
        if root is None:
            return
        print(root.x, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def preorder_nocr(self):
        # 非递归
        stack = []
        if self is None:
            return
        cur = self

        while True:
            while cur.lchild:
                if cur.rchild:
                    stack.append(cur)
                print(cur.x, end=' ')
                
                cur = cur.lchild
            print(cur.x, end=' ')
            
            if stack:
                cur = stack.pop().rchild
            else:
                break


x = Btree(5, Btree(3, Btree(1), Btree(0)), Btree(2, Btree(6)))
y = Btree(5, Btree(3, Btree(1, Btree(8), Btree(9)), Btree(
    0, Btree(10))), Btree(2, Btree(6), Btree(7)))

# x.travel()
y.preorder_nocr()
print('')
y.preorder(y)
