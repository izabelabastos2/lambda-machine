from __future__ import annotations

import inspect
from dataclasses import dataclass
from typing import Any, Callable, Iterable, Literal


class Node:
    def __init_subclass__(cls):
        cls._visit_children = None

    @classmethod
    def _compile_visitors(cls):
        annotations = inspect.get_annotations(cls)
        cls._visit_children = compile_visitor(annotations)

    def is_leaf(self) -> bool:
        """
        Leaf nodes cannot have Node children.
        """
        raise NotImplementedError

    def iter_children(self) -> Iterable[Node]:
        """
        Iterate over all Node children.
        """
        raise NotImplementedError

    def iter_descendants(self, method: Literal["bfs", "dfs"] = "dfs") -> Iterable[Node]:
        raise NotImplementedError


@dataclass
class Cursor:
    """
    A cursor is responsible for traversing a tree from the root node.
    """

    node: Node
    parent: Cursor | Node


def compile_visitor(
    annotations: dict[str, type],
) -> Callable[[Any], Iterable[Node]]:
    namespace: dict[str, type] = {}
    lines = ["def visit_children(self, node: None):"]

    src = "\n    ".join(lines)
    exec(src, namespace)
    return namespace["visit_children"]
