"""使用单链表实现队列"""

class LinkedQueue(object):
    # --------------Node-------------------
    class _Node(object):
        __slots__ = '_element', '_next'

        def __init__(self,element,next):
            self._element = element
            self._next = next
    # -------------method------------------

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        """判断队列是否为空"""
        return len(self) == 0

    def first(self):
        """检查队列的第一个元素"""
        if self.is_empty():
            raise Empty('队列为空')
        else:
            return self._head._element

    def enqueue(self,element):
        """向队列中添加元素"""
        new_node = self._Node(element,None)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        """remove the first element in the queue"""
        if self.is_empty():
            raise Empty('队列为空')
        else:
            result = self._head
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
        return result._element

