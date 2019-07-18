import numpy as np


def test_run1():
    # Dimensions in rows x columns
    print(np.array([(2, 3, 4), (5, 6, 7)]))
    print(np.empty((1, 4, 3)))
    print(np.ones((5, 4), dtype=np.int_))


def test_run2():
    print(np.random.rand(5, 4))
    print(np.random.normal(size=(2, 3)))  # Normal dist
    print(np.random.normal(50, 10, size=(2, 3)))  # Mean changed to 50 and s.d. to 10

    print(np.random.randint(10))  # Single integer between 0 to 10
    print(np.random.randint(0, 10))  # This time specifying low high explicit
    print(np.random.randint(0, 10, size=5))  # 5 random integers as a 1D array
    print(np.random.randint(0, 10, size=(2, 3)))  # 2x3


def test_run3():
    a = np.random.random((5, 4))
    print(a.shape[0])  # no of rows
    print(a.shape[1])  # no of columns
    print(len(a.shape))  # no of dimensions
    print(a.size)
    print(a.dtype)


test_run3()
