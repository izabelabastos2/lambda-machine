from typing import Generic, TypeVar

M = TypeVar("M")


class HoleError(Exception, Generic[M]):
    """
    Exception raised when a value hole is encountered during evaluation.
    """

    def __init__(self, meta: M):
        super().__init__("Hole encountered during program evaluation.")
        self.meta = meta
