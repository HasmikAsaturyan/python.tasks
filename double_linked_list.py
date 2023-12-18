class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
        self.__prev = None

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, new_data):
        self.__data = new_data

    @property
    def next(self):
        return self.__next
    @next.setter
    def next(self,new_next):
        self.__next = new_next

    @property
    def prev(self):
        return self.__prev
    @prev.setter
    def prev(self, new_prev):
        self.__prev = new_prev

class Double_linkedlist:
    def __init__(self):
        self.__head = None

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, new_head):
        self.__head = new_head

    def is_empty(self):
        return self.__head is None

    def append(self, data):
        if self.__head is None:
            new_node = Node(data)
            new_node.prev = None
            self.__head = new_node
        else:
            new_node = Node(data)
            cur = self.__head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur
            new_node.next = None

    def prepend(self,data):
        if self.__head is None:
            new_node = Node(data)
            new_node.prev = None
            new_node = self.__head
        else:
            new_node = Node(data)
            self.__head.prev = new_node
            new_node.next = self.__head
            self.__head = new_node
            new_node.prev = None

    def insert_after(self,target_data, data):
        cur = self.__head
        while cur:
            if cur.next is None and cur.data == target_data:
                self.append(data)
                return
            elif cur.data == target_data:
                new_node = Node(data)
                nxt = cur.next
                cur.next = new_node
                new_node.next = nxt
                new_node.prev = cur
                nxt.prev = new_node
            cur = cur.next

    def insert_before(self,target_data, data):
        cur = self.__head
        while cur:
            if cur.prev is None and cur.data == target_data:
                self.prepend(data)
                return
            elif cur.data == target_data:
                new_node = Node(data)
                prev = cur.prev
                prev.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = prev
            cur = cur.next

    def delete(self,key):
        cur = self.__head
        while cur:
            if cur.data == key and cur == self.__head:
                if not cur.next:
                    cur = None
                    self.__head = None
                    return
                else:
                    nxt = cur.next
                    cur.next = None
                    nxt.prev = None
                    cur = None
                    self.__head = nxt
                    return

            elif cur.data == key:
                if cur.next:
                    nxt = cur.next
                    prev = cur.prev
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return

                else:
                    prev = cur.prev
                    prev.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def display(self):
        cur = self.__head
        while cur:
            print(cur.data)
            cur = cur.next

llist = Double_linkedlist()
llist.append(1)
# llist.prepend(3)
llist.insert_after(1, 2)
llist.insert_before(2,4)
llist.delete(1)
llist.display()