class Square:
    """Represents a square.

    This class defines a square by encapsulating its size.
    The size is stored as a private attribute and cannot be accessed directly.
    """
    def __init__(self, size):
        """Initializes a Square instance with a given size.

        Args:
            size (int or float): The size (length of one side) of the square.
        """
        self.__size = size
