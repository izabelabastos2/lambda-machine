from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar

from ..data.tree import Node
from ..env import Env
from .error import HoleError

M = TypeVar("M")
Atom = TypeVar("Atom", default=int)
Id = TypeVar("Id", default=str)
TagId = TypeVar("TagId", default=str)
RefId = TypeVar("RefId", default=str)
EffId = TypeVar("EffId", default=str)


@dataclass
class Expr(Generic[M, Atom, Id, TagId, RefId, EffId], Node):
    meta: M

    def eval[Data](self, env: Env[Data]):
        msg = f"Eval not implemented for {self.__class__.__name__}"
        raise NotImplementedError(msg)


@dataclass
class Hole(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A value hole is somewhat equivalent to NotImplemented.
    """

    def eval(self, env: Env):
        raise HoleError(self.meta)


@dataclass
class Var(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    An identifier/variable name.
    """

    name: Id


@dataclass
class Lit(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Represent a literal value of an atomic type.
    """

    value: Atom


@dataclass
class Ref(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A reference to a native value or a declaration in another module.
    """

    ref: RefId


@dataclass
class Lambda(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Lambda expression.
    """

    var: Id
    body: Expr[M, Atom, Id, TagId, RefId, EffId]


@dataclass
class Apply(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    Function application.
    """

    func: Expr[M, Atom, Id, TagId, RefId, EffId]
    param: Expr[M, Atom, Id, TagId, RefId, EffId]


@dataclass
class Let(Expr[M, Atom, Id, TagId, RefId, EffId]):
    """
    A let expression is a way to bind a value to a name in a local scope.
    """

    var: Id
    value: Expr[M, Atom, Id, TagId, RefId, EffId]
    body: Expr[M, Atom, Id, TagId, RefId, EffId]
