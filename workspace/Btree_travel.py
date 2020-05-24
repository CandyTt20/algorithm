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

        if root is None:
            return
        print(root.x, end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)


x = Btree(5, Btree(3, Btree(1), Btree(0)), Btree(2, Btree(6)))
# x.travel()
x.preorder(x)
