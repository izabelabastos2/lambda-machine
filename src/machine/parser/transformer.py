from lark import Transformer, v_args

from ..ast import *


@v_args(inline=True, meta=True)
class LambdaTransformer(Transformer):
    """
    A class to transform a lambda expression into a more manageable form.
    """
