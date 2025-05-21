from dataclasses import dataclass

from .ast import Atom, EffId, Expr, Id, M, RefId, TagId


@dataclass
class Record(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A record is a collection of key-value pairs.

    The empty record is the nil type.
    """

    fields: dict[str, Expr[M, Atom, Id, TagId, RefId, EffId]]


@dataclass
class AddField(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A function `value -> record -> record'` that adds a field to a record.
    """

    field: str


@dataclass
class SelectField(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A function `record -> value` that selects a field from a record.
    """

    field: str


@dataclass
class RemoveField(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A function `record -> record'` that selects a field from a record.
    """

    field: str
