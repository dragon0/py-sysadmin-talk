def hypotenuse(x, y):
    """Computes the distance from the origin to the point (x, y)

    :param x: the point's x-coordinate
    :param y: the point's y-coordinate
    :return: number. the distance from (0, 0) to the point (x, y)

    >>> hypotenuse(3, 4)
    5.0
    >>> hypotenuse(5, 12)
    13.0
    """
    return (x**2 + y**2) ** 0.5

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)