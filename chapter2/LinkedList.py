import unittest
from abc import ABCMeta, abstractmethod


class Node:
    """
    無連結ノード

    -- initialize
    node = Node(value)
    -- public method
    node.value()
    node.set_value()
    """

    __value = None

    def __init__(self, value, *args, **kwargs):
        self.set_value(value)

    def value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
        return self


class SinglyLinkedNode(Node):
    """
    一方向連結ノード

    -- initialize
    node = SinglyLinkedNode(value[, next_node])
    -- public method
    node.has_next()
    node.next()
    node.set_next()
    node.delete_next()
    """

    __next = None

    def __init__(self, value, next=None, *args, **kwargs):
        super().__init__(value, *args, **kwargs)
        if next is not None:
            self.set_next(next)

    def next(self):
        if self.__next is None:
            raise LookupError("next() is invalid. next node is not found.")
        return self.__next

    def set_next(self, node):
        if not isinstance(node, SinglyLinkedNode):
            raise TypeError(
                f"Argument type of set_next() is invalid. Expected 'SinglyLinkedNode', but '{node.__class__.__name__}'"
            )
        self.__next = node
        return self

    def delete_next(self):
        self.__next = None
        return self

    def has_next(self):
        return self.__next is not None


class DoublyLinkedNode(SinglyLinkedNode):
    __prev = None

    def __init__(self, value, next=None, prev=None, *args, **kwargs):
        super().__init__(value, next, *args, **kwargs)
        if prev is not None:
            self.__prev = self.set_prev(prev)

    def prev(self):
        if self.__prev is None:
            raise LookupError("prev() is invalid. previous node is not found.")
        return self.__prev

    def set_prev(self, node):
        if not isinstance(node, DoublyLinkedNode):
            raise TypeError(
                f"Argument type of set_prev() is invalid. Expected 'DoublyLinkedNode', but '{node.__class__.__name__}'"
            )
        self.__prev = node
        return self

    def delete_prev(self):
        self.__prev = None
        return self

    def has_prev(self):
        return self.__prev is not None


