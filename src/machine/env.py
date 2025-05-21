from typing import Protocol, TypeVar

T = TypeVar("T", covariant=True)
Id = TypeVar("Id", default=str)


class Env(Protocol[T]):
    """
    A protocol for the environment that can be used to evaluate expressions
    """

    def __getitem__(self, id: Id) -> T:
        """
        Get value from the environment.
        """
        raise NotImplementedError
