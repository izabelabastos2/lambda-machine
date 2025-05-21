from pathlib import Path

from lark import Lark

from .transformer import LambdaTransformer

__all__ = ["grammar", "parse", "lex"]

GRAMMAR = Path(__file__).parent / "grammar.lark"


with GRAMMAR.open() as fd:
    grammar = Lark(
        fd,
        parser="lalr",
        start="start",
        transformer=LambdaTransformer(),
    )
