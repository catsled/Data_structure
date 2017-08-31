


class SingleLinkList(object):

    class _Node(object):
        __slot__ = '_element', '_next'

        def __init__(self,element,next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None  # 定义链表的头节点
        self._size = 0

    def __len__(self):
        """获得链表的长度"""
        return self._size

    def is_empty(self):
        """判断链表是否为空"""
        return self._size == 0

    def add(self,element):
        """在链表的首部添加元素"""
        new_node = self._Node(element,None)
        new_node._next = self._head
        self._head = new_node
        self._size += 1

    def append(self,element):
        """在链表的尾部添加元素"""
        new_node = self._Node(element,None)
        if self.is_empty():
            self.add(element)
        else:
            curr = self._head._next
            prev = self._head
            while curr:
                prev = prev._next
                curr = curr._next
            prev._next = new_node
            self._size += 1

    def insert(self,pos,element):
        """在链表的指定位置添加元素"""
        if pos >= self._size:
            self.append(element)
        else:    
            if pos <= 0:
                self.add(element)
            else:
                new_node = self._Node(element,None)
                curr = self._head._next
                prev = self._head
                while pos > 1:
                    curr = curr._next
                    prev = prev._next
                    pos -= 1
                prev._next = new_node
                new_node._next = curr
                self._size += 1
            
    def del_element(self,element):
        """删除链表中的指定元素"""
        curr = self._head
        prev = None
        while curr:
            if element == curr._element:
                if curr == self._head:
                    self._head = curr._next
                else:
                    prev._next = curr._next
                    curr = None
                print('删除成功')
                self._size -= 1
                return True
            prev = curr
            curr = curr._next
        print('没有该元素')
        return False

    def search(self,element):
        """检查元素是否在链表中"""
        if self.is_empty():
            raise Empty('链表为空')
        else:
            curr = self._head
            while curr:
                if element == curr._element:
                    return True
                curr = curr._next
        return False

    def trivial(self):
        """遍历链表"""
        curr = self._head
        while curr:
            print(curr._element)
            curr = curr._next

if __name__ == '__main__':
    a = SingleLinkList()
    a.add(2)
    a.add(3)
    a.append(8)
    a.add(1)
    a.insert(0,9)
    a.insert(3,11)
    a.append(18)
    a.add(23)
    a.insert(0,63)
    print(a.search(11))
    a.trivial()
    a.del_element(18)
    a.del_element(3)
    a.del_element(63)
    a.trivial()

