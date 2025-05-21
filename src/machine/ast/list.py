from dataclasses import dataclass

from .ast import Atom, EffId, Expr, Id, M, RefId, TagId


@dataclass
class Cons(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A cons cell constructor.
    """


@dataclass
class Empty(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Represents an empty list.
    """
