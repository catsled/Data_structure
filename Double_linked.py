"""实现双向链表"""

class DoubleLink(object):
    # ------------Node--------------
    class _Node(object):
        __slots__ = '_element', '_prev', '_next'

        def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next

    # -----------method----------------

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def _insert_between(self,element,pre,suc):
        """插入一个新的节点"""
        new_node = self._Node(element,pre,suc)
        pre._next = new_node
        suc._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self,node):
        """删除一个节点"""
        if self.is_empty():
            raise Empty('无法删除空')
        else:
            pre = node._prev
            suc = node._next
            pre._next = suc
            suc._prev = pre
            self._size -= 1
            element = node._element
            node._element = node._prev = node._next = None
            return element
