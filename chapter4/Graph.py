from typing import NoReturn, Any, List, Iterable, Optional


class Node:
    data: Any = None

    def __init__(self, data: Any = None):
        self.data = data


class GraphNode(Node):
    adjacences: List["GraphNode"]

    def __init__(self, data: Any = None, adjacences: Iterable = ()) -> NoReturn:
        super().__init__(data)

        self.adjacences = []
        for adjacence in adjacences:
            self.adjacences.append(adjacence)

    def connect(self, node: "GraphNode") -> "GraphNode":
        self.adjacences.append(node)

        return self


class BinaryNode(Node):
    parent: "BinaryNode" = None
    left_child: "BinaryNode" = None
    right_child: "BinaryNode" = None

    def add_left(self, node: "BinaryNode") -> "BinaryNode":
        self.left_child = node
        node.parent = self
        return self

    def add_right(self, node: "BinaryNode") -> "BinaryNode":
        self.right_child = node
        node.parent = self
        return self

    @property
    def is_left_child(self) -> bool:
        return self.parent.left_child is self

    @property
    def is_right_child(self) -> bool:
        return self.parent.right_child is self

    @property
    def has_left_child(self) -> bool:
        return self.left_child is not None

    @property
    def has_right_child(self) -> bool:
        return self.right_child is not None

    @property
    def has_parent(self) -> bool:
        return self.parent is not None


class Graph:
    nodes: List[Node]

    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node) -> "Graph":
        self.nodes.append(node)
        return self

    def add_nodes(self, nodes: Iterable) -> "Graph":
        for node in nodes:
            self.nodes.append(node)
        return self


class BinaryTree:
    root: Optional[BinaryNode]

    def __init__(self, node: BinaryNode = None):
        self.root = node
