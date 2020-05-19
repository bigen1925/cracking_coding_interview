from copy import copy
from enum import IntEnum
from random import shuffle, randint
from typing import List, Optional, Tuple, Dict

import numpy as np


class EdgePosition(IntEnum):
    """
    パズルピースの辺の場所を表表現するクラス
    """
    TOP = 0
    RIGHT = 1
    BOTTOM = 2
    LEFT = 3

    def next(self, n: int = 1) -> "EdgePosition":
        """
        n直角次の面を返す
        ex) next_position = EdgePosition.TOP.next() #  EdgePosition.RIGHT
        ex) next_position = EdgePosition.TOP.next(2) #  EdgePosition.BOTTOM
        """
        return self.__class__((self + n) % 4)

    def opposite(self) -> "EdgePosition":
        """
        反対側の面を返す
        ex) opposite_position = EdgePosition.TOP.opposite #  EdgePosition.BOTTOM
        ex) opposite_position = EdgePosition.LEFT.opposite #  EdgePosition.RIGHT
        """
        return self.__class__((self + 2) % 4)

    def diff(self, other: "EdgePosition") -> int:
        """
        otherとの差分を返す
        """
        return (other - self) % 4


class PieceEdge(int):
    """
    パズルピースの辺（の形状）を表現するドメインモデルクラス
    辺の形状をintで表現し、足して0になる辺とマッチすると判断する
    例） 形状が5の辺と、形状が-5の辺はマッチすると判断する
    """
    FLAT_VALUE = 0  # 平坦な形状（パズル全体の端っこの辺

    def __new__(cls, value: int = None):
        if value is None:
            value = cls.FLAT_VALUE

        return super().__new__(cls, value)

    def match(self, other_edge: "PieceEdge") -> bool:
        if not isinstance(other_edge, PieceEdge):
            raise ValueError(f"match() of PieceEdge expected an argument of PieceEdge, but of {other_edge.__class__}")
        return self + other_edge == 0

    @property
    def is_flat(self) -> bool:
        return self == self.FLAT_VALUE

    def get_correspondent(self):
        return self.__class__(-self)


class Piece:
    """
    パズルピースを表現するクラス

    4方向に辺を持ち、回転することができる
    """
    edges: Dict[EdgePosition, PieceEdge]

    def __init__(self):
        self.edges = {
            EdgePosition.TOP: PieceEdge(),
            EdgePosition.RIGHT: PieceEdge(),
            EdgePosition.BOTTOM: PieceEdge(),
            EdgePosition.LEFT: PieceEdge(),
        }

    @property
    def top(self) -> PieceEdge:
        """
        piece.topで辺にアクセスできる
        以下同様
        """
        return self.edges[EdgePosition.TOP]

    @property
    def right(self) -> PieceEdge:
        return self.edges[EdgePosition.RIGHT]

    @property
    def bottom(self) -> PieceEdge:
        return self.edges[EdgePosition.BOTTOM]

    @property
    def left(self) -> PieceEdge:
        return self.edges[EdgePosition.LEFT]

    def rotate(self, n: int = 1) -> "Piece":
        """
        n直角回転する
        """
        n = n % 4
        old_edges = copy(self.edges)

        for old_position, old_edge in old_edges.items():
            new_position = old_position.next(n)
            self.edges[new_position] = old_edge

        return self

    def rotate_random(self) -> "Piece":
        """
        ランダムに回る
        """
        n = randint(0, 3)
        return self.rotate(n)

    def rotate_with_position(self, from_position: EdgePosition, to_position: EdgePosition) -> "Piece":
        """
        今from_positionにある辺が、to_positionにくるように回す
        ex) piece.rotate_with_position(EdgePosition.TOP, EdgePosition.RIGHT)
         -> 今TOPにある辺がRIGHTにくるように回す
        """
        return self.rotate(from_position.diff(to_position))

    def position(self, target_edge: PieceEdge) -> EdgePosition:
        """
        辺（の形状）を指定して、その辺がピースのどのPositionにあるかを返す
        """
        for position, edge in self.edges.items():
            if edge == target_edge:
                return position

        raise ValueError(f"an edge passed is not found. edge: {target_edge}")

    def let_edge_to_position(self, edge: PieceEdge, position: EdgePosition) -> "Piece":
        """
        辺（の形状）を指定して、その辺がピースのpositionに来るように回す
        ex) piece.let_edge_to_position(PieceEdge(3), EdgePosition.RIGHT)
        """
        current_position = self.position(edge)
        self.rotate_with_position(from_position=current_position, to_position=position)

        return self


