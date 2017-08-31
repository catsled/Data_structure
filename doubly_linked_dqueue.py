from Double_linked import DoubleLink

class Dqueue(DoubleLink):

    def first(self):
        """查看队列中的第一个元素"""
        if self.is_empty():
            raise Empty('队列为空')
        head = self._header._next
        return head._element

    def first_enqueue(self,element):
        """向队首添加元素"""
        self._insert_between(element,self._header,self._header._next)

    def enqueue(self,element):
        """向队尾添加元素"""
        self._insert_between(element,self._trailer._prev,self._trailer)

    def dequeue(self):
        """删除队首元素"""
        if self.is_empty():
            raise Empty('队列为空')
        else:
            self._delete_node(self._header._next)

    def delete_last(self):
        """删除队尾元素"""
        if self.is_empty():
            raise Empty('队列为空')
        else:
            self._delete_node(self._trailer._prev)


        

