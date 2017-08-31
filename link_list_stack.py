
"""使用单链表实现栈"""

class LinkStack(object):
    # ---------------Node-------------------
    class _Node(object):
        __slots__ = '_element','_next'

        def __init__(self,element,next):
            self._element = element
            self._next = next
    # --------------method------------------

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """判断栈是否为空"""
        return self._size == 0

    def push(self,element):
        """向栈中添加元素"""
        self._head = self._Node(element,self._head)
        self._size += 1

    def pop(self):
        """弹出栈顶元素"""
        if self.is_empty():
            raise IndexError('栈空')
        else:
            result = self._head
            self._head = self._head._next
            self._size -= 1
            return result._element

    def top(self):
        """检查栈顶元素"""
        if self.is_empty():
            raise IndexError('栈空')
        else:
            return self._head._element