class Frame:
    """
    パズルのフレームを表現するクラス
    ピースをはめると、上下左右の隣をチェックして、辺の形状がマッチするかをバリデーションしてくれる
    """
    columns: int
    rows: int
    pieces: List[List[Optional[Piece]]]

    def __init__(self, columns: int, rows):
        self.columns = columns
        self.rows = rows
        self.pieces = [[None for _ in range(rows)] for _ in range(columns)]

    def set_pieces(self, pieces: List[List[Piece]]):
        """
        ピース全部をいっきにはめる
        """
        columns = len(pieces)
        rows = len(pieces[0])
        if rows != self.rows or columns != self.columns:
            raise ValueError(f"a size is not matched to set pieces to frame. size: {columns} * {rows}")

        for x in range(columns):
            for y in range(rows):
                self.set_piece(x, y, pieces[x][y])

    def set_piece(self, x: int, y: int, piece: Piece) -> "Frame":
        """
        ピース1枚をはめる
        上下左右をチェックして辺の形状があっているか確かめてくれる
        """
        if self.pieces[x][y] is not None:
            raise ValueError(
                f"target position({x}, {y}) is not empty."
            )

        # 左隣のバリデーション
        if x == 0:
            if not piece.left.is_flat:
                raise ValueError(
                    f"left edge of piece is not flat. x: {x}, y: {y}, piece: {piece}"
                )
        else:
            left_neighbor = self.pieces[x - 1][y]
            if left_neighbor is not None and not piece.left.match(left_neighbor.right):
                raise ValueError(
                    f"left edge is not matched. x: {x}, y: {y}, piece: {piece}, left_neighbor: {left_neighbor}"
                )

        # 右隣のバリデーション
        if x == self.columns - 1:
            if not piece.right.is_flat:
                raise ValueError(
                    f"right edge of piece is not flat. x: {x}, y: {y}, piece: {piece}"
                )
        else:
            right_neighbor = self.pieces[x + 1][y]
            if right_neighbor is not None and not piece.right.match(right_neighbor.left):
                raise ValueError(
                    f"right edge is not matched. x: {x}, y: {y}, piece: {piece}, right_neighbor: {right_neighbor}"
                )

        # 上隣のバリデーション
        if y == 0:
            if not piece.top.is_flat:
                raise ValueError(
                    f"top edge of piece is not flat. x: {x}, y: {y}, piece: {piece}"
                )
        else:
            above_neighbor = self.pieces[x][y - 1]
            if above_neighbor is not None and not piece.top.match(above_neighbor.bottom):
                raise ValueError(
                    f"top edge is not matched. x: {x}, y: {y}, piece: {piece}, above_neighbor: {above_neighbor}"
                )

        # 下隣のバリデーション
        if y == self.rows - 1:
            if not piece.bottom.is_flat:
                raise ValueError(
                    f"bottom edge of piece is not flat. x: {x}, y: {y}, piece: {piece}"
                )
        else:
            below_neighbor = self.pieces[x][y + 1]
            if below_neighbor is not None and not piece.bottom.match(below_neighbor.top):
                raise ValueError(
                    f"bottom edge is not matched. x: {x}, y: {y}, piece: {piece}, below_neighbor: {below_neighbor}"
                )

        self.pieces[x][y] = piece

        return self

    @property
    def is_completed(self) -> bool:
        """
        全て埋まっていたらTrue
        """
        for columns in self.pieces:
            if not all(columns):
                return False

        return True


class PuzzleFactory:
    """
    パズルを作るクラス

    フレームと、フレームにはめることが可能なピースのリストを返す
    """
    rows: int
    columns: int
    sequence: int

    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.sequence = 1

    # noinspection PyShadowingNames
    def factory(self) -> Tuple[Frame, List[Piece]]:
        frame = Frame(rows=self.rows, columns=self.columns)
        pieces = [[Piece() for _ in range(self.rows)] for _ in range(self.columns)]

        for x in range(self.columns):
            for y in range(self.rows):
                if 0 < x:
                    self.make_jig(pieces[x][y], EdgePosition.LEFT, pieces[x - 1][y])

                if 0 < y:
                    self.make_jig(pieces[x][y], EdgePosition.TOP, pieces[x][y - 1])

        pieces_box = list(np.array(pieces).flatten())
        shuffle(pieces_box)
        for piece in pieces_box:
            piece.rotate_random()

        return frame, pieces_box

    def make_jig(self, piece: Piece, position: EdgePosition, neighbor: Piece) -> None:
        """
        指定したピースの、指定した辺に形状を作る
        形状はシーケンスで指定し、パズル内で同じ形状が作られないようにする
        """
        edge = PieceEdge(self.sequence)
        self.sequence += 1

        piece.edges[position] = edge
        neighbor.edges[position.opposite()] = edge.get_correspondent()


