from dataclasses import dataclass

from .ast import Atom, EffId, Expr, Id, M, RefId, TagId


@dataclass
class Perform(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Perform an effect.
    """

    eff_id: EffId


@dataclass
class Handle(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A handle is a reference to a record.
    """

    eff_id: EffId
