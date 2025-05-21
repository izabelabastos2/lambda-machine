from dataclasses import dataclass

from .ast import Atom, EffId, Expr, Id, M, RefId, TagId


@dataclass
class Pair(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A pair constructor.
    """
