import numpy as np


def test_run1():
    np.random.seed(693)
    a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random ints
    print("Array:\n", a)

    print("Sum of all elements:", a.sum())
    print("Sum of each column", a.sum(axis=0))
    print("Sum of each column", a.sum(axis=1))

    print("Min of each column:\n", a.min(axis=0))
    print("Max of each row:\n", a.max(axis=1))
    print("Mean of all elements:", a.mean())


def get_max_index(a):
    """Return the index of the maximum value in given 1D array."""
    return a.argmax()


def test_run2():
    a = np.array([9, 6, 2, 3, 12, 14, 7, 10], dtype=np.int32)  # 32-bit integer array
    print("Array:", a)

    # Find the maximum and its index in array
    print("Maximum value:", a.max())
    print("Index of max.:", get_max_index(a))


test_run2()
