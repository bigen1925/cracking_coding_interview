from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional, List


class HashTableChain:
    first: Optional["HashTableChainNode"]
    last: Optional["HashTableChainNode"]

    def __init__(self):
        self.first = None
        self.last = None

    def append(self, key: Any, value: Any):
        node = HashTableChainNode(key=key, value=value)
        if self.first is None:
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node

    def find(self, key: Any) -> "HashTableChainNode":
        current = self.first

        while current:
            if current.key == key:
                return current
            else:
                current = current.next

        raise KeyError


@dataclass
class HashTableChainNode:
    key: Any
    value: Any
    next: Optional["HashTableChainNode"] = None


class HashTable:
    hasher: "Hasher"
    table_size: int
    chains: List[HashTableChain]

    def __init__(self, hasher: "Hasher" = None, table_size: int = 16):
        if hasher is None:
            hasher = ObjectHasher()

        self.hasher = hasher
        self.table_size = table_size

        self.chains = [HashTableChain() for _ in range(table_size)]

    # noinspection PyShadowingBuiltins
    def __setitem__(self, key, value):
        hash = self._get_hash(key)

        chain = self.chains[hash]

        try:
            node = chain.find(key)
            node.value = value
        except KeyError:
            chain.append(key, value)

    # noinspection PyShadowingBuiltins
    def __getitem__(self, key):
        hash = self._get_hash(key)
        return self.chains[hash].find(key).value

    def __repr__(self):
        content = ""
        for j, item in enumerate(self.chains):
            content += f"    [{j}] ::: "

            current = item.first
            items = []
            while current:
                items.append(f"({current.key}: {current.value})")
                current = current.next
            content += " => ".join(items) + "\n"

        return "{\n" + content + "}\n"

    def _get_hash(self, value):
        return self.hasher.hash(value) % self.table_size


class Hasher(ABC):
    @abstractmethod
    def hash(self, value) -> int:
        pass


class ObjectHasher:
    def hash(self, value) -> int:
        return value.__hash__()


class IdHasher:
    def hash(self, value) -> int:
        return id(value)


if __name__ == '__main__':
    ht = HashTable()

    # テーブルサイズ以上の数いれてももちろんOK
    for i in range(40):
        ht[i] = i

    print(ht)

    ht = HashTable(table_size=5)

    ht[1] = 1
    ht[1] = 2  # 更新もおっけー
    ht[6] = 3

    print(ht)
    print(f"ht[1] = {ht[1]}")
    print(f"ht[6] = {ht[6]}")
