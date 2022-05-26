from dataclasses import dataclass


@dataclass
class MyClass:
    """This is a custom class.

    Use it as you like.

    .. math::
        \text{MultiHead}(Q, K, V) = \text{Concat}(head_1,\dots,head_h)W^O

    .. code-block:: python

        x = 1
        y = 2

    """

    a: int = 1
    b: str = "abc"

    def get_string(self) -> str:
        """Return a string

        Args:
            None

        Returns:
            A string

        """
        return self.b

    def get_int(self) -> int:
        """Return a string

        Args:
            None

        Returns:
            A string

        """
        return self.a

    def _private(self, a: int = 1) -> None:
        return a