class LinkedList(metaclass=ABCMeta):
    """
    連結リストの抽象クラス

    -- public method
    get_head()
    has_head()
    set_head()
    get_tail()
    has_tail()
    set_tail()

    append()
    delete()

    -- abstract method
    append()
    delete()
    """

    __head = None
    __tail = None
    node_class = None

    def __init__(self, iterable=()):
        for value in iterable:
            self.append(value)

    def __iter__(self):
        if not self.has_head():
            return

        _i = self.get_head()
        while _i.has_next():
            yield _i.value()
            _i = _i.next()
        yield _i.value()

    def __len__(self):
        if not self.has_head():
            return 0

        length = 1
        node = self.get_head()
        while node.has_next():
            length += 1
            node = node.next()
        return length

    def __eq__(self, other):
        if not isinstance(other, LinkedList):
            raise NotImplementedError(
                "LinkedList can be compared only with LinkedList."
            )
        if not self.has_head() and not other.has_head():
            return True
        if not (self.has_head() and other.has_head()):
            return False

        self_node = self.get_head()
        other_node = other.get_head()
        while self_node.has_next() or other_node.has_next():
            if not (self_node.has_next() and other_node.has_next()):
                return False
            if self_node.value() != other_node.value():
                return False
            self_node = self_node.next()
            other_node = other_node.next()
        if self_node.value() != other_node.value():
            return False
        return True

    def __str__(self):
        return "SinglyLinkedList[" + ", ".join([str(x) for x in self]) + "]"

    def __getitem__(self, key):
        return self._get_node(key).value()

    def _check_negative_index(self, key):
        if key < 0:
            raise IndexError("negative index is invalid")
        return self

    def _get_node(self, key):
        self._check_negative_index(key)
        node = self.get_head()
        for i in range(key):
            node = node.next()
        return node

    def _create_node(self, *args, **kwargs):
        if not self.node_class:
            raise TypeError("_create_node() is invalid. node_class isn't set.")
        return self.node_class(*args, **kwargs)

    def has_head(self):
        return self.__head is not None

    def has_tail(self):
        return self.__tail is not None

    def get_head(self):
        if not self.has_head():
            raise LookupError("_get_head() is invalid. head node is not found.")
        return self.__head

    def get_tail(self):
        if not self.has_tail():
            raise LookupError("_get_tail() is invalid. tail node is not found.")
        return self.__tail

    def set_head(self, node):
        if not isinstance(node, SinglyLinkedNode):
            raise TypeError(
                f"_set_head() is invalid. node type is expected 'SinglyLinkedNode', but {node.__class__.__name__}"
            )
        self.__head = node
        return self

    def set_tail(self, node):
        if not isinstance(node, SinglyLinkedNode):
            raise TypeError(
                f"_set_tail() is invalid. node type is expected 'SinglyLinkedNode', but {node.__class__.__name__}"
            )
        self.__tail = node
        return self

    def _delete_head_and_tail(self):
        self.__head = None
        self.__tail = None
        return self

    @abstractmethod
    def append(self, value):
        pass

    @abstractmethod
    def append_head(self, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass


class SinglyLinkedList(LinkedList):
    """
    一方向連結リスト
    """

    node_class = SinglyLinkedNode

    def append(self, value):
        node = self._create_node(value)

        if not self.has_head():
            return self.set_head(node).set_tail(node)

        self.get_tail().set_next(node)
        return self.set_tail(node)

    def append_head(self, value):
        node = self._create_node(value)

        if not self.has_head():
            return self.set_head(node).set_tail(node)

        return self.set_head(node.set_next(self.get_head()))

    def delete(self, key):
        if key == 0:
            return self._delete_head()
        return self._delete_next_node(self._get_node(key - 1))

    def _delete_next_node(self, node):
        if not node.next().has_next():
            return self.set_tail(node.delete_next())

        node.set_next(node.next().next())
        return self

    def _delete_head(self):
        head = self.get_head()
        if not head.has_next():
            return self._delete_head_and_tail()
        return self.set_head(head.next())


class DoublyLinkedList(LinkedList):
    """
    両方向連結リスト
    """

    node_class = DoublyLinkedNode

    def append(self, value):
        node = self._create_node(value)

        if not self.has_head():
            return self.set_head(node).set_tail(node)

        return self.set_tail(node.set_prev(self.get_tail().set_next(node)))

    def append_head(self, value):
        node = self._create_node(value)

        if not self.has_head():
            return self.set_head(node).set_tail(node)

        return self.set_head(node.set_next(self.get_head().set_prev(node)))

    def delete(self, key):
        target = self._get_node(key)
        head = self.get_head()
        tail = self.get_tail()

        if target is head and target is tail:
            return self._delete_head_and_tail()
        if target is head:
            return self._delete_head()
        if target is tail:
            return self._delete_tail()
        return self._delete_middle(target)

    def _delete_head(self):
        return self.set_head(self.get_head().next().delete_prev())

    def _delete_tail(self):
        return self.set_tail(self.get_tail().prev().delete_next())

    def _delete_middle(self, node):
        node.prev().set_next(node.next().set_prev(node.prev()))
        return self


class TestSinglyLinkedList(unittest.TestCase):
    list_class = SinglyLinkedList

    def testDeleteHead(self):
        assert self.list_class([0, 1, 2]).delete(0) == self.list_class([1, 2])

    def testDeleteTail(self):
        assert self.list_class([0, 1, 2]).delete(2) == self.list_class([0, 1])

    def testDeleteMiddle(self):
        assert self.list_class([0, 1, 2]).delete(1) == self.list_class([0, 2])

    def testAppendToEmpty(self):
        assert self.list_class().append(0) == self.list_class([0])

    def testAppend(self):
        assert self.list_class([0]).append(1) == self.list_class([0, 1])

    def testAppendHeadToEmpty(self):
        assert self.list_class().append_head(0) == self.list_class([0])

    def testAppendHead(self):
        assert self.list_class([0]).append_head(1) == self.list_class([1, 0])


class TestDoublyLinkedList(TestSinglyLinkedList):
    list_class = DoublyLinkedList


if __name__ == "__main__":
    unittest.main()
