from typing import Dict, List
import unittest

from .Graph import Graph, GraphNode


class GraphE1(Graph):
    @staticmethod
    def is_reachable(start: GraphNode, goal: GraphNode) -> bool:
        """
        枝切り深さ優先探索を行う
        一度探索を行ったノードは、次からは探索を行わないので、O(num_nodes)
        """

        searched_nodes: Dict[int, bool] = {}
        search_stack: List[GraphNode] = []

        searching = start
        while True:
            if searching is goal:
                return True
            searched_nodes[id(searching)] = True

            for adjacence in searching.adjacences:
                if id(adjacence) not in searched_nodes:
                    search_stack.append(adjacence)

            if not search_stack:
                return False

            searching = search_stack.pop()


class TestE1(unittest.TestCase):
    def test_is_reachable1(self):
        node = GraphNode()

        assert GraphE1().is_reachable(node, node) is True

    def test_is_reachable2(self):
        node1 = GraphNode()
        node2 = GraphNode().connect(node1)

        assert GraphE1().is_reachable(node2, node1) is True
        assert GraphE1().is_reachable(node1, node2) is False

    def test_is_reachable3(self):
        node1 = GraphNode()
        node2 = GraphNode().connect(node1)
        node3 = GraphNode().connect(node2)

        assert GraphE1().is_reachable(node1, node2) is False
        assert GraphE1().is_reachable(node1, node3) is False
        assert GraphE1().is_reachable(node2, node1) is True
        assert GraphE1().is_reachable(node2, node3) is False
        assert GraphE1().is_reachable(node3, node1) is True
        assert GraphE1().is_reachable(node3, node2) is True

    def test_is_reachable4(self):
        node1 = GraphNode()
        node2 = GraphNode().connect(node1)
        node1.connect(node2)

        node3 = GraphNode()
        node4 = GraphNode().connect(node3)
        node3.connect(node4)

        assert GraphE1().is_reachable(node1, node2) is True
        assert GraphE1().is_reachable(node1, node3) is False
        assert GraphE1().is_reachable(node1, node4) is False
        assert GraphE1().is_reachable(node2, node1) is True
        assert GraphE1().is_reachable(node2, node3) is False
        assert GraphE1().is_reachable(node2, node4) is False
        assert GraphE1().is_reachable(node3, node1) is False
        assert GraphE1().is_reachable(node3, node2) is False
        assert GraphE1().is_reachable(node3, node4) is True
        assert GraphE1().is_reachable(node4, node1) is False
        assert GraphE1().is_reachable(node4, node2) is False
        assert GraphE1().is_reachable(node4, node3) is True


if __name__ == "__main__":
    if __name__ == "__main__":
        unittest.main()
