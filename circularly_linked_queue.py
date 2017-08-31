
class CLinkedQueue(object):
    # --------------Node-------------------
    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self,element,next):
            self._element = element
            self._next = next
    # -------------method------------------

    def __init__(self):
        # self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        """判断队列是否为空"""
        return len(self) == 0
    
    def enqueue(self,element):
        """添加数据"""
        new_node = self._Node(element,None)

