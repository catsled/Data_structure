
import random

class OrderedBTree(object):
    """实现排序树"""
    class _Node(object):

        def __init__(self,element,parent,lchild,rchild):
            self.element = element
            self.parent = parent
            self.lchild = lchild
            self.rchild = rchild

    def __init__(self):
        self.root = None
        self.nodes = 0

    def __len__(self):
        """返回树的节点个数"""
        return self.nodes

    def build_root(self,element):
        """创建根节点"""
        if len(self) > 0:
            raise ValueError('根节点已经存在')
        new_node = self._Node(element,None,None,None)
        self.root = new_node
        self.nodes = 1

    def add_node(self,element,root):
        """添加节点"""
        if root == None:
            return
        if element < root.element:
            if root.lchild == None:
                new_node = self._Node(element,None,None,None)
                root.lchild = new_node
                new_node.parent = root
                self.nodes += 1
            else:
                self.add_node(element,root.lchild)
        elif element >= root.element:
            if root.rchild == None:
                new_node = self._Node(element,None,None,None)
                root.rchild = new_node
                new_node.parent = root
                self.nodes += 1
            else:
                self.add_node(element,root.rchild)

    def parent(self,node=None):
        """检查某一节点的父节点"""
        if node == None:
            return None
        return node.parent

    def children(self,node=None):
        """检查某一节点的子节点"""
        if node.lchild is not None:
            yield node.lchild
        if node.rchild is not None:
            yield node.rchild

    def sibling(self,node):
        """检查一个节点的兄弟节点"""
        if node == None:
            return None
        parent = self.parent(node)
        if node == parent.lchild:
            return parent.rchild
        elif node == parent.rchild:
            return parent.lchild

    def is_leaf(self,node):
        """检查某一节点是否是叶子节点"""
        return node.lchild == node.rchild == None

    def height(self,root=None):
        """计算树的高度(根节点为第0层)"""
        if self.is_leaf(root):  # 如果某个节点是叶子节点那么他没有其他子节点
            return 0
        else:
            return 1 + max(self.height(c) for c in self.children(root))

    def get_nodes(self):
        """获取树的节点数"""
        return self.nodes

    # --------------------------遍历方法----------------------------

    def preorder(self,root=None):
        """先序"""
        if root == None:
            return
        print(root.element,end=' ')
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self,root=None):
        """中序"""
        if root == None:
            return
        self.inorder(root.lchild)
        print(root.element,end=' ')
        self.inorder(root.rchild)

    def postorder(self,root=None):
        """后序"""
        if root == None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.element,end=' ')

    def wildly_through(self):
        """广度优先遍历"""
        w_list = list()
        w_list.append(self.root)
        while w_list:
            root = w_list.pop(0)
            print(root.element,end=' ')
            if root.lchild:
                w_list.append(root.lchild)
            if root.rchild:
                w_list.append(root.rchild)


if __name__ == '__main__':
    a = OrderedBTree()
    a.build_root(7)
    for _ in range(10):  # 向树中添加10个节点
        a.add_node(random.randint(1,20),a.root)
    print('先序遍历: ', end=' ')
    a.preorder(a.root)
    print()
    print('中序遍历: ', end=' ')
    a.inorder(a.root)
    print()
    print('后序遍历: ', end=' ')
    a.postorder(a.root)
    print()
    print('层次遍历: ', end=' ')
    a.wildly_through()
    print()
    print('树的高度: %d' % a.height(a.root))
    print('节点数: %d' % a.get_nodes())


