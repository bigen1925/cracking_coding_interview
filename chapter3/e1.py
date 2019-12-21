class Separator:
    pass


class ThreeStackList(list):
    def __init__(self):
        super().__init__()
        self.append(Separator())  # 先頭
        self.append(Separator())  # stack1とstack2の区切り
        self.append(Separator())  # stack2とstack3の区切り
        self.append(Separator())  # 最後

    def add_stack(self, stack: int, item) -> "ThreeStackList":
        # O(n)
        # stackの最初のindexを取得
        first_index = self.get_stack_first_index(stack)
        # 要素を割り込ませる
        self.insert(first_index, item)

        return self

    def remove_stack(self, stack: int, item) -> "ThreeStackList":
        # O(n)
        # stackの最初のindexを取得
        first_index = self.get_stack_first_index(stack)
        # 要素を消す
        self.remove(first_index)

        return self

    def peek(self, stack: int):
        # O(n)
        # stackの最初のindexを取得
        first_index = self.get_stack_first_index(stack)
        # 先頭の値を取得
        return self[first_index]

    def is_empty(self, stack: int):
        # O(n)
        # stackの最初のindexを取得
        first_index = self.get_stack_first_index(stack)
        # 先頭が区切りインスタンスなら、空
        return isinstance(self[first_index], Separator)

    def get_seps(self) -> list:
        return [i for i, e in enumerate(self) if isinstance(e, Separator)]

    def get_stack_first_index(self, stack: int):
        seps = self.get_seps()
        return seps[stack - 1] + 1
