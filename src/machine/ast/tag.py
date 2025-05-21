from dataclasses import dataclass

from .ast import Atom, EffId, Expr, Id, M, RefId, TagId


@dataclass
class Tag(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A tag constructor.

    Represents a function `value -> tagged_value`.
    """

    tag_id: TagId


@dataclass
class Case(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Match any value with the given tag.
    """

    tag_id: TagId


@dataclass
class CaseIs(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Match any value with the given tag and atomic value.
    """

    tag_id: TagId
    value: Atom


@dataclass
class NoCases(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A case expression with no cases.
    """