class PuzzleSolver:
    """
    パズルを解くクラス
    """
    frame: Frame
    pieces_box: List[Piece]
    indices: Dict[PieceEdge, Piece]
    corner_pieces: List[Piece]

    # noinspection PyShadowingNames
    def __init__(self, frame: Frame, pieces_box: List[Piece]):
        self.frame = copy(frame)
        self.pieces_box = copy(pieces_box)

    def solve(self) -> Frame:
        # 辺の形ですぐピースを見つけられるように、インデックスを作っておく
        self.make_indices(self.pieces_box)

        pieces = []
        current = None
        column: List[Piece]

        while True:
            if current is None:
                # 角のピースを1つ取り、左上に合うように回転させる
                current = self.corner_pieces[0]
                self.rotate_corner_piece_as_left_top(current)
            else:
                # 前の列の先頭の右隣を取得
                # noinspection PyUnboundLocalVariable
                neighbor_edge = column[0].right.get_correspondent()  # 右隣のピースが持っているはずの辺を取得
                current = self.get_piece_by_edge(neighbor_edge)  # インデックスからその辺を持つピースを取得
                # 対応する辺が左側にくるように、ピースを回転させる
                current.let_edge_to_position(neighbor_edge, EdgePosition.LEFT)

            column = [current]
            while not current.bottom.is_flat:
                # 下隣のピースを取得
                neighbor_edge = current.bottom.get_correspondent()  # 下隣のピースが持っているはずの辺を取得
                neighbor_piece = self.get_piece_by_edge(neighbor_edge)  # インデックスからその辺を持つピースを取得
                # 対応する辺が上側にくるように、下隣のピースを回転させる
                neighbor_piece.let_edge_to_position(neighbor_edge, EdgePosition.TOP)

                column.append(neighbor_piece)
                current = neighbor_piece

            pieces.append(column)

            if current.right.is_flat:
                # 右下の角まで埋めたら終了
                break

        # 縦横の長さが違ったら、90度ずれてるので、回す
        if len(pieces) != self.frame.columns:
            self.rotate_pieces(pieces=pieces)

        # 全部まとめてフレームにはめる
        self.frame.set_pieces(pieces)

        if not self.frame.is_completed:
            raise Exception("solving is finished, but a frame has not completed yet. something is wrong.")

        return self.frame

    def make_indices(self, pieces: List[Piece]) -> None:
        self.indices = {}
        self.corner_pieces = []

        for piece in pieces:
            flat_count = 0
            for edge in piece.edges.values():
                if not edge.is_flat:
                    self.indices[edge] = piece
                else:
                    flat_count += 1

            if flat_count == 2:
                self.corner_pieces.append(piece)

    def get_piece_by_edge(self, edge: PieceEdge) -> Piece:
        """
        指定した辺の形状を持つピースを取得する

        インデックスを使わない場合はここを書き換えておけばok
        """
        return self.indices[edge]

    @staticmethod
    def rotate_corner_piece_as_left_top(piece: Piece) -> Piece:
        """
        角のピース（2辺が平坦なピース）を、左上にはまるように回転させる
        →　左辺と上辺が平坦になるように回転させる
        """
        if piece.top.is_flat and piece.right.is_flat:
            piece.rotate(3)
        elif piece.right.is_flat and piece.bottom.is_flat:
            piece.rotate(2)
        elif piece.bottom.is_flat and piece.left.is_flat:
            piece.rotate(1)
        elif piece.left.is_flat and piece.top.is_flat:
            pass
        else:
            raise ValueError("piece passed is not a corner piece.")

        return piece

    @staticmethod
    def rotate_pieces(pieces: List[List[Piece]]):
        """
        m * n のパズルピースを n * m に90度回転させる
        """
        original = copy(pieces)
        columns = len(original)
        rows = len(original[0])

        pieces.clear()
        for _ in range(rows):
            pieces.append([])

        for x in range(columns):
            for y in range(rows):
                piece = original[x][y]
                pieces[rows - 1 - y].append(piece)
                piece.rotate()


if __name__ == '__main__':
    frame, pieces_box = PuzzleFactory(columns=5, rows=3).factory()
    solver = PuzzleSolver(frame, pieces_box)
    frame = solver.solve()
    pass
